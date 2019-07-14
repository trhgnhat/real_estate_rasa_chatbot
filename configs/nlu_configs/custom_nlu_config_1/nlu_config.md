language: "en"

pipeline:
- name: "nlp_spacy"
  model: "en"
- name: "ner_duckling_http"
  # url of the running duckling server
  url: "http://localhost:8000"
  # dimensions to extract
  dimensions: ["time", "amount-of-money", "phone-number", "duration", "distance", "volume", "ordinal", "number", "email"]
  # allows you to configure the locale, by default the language is
  # used
  locale: "en_US"
  # if not set the default timezone of Duckling is going to be used
  # needed to calculate dates from relative expressions like "tomorrow"
  timezone: "Asia/Ho_Chi_Minh"
