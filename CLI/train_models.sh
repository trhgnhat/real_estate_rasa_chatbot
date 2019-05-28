#!/usr/bin/env bash
cd ../

rasa train nlu --nlu data/training_data.md -c configs/nlu_configs/custom_nlu_config_1/nlu_config.md --out models/nlu --fixed-model-name custom_nlu_config_1
rasa train nlu --nlu data/training_data.md -c configs/nlu_configs/custom_nlu_config_2/nlu_config.md --out models/nlu --fixed-model-name custom_nlu_config_2
rasa train nlu --nlu data/training_data.md -c configs/nlu_configs/custom_nlu_config_3/nlu_config.md --out models/nlu --fixed-model-name custom_nlu_config_3
rasa train nlu --nlu data/training_data.md -c configs/nlu_configs/pretrained_spacy_config/nlu_config.md --out models/nlu --fixed-model-name pretrained_spacy_config
rasa train nlu --nlu data/training_data.md -c configs/nlu_configs/supervised_tensorflow_config/nlu_config.md --out models/nlu --fixed-model-name supervised_tensorflow_config
