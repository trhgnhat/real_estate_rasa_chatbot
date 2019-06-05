import logging
import os
import re
import warnings
import io
import sys

import typing
from typing import Any, Dict, List, Optional, Text

from rasa_nlu import utils
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.featurizers import Featurizer
from rasa_nlu.training_data import Message
from rasa_nlu.training_data import TrainingData
from fuzzywuzzy import process, fuzz

import numpy as np

logger = logging.getLogger(__name__)

if typing.TYPE_CHECKING:
    from rasa_nlu.model import Metadata

STOPWORDS = [line.replace("\n", "") for line in open("data/corpus/stopwords.txt", "r").readlines()]

REGEX_FEATURIZER_FILE_NAME = "fuzzy_wuzzy_regex_featurizer.json"


class FuzzyWuzzyRegexFeaturizer(Featurizer):
    name = "fuzzywuzzy_regex_featurizer"

    provides = ["text_features"]

    requires = ["tokens"]

    def __init__(self, component_config=None,
                 known_patterns=None, lookup_tables=None, lookup_tables_features=None):

        super(FuzzyWuzzyRegexFeaturizer, self).__init__(component_config)

        self.known_patterns = known_patterns if known_patterns else []
        lookup_tables = lookup_tables or []
        self._add_lookup_table_regexes(lookup_tables)
        self.lookup_tables_features = lookup_tables_features or {}

    def train(self, training_data, config, **kwargs):
        # type: (TrainingData, RasaNLUModelConfig, **Any) -> None

        self.known_patterns = training_data.regex_features
        self._add_lookup_table_regexes(training_data.lookup_tables)

        for example in training_data.training_examples:
            updated = self._text_features_with_regex(example)
            example.set("text_features", updated)

    def process(self, message, **kwargs):
        # type: (Message, **Any) -> None

        updated = self._text_features_with_regex(message)
        message.set("text_features", updated)

    def _text_features_with_regex(self, message):
        if self.known_patterns:
            extras = self.features_for_patterns(message)
            return self._combine_with_existing_text_features(message, extras)
        else:
            return message.get("text_features")

    def _add_lookup_table_regexes(self, lookup_tables):
        # appends the regex features from the lookup tables to
        # self.known_patterns
        for table in lookup_tables:
            regex_pattern = self._generate_lookup_regex(table)
            lookup_regex = {'name': table['name'],
                            'pattern': regex_pattern}
            self.known_patterns.append(lookup_regex)

    def features_for_patterns(self, message):
        """Checks which known patterns match the message.

        Given a sentence, returns a vector of {1,0} values indicating which
        regexes did match. Furthermore, if the
        message is tokenized, the function will mark all tokens with a dict
        relating the name of the regex to whether it was matched."""

        matches = []
        for i, exp in enumerate(self.known_patterns):
            match = re.search(exp["pattern"], message.text)
            matches.append(match)
            for token_index, t in enumerate(message.get("tokens", [])):
                patterns = t.get("pattern", default={})
                if match is not None:
                    if t.offset < match.end() and t.end > match.start():
                        patterns[exp["name"]] = True
                    else:
                        patterns[exp["name"]] = False
                else:
                    patterns[exp["name"]] = False
                t.set("pattern", patterns)
        found = [1.0 if m is not None else 0.0 for m in matches]
        return np.array(found)

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
        if lookup_table['name'] not in self.lookup_tables_features:
            self.lookup_tables_features[lookup_table['name']] = []
        [self.lookup_tables_features[lookup_table['name']].append(each) for each in elements_to_regex]
        # sanitize the regex, escape special characters
        elements_sanitized = [re.escape(e) for e in elements_to_regex]
        # regex matching elements with word boundaries on either side
        regex_string = '(?i)(\\b' + '\\b|\\b'.join(elements_sanitized) + '\\b)'
        return regex_string

    @classmethod
    def load(cls,
             model_dir=None,  # type: Optional[Text]
             model_metadata=None,  # type: Optional[Metadata]
             cached_component=None,  # type: Optional[RegexFeaturizer]
             **kwargs  # type: **Any
             ):
        # type: (...) -> RegexFeaturizer

        meta = model_metadata.for_component(cls.name)

        file_name = meta.get("regex_file", REGEX_FEATURIZER_FILE_NAME)
        regex_file = os.path.join(model_dir, file_name)
        if os.path.exists(regex_file):
            known_patterns = utils.read_json_file(regex_file)
        else:
            known_patterns = []

        file_name = meta.get("regex_fuzwuz_table_file", "fuzzy_wuzzy_regex_featurizer_lookup_tables.json")
        regex_fuzwuz_table_file = os.path.join(model_dir, file_name)
        if os.path.exists(regex_fuzwuz_table_file):
            lookup_tables_features = utils.read_json_file(regex_fuzwuz_table_file)
        else:
            lookup_tables_features = {}

        return FuzzyWuzzyRegexFeaturizer(meta, known_patterns=known_patterns,
                                         lookup_tables_features=lookup_tables_features)

    def persist(self, model_dir, saveLookupTablesJson=True):
        # type: (Text) -> Optional[Dict[Text, Any]]
        """Persist this model into the passed directory.

        Return the metadata necessary to load the model again."""

        regex_file = os.path.join(model_dir, REGEX_FEATURIZER_FILE_NAME)
        utils.write_json_to_file(regex_file, self.known_patterns, indent=4)
        if saveLookupTablesJson:
            regex_file = os.path.join(model_dir, "fuzzy_wuzzy_regex_featurizer_lookup_tables.json")
            utils.write_json_to_file(regex_file, self.lookup_tables_features, indent=4)

        return {"regex_file": REGEX_FEATURIZER_FILE_NAME,
                "regex_fuzwuz_table_file": "fuzzy_wuzzy_regex_featurizer_lookup_tables.json"}
