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
- name: "ner_crf"
  BILOU_flag: True
  max_iterations: 100
  features:
    - ["prefix5", "prefix2", "suffix5",  "suffix2",  "upper", "digit", "pattern", "pos", "pos2"]
    - ["bias", "low", "prefix5", "prefix2", "suffix5",  "upper", "title", "digit", "pattern", "pos", "pos2"]
    - ["prefix5", "prefix2", "suffix5",  "suffix2",  "upper", "digit", "pattern", "pos", "pos2"]
- name: "components.dict_ner_extractor.DictNerExtractor"
- name: "ner_synonyms"
- name: "intent_featurizer_count_vectors"
  token_pattern: '(?u)\b\w+\b'
  max_ngram: 4
- name: "intent_featurizer_ngrams"
- name: "intent_classifier_tensorflow_embedding"
  batch_size: 10
  epochs: 300