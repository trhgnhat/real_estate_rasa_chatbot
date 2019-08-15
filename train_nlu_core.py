import logging
from rasa_core.agent import Agent
from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.form_policy import FormPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.tracker_store import RedisTrackerStore
import os

logger = logging.getLogger(__name__)

DATA_PATH = os.getcwd() + "/"


def train_nlu(data_path, configs, model_dir):
    training_data = load_data(data_path + "data.md")
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)
    fixed_model_name = "official"
    # save model
    model_directory = trainer.persist(model_dir, fixed_model_name=fixed_model_name)
    print("FINISH NLU TRAINING PROCESS")
    return model_directory


def train_dialogue(policies,
                   model_path='models/core/',
                   name="official",
                   domain_file='domain.yml',
                   training_data_file='data/stories.md'):
    agent = Agent(DATA_PATH + domain_file, policies=policies)
    data = agent.load_data(DATA_PATH + training_data_file)
    agent.train(data)
    agent.persist(DATA_PATH + model_path + name)
    print("FINISH CORE TRAINING PROCESS")


config_dir = DATA_PATH + "/configs/nlu_configs/custom_nlu_config_3/nlu_config.md"
train_nlu(data_path=DATA_PATH + 'data/', configs=config_dir, model_dir=DATA_PATH + 'models/nlu')

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/official')

policies_3 = [
    MemoizationPolicy(max_history=2),
    FormPolicy(),
    KerasPolicy(max_history=2, epochs=200, batch_size=16, validation_split=0.1, rnn_size=64),
    FallbackPolicy(fallback_action_name="utter_unclear", core_threshold=0.3, nlu_threshold=0.3)
]
train_dialogue(policies_3)
