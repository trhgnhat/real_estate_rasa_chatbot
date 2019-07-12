import matplotlib.pylab as plt
import numpy as np
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
    evaluate_result_dir = 'evaluation_results/NLU/' + model_dir.split("/")[-1] + "/"
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
    for actual in data:
        false_pred = False  # means predict correctly
        pred = interpreter.parse(actual['text'])
        pred['entities'] = sorted(pred['entities'], key=itemgetter('start'))
        if "entities" not in actual:
            actual['entities'] = []
        if "entities" in actual and "entities" in pred and len(pred['entities']) > 0:
            if len(pred['entities']) != len(actual['entities']):
                false_pred = True
            else:
                for idx, pred_entity in enumerate(pred['entities']):
                    true_entity = actual["entities"][idx]
                    if pred_entity['start'] != true_entity['start'] and \
                            pred_entity['end'] != true_entity['end'] and \
                            pred_entity['value'] != true_entity['value'] and \
                            pred_entity['entity'] != true_entity['entity']:
                        false_pred = True
        if false_pred:
            false_data['examples'].append(
                {"text": actual['text'], "true": actual["entities"], "predict": pred["entities"]})
        else:
            true_data['examples'].append(
                {"text": actual['text'], "true": actual["entities"], "predict": pred["entities"]})
    false_data['support'] = len(false_data['examples'])
    true_data['support'] = len(true_data['examples'])
    with open(evaluate_result_dir + 'entity_extractor_errors.json', 'w') as outfile:
        json.dump(false_data, outfile, indent=4)
    with open(evaluate_result_dir + 'entity_extractor_successes.json', 'w') as outfile:
        json.dump(true_data, outfile, indent=4)


def plot_metrics(metric_list, title, type, save_path=None):
    # runs through each test case and adds a set of bars to a plot.  Saves

    f, (ax1) = plt.subplots(1, 1)
    plt.grid(True)
    idx = 0
    for each in metric_list:
        bar_metrics(each, ax1, title, index=idx)
        idx += 1

    if save_path is None:
        save_path = 'img/NLU/' + type + '/bar_' + title + '.png'

    plt.savefig(save_path, dpi=400)


def bar_metrics(metrics, ax, title, index=0):
    # adds a set of metrics bars to the axis 'ax' of the plot
    precision = metrics['precision']
    recall = metrics['recall']
    f1 = metrics['f1-score']
    width = 0.2
    shift = index * width
    indeces = [r + shift for r in np.arange(3)]
    metric_list = [precision, recall, f1]
    ax.set_title(title.replace("_", " "))
    ax.set_axisbelow(True)
    ax.bar(indeces, metric_list, width)
    ax.set_xticks([r + width / 2 for r in np.arange(3)])
    ax.set_xticklabels(('precision', 'recall', 'f1'))
    ax.legend(all_configs_dir_name, loc='upper center', bbox_to_anchor=(0.5, -0.05),
              fancybox=True, shadow=True, ncol=4)
    ax.set_ylabel('score')


if __name__ == '__main__':
    from evaluator.nereval import evaluate_json as evaluate_entity

    all_configs_dir_name = [
        # "Baseline",
        "Custom",
        "Custom new",
        # "Spacy NLP",
        # "TensorFlow Embedding"
    ]
    all_configs_dir = [
        # "custom_nlu_config_1",
        "custom_nlu_config_2",
        "official",
        # "spacy_nlp_config",
        # "tensorflow_embedding_config"
    ]
    intent_metric_list = []
    entity_metric_list = []
    for each in all_configs_dir:
        config_dir = 'configs/nlu_configs/' + each + "/nlu_config.md"
        # train_nlu(data_path='data/', configs=config_dir, model_dir='models/nlu')
        evaluate_nlu('models/nlu/default/' + each)
        with open('evaluation_results/NLU/' + each + "/intent_report.json") as json_file:
            data = json.load(json_file)
            del (data['weighted avg']["support"])
            intent_metric_list.append(data["weighted avg"])
        print("\nmodel 1")
        file_names = [
            'evaluation_results/NLU/' + each + "/entity_extractor_errors.json",
            'evaluation_results/NLU/' + each + "/entity_extractor_successes.json"
        ]
        f1, p, r = evaluate_entity(file_names)
        entity_metric_list.append({"f1-score": f1, "precision": p, "recall": r})
    plot_metrics(intent_metric_list, "intent_custom_pipeline", type="intent")
    plot_metrics(entity_metric_list, "entity_custom_pipeline", type="entity")
