#!/usr/bin/env bash
cd ../
rasa train nlu --nlu data/data.md -c configs/nlu_configs/custom_nlu_config_1/nlu_config.md --out models/nlu --fixed-model-name custom_nlu_config_1
rasa test nlu --nlu data/data_test.md --model models/nlu/custom_nlu_config_1.tar.gz --report configs/nlu_configs/custom_nlu_config_1/evaluate/reports --successes configs/nlu_configs/custom_nlu_config_1/evaluate/successes.json --errors configs/nlu_configs/custom_nlu_config_1/evaluate/errors.json --histogram configs/nlu_configs/custom_nlu_config_1/evaluate/hist.png --confmat configs/nlu_configs/custom_nlu_config_1/evaluate/confmat.png

rasa train nlu --nlu data/data.md -c configs/nlu_configs/custom_nlu_config_2/nlu_config.md --out models/nlu --fixed-model-name custom_nlu_config_2
rasa test nlu --nlu data/data_test.md --model models/nlu/custom_nlu_config_2.tar.gz --report configs/nlu_configs/custom_nlu_config_2/evaluate/reports --successes configs/nlu_configs/custom_nlu_config_2/evaluate/successes.json --errors configs/nlu_configs/custom_nlu_config_2/evaluate/errors.json --histogram configs/nlu_configs/custom_nlu_config_2/evaluate/hist.png --confmat configs/nlu_configs/custom_nlu_config_2/evaluate/confmat.png

rasa train nlu --nlu data/data.md -c configs/nlu_configs/custom_nlu_config_3/nlu_config.md --out models/nlu --fixed-model-name custom_nlu_config_3
rasa test nlu --nlu data/data_test.md --model models/nlu/custom_nlu_config_3.tar.gz --report configs/nlu_configs/custom_nlu_config_3/evaluate/reports --successes configs/nlu_configs/custom_nlu_config_3/evaluate/successes.json --errors configs/nlu_configs/custom_nlu_config_3/evaluate/errors.json --histogram configs/nlu_configs/custom_nlu_config_3/evaluate/hist.png --confmat configs/nlu_configs/custom_nlu_config_3/evaluate/confmat.png

rasa train nlu --nlu data/data.md -c configs/nlu_configs/pretrained_spacy_config/nlu_config.md --out models/nlu --fixed-model-name pretrained_spacy_config
rasa test nlu --nlu data/data_test.md --model models/nlu/pretrained_spacy_config.tar.gz --report configs/nlu_configs/pretrained_spacy_config/evaluate/reports --successes configs/nlu_configs/pretrained_spacy_config/evaluate/successes.json --errors configs/nlu_configs/pretrained_spacy_config/evaluate/errors.json --histogram configs/nlu_configs/pretrained_spacy_config/evaluate/hist.png --confmat configs/nlu_configs/pretrained_spacy_config/evaluate/confmat.png

rasa train nlu --nlu data/data.md -c configs/nlu_configs/supervised_tensorflow_config/nlu_config.md --out models/nlu --fixed-model-name supervised_tensorflow_config
rasa test nlu --nlu data/data_test.md --model models/nlu/supervised_tensorflow_config.tar.gz --report configs/nlu_configs/supervised_tensorflow_config/evaluate/reports --successes configs/nlu_configs/supervised_tensorflow_config/evaluate/successes.json --errors configs/nlu_configs/supervised_tensorflow_config/evaluate/errors.json --histogram configs/nlu_configs/supervised_tensorflow_config/evaluate/hist.png --confmat configs/nlu_configs/supervised_tensorflow_config/ev
