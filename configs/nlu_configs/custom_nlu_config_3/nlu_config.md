language: "en"

pipeline:
- name: "nlp_spacy"
  model: "en"
  # when retrieving word vectors, this will decide if the casing
  # of the word is relevant. E.g. `hello` and `Hello` will
  # retrieve the same vector, if set to `false`. For some
  # applications and models it makes sense to differentiate
  # between these two words, therefore setting this to `true`.
  case_sensitive: false
- name: "tokenizer_spacy"
- name: "intent_entity_featurizer_regex"
- name: "intent_featurizer_spacy"
- name: "components.modified_crf_entity_extractor.ModifiedCRFEntityExtractor"
- name: "components.dict_ner_extractor.DictNerExtractor"
- name: "ner_synonyms"
- name: "intent_featurizer_count_vectors"
  max_ngram: 4
- name: "intent_featurizer_ngrams"
- name: "intent_classifier_sklearn"
  gamma: [0.1, 1, 10, 100]
  kernal: ["linear", "rbf", "poly"]
- name: "ner_duckling_http"
  url: "http://localhost:8000"
  dimensions: ["time", "amount-of-money", "duration", "distance", "volume", "ordinal", "email"]
  locale: "en_US"
  timezone: "Asia/Ho_Chi_Minh"