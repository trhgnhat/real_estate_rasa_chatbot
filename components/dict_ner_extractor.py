from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import os
import re
import io
import numpy as np

import typing
from builtins import str
from typing import Any, Dict, List, Optional, Text, Tuple
from rasa_nlu import utils
from rasa_nlu.config import RasaNLUModelConfig, InvalidConfigError
from rasa_nlu.extractors import EntityExtractor
from rasa_nlu.model import Metadata
from rasa_nlu.training_data import Message
from rasa_nlu.training_data import TrainingData
from fuzzywuzzy import process, fuzz

try:
    import spacy
except ImportError:
    spacy = None

logger = logging.getLogger(__name__)

if typing.TYPE_CHECKING:
    import sklearn_crfsuite

DICT_NER_MODEL_FILE_NAME = "dict_ner_extractor.json"
STOPWORDS = [line.replace("\n", "") for line in open("data/corpus/stopwords.txt", "r").readlines()]


class DictNerExtractor(EntityExtractor):
    name = "dict_ner_extractor"

    provides = ["entities"]
    requires = []
    defaults = {}
    language_list = ["en"]

    def __init__(self, component_config=None, known_patterns=None, lookup_tables=None):
        super(DictNerExtractor, self).__init__(component_config)
        self.known_patterns = known_patterns if known_patterns else []
        lookup_tables = lookup_tables or []

    def _add_lookup_table_regexes(self, lookup_tables):
        # appends the regex features from the lookup tables to
        # self.known_patterns
        for table in lookup_tables:
            regex_pattern = self._generate_lookup_regex(table)
            lookup_regex = {'name': table['name'],
                            'pattern': regex_pattern}
            self.known_patterns.append(lookup_regex)

    def _generate_lookup_regex(self, lookup_table):
        """creates a regex out of the contents of a lookup table file"""
        lookup_elements = lookup_table['elements']
        elements_to_regex = []

        # if it's a list, it should be the elements directly
        if isinstance(lookup_elements, list):
            elements_to_regex = lookup_elements

        # otherwise it's a file path.
        else:

            try:
                f = io.open(lookup_elements, 'r')
            except IOError:
                raise ValueError("Could not load lookup table {}"
                                 "Make sure you've provided the correct path"
                                 .format(lookup_elements))

            with f:
                for line in f:
                    new_element = line.strip()
                    if new_element:
                        elements_to_regex.append(new_element)
        # sanitize the regex, escape special characters
        elements_to_regex = ["".join(["[" + char + "]+" if (char != " ") else "[" + char + "]*" for char in e]) + "[s]*"
                             for e in elements_to_regex]
        # regex matching elements with word boundaries on either side
        regex_string = '(?i)(' + '|'.join(elements_to_regex) + ')'
        return regex_string

    def extract_for_patterns(self, message):
        """Checks which known patterns match the message.

        Given a sentence, returns a vector of {1,0} values indicating which
        regexes did match. Furthermore, if the
        message is tokenized, the function will mark all tokens with a dict
        relating the name of the regex to whether it was matched."""

        matches = []
        for i, exp in enumerate(self.known_patterns):
            match = re.findall(exp["pattern"], message.text)
            if len(match) > 0:
                [matches.append([exp['name'], each]) for each in match]
        return matches

    def train(self, training_data, cfg, **kwargs):
        """Not needed, because the the model is pretrained"""
        self._add_lookup_table_regexes(training_data.lookup_tables)

    def convert_to_rasa(self, value, entity, start, end, confidence=1):
        """Convert model output into the Rasa NLU compatible output format."""

        result = {"value": value,
                  "confidence": confidence,
                  "entity": entity,
                  "start": start,
                  "end": end,
                  "extractor": self.name}

        return result

    def process(self, message, **kwargs):
        """Retrieve the text message, pass it to the classifier
            and append the prediction results to the message class."""
        entities = []
        results = self.extract_for_patterns(message)
        for each in results:
            start = message.text.index(each[1])
            end = start + len(each[1])
            save = True
            # check if the entity are not recognized by ner_crf yet, otherwise pass
            for ent in message.get("entities", []):
                if ent['value'].lower() == each[1].lower() and ent['start'] == start and each[0] in ent['entity'].split(
                        "/"):
                    save = False
                    break
            if save:
                entity = self.convert_to_rasa(each[1], each[0], start, end)
                entities.append(entity)

        message.set("entities", message.get("entities", []) + entities, add_to_output=True)

    def persist(self, model_dir):
        """Pass because a pre-trained model is already persisted"""
        regex_file = os.path.join(model_dir, DICT_NER_MODEL_FILE_NAME)
        utils.write_json_to_file(regex_file, self.known_patterns, indent=4)

        return {"dict_ner_file": DICT_NER_MODEL_FILE_NAME}

    @classmethod
    def load(cls,
             model_dir=None,  # type: Optional[Text]
             model_metadata=None,  # type: Optional[Metadata]
             cached_component=None,  # type: Optional[RegexFeaturizer]
             **kwargs  # type: **Any
             ):
        # type: (...) -> RegexFeaturizer

        meta = model_metadata.for_component(cls.name)

        file_name = meta.get("dict_ner_file", DICT_NER_MODEL_FILE_NAME)
        regex_file = os.path.join(model_dir, file_name)
        if os.path.exists(regex_file):
            known_patterns = utils.read_json_file(regex_file)
        else:
            known_patterns = []

        return DictNerExtractor(meta, known_patterns=known_patterns)
