import logging
import rasa_core
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.form_policy import FormPolicy
from rasa_core.policies.embedding_policy import EmbeddingPolicy
from rasa_core.policies.memoization import AugmentedMemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.run import serve_application
from rasa_core.evaluate import run_story_evaluation
import matplotlib.pylab as plt
import numpy as np
import json
import os

logger = logging.getLogger(__name__)

DATA_PATH = "D:/workspace/Pet Project/Rasa NLP NLU/House/"


def train_dialogue(policies,
                   model_path='models/core/',
                   name="general",
                   domain_file='house_domain.yml',
                   training_data_file='data/stories.md'):
    # this will catch predictions the model isn't very certain about
    # there is a threshold for the NLU predictions as well as the action predictions

    agent = Agent(DATA_PATH + domain_file, policies=policies)
    data = agent.load_data(DATA_PATH + training_data_file)
    agent.train(data)
    agent.persist(DATA_PATH + model_path + name)
    return DATA_PATH + model_path + name


def run_house_bot(interpreter, serve_forever=True):
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    agent = Agent.load(DATA_PATH + 'models/core/' + "keras_lstm", interpreter=interpreter,
                       action_endpoint=action_endpoint)
    rasa_core.run.serve_application(agent, channel='cmdline', port=5000)
    return agent


def evaluate_model(interpreter, name=None):
    if name is None:
        name = "general"
    model_dir = DATA_PATH + 'models/core/' + name
    if not os.path.exists(DATA_PATH + "evaluation_results/Core/" + name):
        os.makedirs(DATA_PATH + "evaluation_results/Core/" + name)
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    agent = Agent.load(model_dir, interpreter=interpreter, action_endpoint=action_endpoint)
    result = run_story_evaluation(DATA_PATH + "data/stories.md",
                                  agent,
                                  out_directory=DATA_PATH + "evaluation_results/Core/" + name)
    with open(DATA_PATH + "evaluation_results/Core/" + name + "/scores.txt", 'w') as f:
        f.write(result['report'])
        del result['report']
    with open(DATA_PATH + "evaluation_results/Core/" + name + "/detail.json", 'w') as outfile:
        json.dump(result["actions"], outfile, indent=4)
        del result['actions']
    return result


def plot_metrics(metric_list, type="core", save_path=None):
    # runs through each test case and adds a set of bars to a plot.  Saves

    f, (ax1) = plt.subplots(1, 1)
    plt.grid(True)
    idx = 0
    for each in metric_list:
        bar_metrics(each, ax1, type, index=idx)
        idx += 1

    if save_path is None:
        save_path = 'img/Core/bar_' + type + '.png'

    plt.savefig(save_path, dpi=400)


def bar_metrics(metrics, ax, title, index=0):
    # adds a set of metrics bars to the axis 'ax' of the plot
    precision = metrics['precision']
    f1 = metrics['f1']
    accuracy = metrics['accuracy']
    width = 0.2
    shift = index * width
    indeces = [r + shift for r in np.arange(3)]
    metric_list = [precision, f1, accuracy]
    ax.set_title(title.replace("_", " "))
    ax.set_axisbelow(True)
    ax.bar(indeces, metric_list, width)
    ax.set_xticks([r + width / 2 for r in np.arange(3)])
    ax.set_xticklabels(('precision', 'f1', 'accuracy'))
    ax.legend(core_metric_name, loc='upper center', bbox_to_anchor=(0.5, -0.05),
              fancybox=True, shadow=True, ncol=4)
    ax.set_ylabel('score')


if __name__ == '__main__':
    core_metric_list = []
    core_metric_name = [
        "baseline",
        "Keras LSTM after tuning num of epochs",
        # "Keras LSTM after tuning RNN size"
    ]
    nlu_model_dir = "custom_nlu_config_3"
    nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/' + nlu_model_dir)
    #
    # name1 = "keras_lstm_base_line"
    # policies_1 = [
    #     MemoizationPolicy(),
    #     FormPolicy(),
    #     KerasPolicy(),
    #     FallbackPolicy()
    # ]
    #
    name2 = "keras_lstm_his_3"
    policies_2 = [
        MemoizationPolicy(max_history=3),
        FormPolicy(),
        KerasPolicy(max_history=3, epochs=200, batch_size=5, validation_split=0.1, rnn_size=64),
        FallbackPolicy(fallback_action_name="utter_unclear", core_threshold=0.3, nlu_threshold=0.3)
    ]

    name3 = "keras_lstm_his_6"
    policies_3 = [
        MemoizationPolicy(max_history=6),
        FormPolicy(),
        KerasPolicy(max_history=6, epochs=200, batch_size=5, validation_split=0.1, rnn_size=64),
        FallbackPolicy(fallback_action_name="utter_unclear", core_threshold=0.3, nlu_threshold=0.3)
    ]

    # # Keras LSTM baseline
    # model_1_dir = train_dialogue(policies_1, name=name1)
    # result_1 = evaluate_model(nlu_interpreter, name=name1)
    # core_metric_list.append(result_1)
    #
    # Keras LSTM
    model_2_dir = train_dialogue(policies_2, name=name2)
    result_2 = evaluate_model(nlu_interpreter, name=name2)
    core_metric_list.append(result_2)

    # Keras LSTM
    model_3_dir = train_dialogue(policies_3, name=name3)
    result_3 = evaluate_model(nlu_interpreter, name=name3)
    core_metric_list.append(result_3)
    #
    plot_metrics(core_metric_list, "core_keras_tuning_history")
    # run_house_bot(nlu_interpreter)
