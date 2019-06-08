from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
from rasa_nlu.evaluate import run_evaluation
from operator import itemgetter
import pprint
import json


def train_nlu(data_path, configs, model_dir):
    training_data = load_data(data_path + "training_data.md")
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)
    fixed_model_name = configs.split("/")[2]
    # save model
    model_directory = trainer.persist(model_dir, fixed_model_name=fixed_model_name)


def evaluate_nlu(model_dir):
    interpreter = Interpreter.load(model_dir)
    test_data_path = "data/test_data.json"
    evaluate_result_dir = 'configs/nlu_configs/' + model_dir.split("/")[-1] + '/evaluate/'
    run_evaluation("data/test_data.md",
                   model_dir,
                   report_folder=evaluate_result_dir,
                   successes_filename=evaluate_result_dir + 'successes.json',
                   errors_filename=evaluate_result_dir + 'errors.json')
    # ,
    # confmat_filename = evaluate_result_dir + 'confmat.png',
    # intent_hist_filename = evaluate_result_dir + 'intent_hist.png'
    with open(test_data_path, 'r') as f:
        data = json.load(f)
        data = data["rasa_nlu_data"]["common_examples"]
    false_data = {'examples': []}
    true_data = {'examples': []}
    for each in data:
        false_pred = False  # means predict correctly
        pred = interpreter.parse(each['text'])
        pred['entities'] = sorted(pred['entities'], key=itemgetter('start'))
        if "entities" not in each:
            each['entities'] = []
        if "entities" in each and "entities" in pred and len(pred['entities']) > 0:
            if len(pred['entities']) != len(each['entities']):
                false_pred = True
            else:
                for idx, pred_entity in enumerate(pred['entities']):
                    true_entity = each["entities"][idx]
                    if pred_entity['start'] != true_entity['start'] and \
                            pred_entity['end'] != true_entity['end'] and \
                            pred_entity['value'] != true_entity['value'] and \
                            pred_entity['entity'] != true_entity['entity']:
                        false_pred = True
        if false_pred:
            false_data['examples'].append({"text": each['text'], "true": each["entities"], "predict": pred["entities"]})
        else:
            true_data['examples'].append({"text": each['text'], "true": each["entities"], "predict": pred["entities"]})
    false_data['support'] = len(false_data['examples'])
    true_data['support'] = len(true_data['examples'])
    with open(evaluate_result_dir + 'entity_extractor_errors.json', 'w') as outfile:
        json.dump(false_data, outfile, indent=4)
    with open(evaluate_result_dir + 'entity_extractor_successes.json', 'w') as outfile:
        json.dump(true_data, outfile, indent=4)


if __name__ == '__main__':
    all_configs_dir = [
        # "custom_nlu_config_1",
        # "custom_nlu_config_2",
        "custom_nlu_config_3",
        # "spacy_nlp_config",
        # "tensorflow_embedding_config"
    ]
    for each in all_configs_dir:
        config_dir = 'configs/nlu_configs/' + each + "/nlu_config.md"
        train_nlu(data_path='data/', configs=config_dir, model_dir='models/nlu')
        evaluate_nlu('models/nlu/default/' + each)
