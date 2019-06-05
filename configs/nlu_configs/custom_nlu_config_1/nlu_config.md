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
  features:
    - ["bias", "low", "prefix5", "prefix2", "suffix5", "suffix3", "suffix2", "upper", "title", "digit", "pattern", "pos", "pos2", "upper"]
    - ["bias", "low", "prefix5", "prefix2", "suffix5", "suffix3", "suffix2", "upper", "title", "digit", "pattern", "pos", "pos2", "upper"]
    - ["bias", "low", "prefix5", "prefix2", "suffix5", "suffix3", "suffix2", "upper", "title", "digit", "pattern", "pos", "pos2", "upper"]
  BILOU_flag: true
  # This is the value given to sklearn_crfcuite.CRF tagger before training.
  max_iterations: 100
  # This is the value given to sklearn_crfcuite.CRF tagger before training.
  # Specifies the L1 regularization coefficient.
  L1_c: 1
  # This is the value given to sklearn_crfcuite.CRF tagger before training.
  # Specifies the L2 regularization coefficient.
  L2_c: 1e-3
- name: "ner_synonyms"
- name: "intent_featurizer_count_vectors"
  token_pattern: '(?u)\b\w+\b'
  max_ngram: 4
- name: "intent_featurizer_ngrams"
- name: "intent_classifier_tensorflow_embedding"
  intent_tokenization_flag: false
  batch_size: 10
  epochs: 500
