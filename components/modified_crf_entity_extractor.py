from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import os

import typing
from builtins import str
from typing import Any, Dict, List, Optional, Text, Tuple

from rasa_nlu.config import RasaNLUModelConfig, InvalidConfigError
from rasa_nlu.extractors.crf_entity_extractor import CRFEntityExtractor
from rasa_nlu.model import Metadata
from rasa_nlu.training_data import Message
from rasa_nlu.training_data import TrainingData

try:
    import spacy
except ImportError:
    spacy = None

logger = logging.getLogger(__name__)

if typing.TYPE_CHECKING:
    import sklearn_crfsuite

CRF_MODEL_FILE_NAME = "crf_model.pkl"


class ModifiedCRFEntityExtractor(CRFEntityExtractor):
    name = "modified_crf_entity_extractor"

    provides = ["entities"]

    requires = ["tokens"]

    defaults = {
        # BILOU_flag determines whether to use BILOU tagging or not.
        # More rigorous however requires more examples per entity
        # rule of thumb: use only if more than 100 egs. per entity
        "BILOU_flag": True,

        # crf_features is [before, word, after] array with before, word,
        # after holding keys about which
        # features to use for each word, for example, 'title' in
        # array before will have the feature
        # "is the preceding word in title case?"
        # POS features require spaCy to be installed
        "features": [
            ["low", "title", "upper"],
            ["bias", "low", "prefix5", "prefix2", "suffix5", "suffix3",
             "suffix2", "upper", "title", "digit", "pattern"],
            ["low", "title", "upper"]],

        # The maximum number of iterations for optimization algorithms.
        "max_iterations": 50,

        # weight of theL1 regularization
        "L1_c": 0.1,

        # weight of the L2 regularization
        "L2_c": 0.1
    }

    function_dict = {
        'low': lambda doc: doc[0].lower(),
        'title': lambda doc: doc[0].istitle(),
        'prefix5': lambda doc: doc[0][:5],
        'prefix2': lambda doc: doc[0][:2],
        'suffix5': lambda doc: doc[0][-5:],
        'suffix3': lambda doc: doc[0][-3:],
        'suffix2': lambda doc: doc[0][-2:],
        'suffix1': lambda doc: doc[0][-1:],
        'pos': lambda doc: doc[1],
        'pos2': lambda doc: doc[1][:2],
        'bias': lambda doc: 'bias',
        'upper': lambda doc: doc[0].isupper(),
        'digit': lambda doc: doc[0].isdigit(),
        'pattern': lambda doc: doc[3],
    }

    def __init__(self, component_config=None, ent_tagger=None):
        # type: (sklearn_crfsuite.CRF, Dict[Text, Any]) -> None

        super(CRFEntityExtractor, self).__init__(component_config)

        self.ent_tagger = ent_tagger

        self._validate_configuration()

        self._check_pos_features_and_spacy()

    def _train_model(self, df_train):
        # type: (List[List[Tuple[Text, Text, Text, Text]]]) -> None
        """Train the crf tagger based on the training data."""
        import sklearn_crfsuite

        X_train = [self._sentence_to_features(sent) for sent in df_train]
        y_train = [self._sentence_to_labels(sent) for sent in df_train]

        from itertools import chain

        import nltk
        import sklearn
        import scipy.stats
        from sklearn.metrics import make_scorer
        from sklearn.model_selection import cross_val_score
        from sklearn.model_selection import RandomizedSearchCV

        import sklearn_crfsuite
        from sklearn_crfsuite import scorers
        from sklearn_crfsuite import metrics

        X_train = [self._sentence_to_features(sent) for sent in df_train]
        y_train = [self._sentence_to_labels(sent) for sent in df_train]
        self.ent_tagger = sklearn_crfsuite.CRF(
            algorithm='lbfgs',
            # stop earlier
            max_iterations=self.component_config["max_iterations"],
            # include transitions that are possible, but not observed
            all_possible_transitions=True
        )
        self.ent_tagger.fit(X_train, y_train)

        params_space = {
            'c1': scipy.stats.expon(scale=0.5),
            'c2': scipy.stats.expon(scale=0.5),
        }
        labels = self.ent_tagger.classes_

        # use the same metric for evaluation
        f1_scorer = make_scorer(metrics.flat_f1_score,
                                average='weighted', labels=labels)

        # search
        rs = RandomizedSearchCV(self.ent_tagger, params_space,
                                cv=10,
                                verbose=1,
                                n_jobs=-1,
                                n_iter=100,
                                scoring=f1_scorer)
        rs.fit(X_train, y_train)
        print('best params:', rs.best_params_)
        print('best CV score:', rs.best_score_)
        print('model size: {:0.2f}M'.format(rs.best_estimator_.size_ / 1000000))
        self.ent_tagger = sklearn_crfsuite.CRF(
            algorithm='lbfgs',
            c1=rs.best_params_["c1"],
            c2=rs.best_params_["c2"],
            # stop earlier
            max_iterations=self.component_config["max_iterations"],
            # include transitions that are possible, but not observed
            all_possible_transitions=True
        )
        self.ent_tagger.fit(X_train, y_train)
