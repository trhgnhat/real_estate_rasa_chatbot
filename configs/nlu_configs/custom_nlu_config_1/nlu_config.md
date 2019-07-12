language: "en"

pipeline:
- name: "nlp_spacy"
  model: "en"
- name: "tokenizer_spacy"
- name: "intent_entity_featurizer_regex"
- name: "ner_crf"
##- name: "ner_synonyms"
- name: "intent_featurizer_count_vectors"
- name: "intent_featurizer_ngrams"
- name: "intent_classifier_tensorflow_embedding"
