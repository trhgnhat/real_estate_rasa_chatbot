import logging
import rasa_core
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.form_policy import FormPolicy
from rasa_core.policies.embedding_policy import EmbeddingPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.run import serve_application
from rasa_core import config

logger = logging.getLogger(__name__)

DATA_PATH = "D:/workspace/Pet Project/Rasa NLP NLU/House/"


def train_dialogue(domain_file='house_domain.yml',
                   model_path='models/dialogue',
                   training_data_file='data/stories.md'):
    # this will catch predictions the model isn't very certain about
    # there is a threshold for the NLU predictions as well as the action predictions
    fallback = FallbackPolicy(fallback_action_name="utter_unclear", core_threshold=0.2, nlu_threshold=0.1)
    agent = Agent(DATA_PATH + domain_file,
                  policies=[MemoizationPolicy(), FormPolicy(), KerasPolicy(max_history=5, epochs=200, batch_size=50),
                            fallback])
    data = agent.load_data(DATA_PATH + training_data_file)

    agent.train(data)

    agent.persist(DATA_PATH + model_path)
    return agent


def run_house_bot(serve_forever=True):
    interpreter = RasaNLUInterpreter(DATA_PATH + 'models/nlu/default/real_estate_nlu')
    action_endpoint = EndpointConfig(url="http://localhost:4000/webhook")
    agent = Agent.load(DATA_PATH + 'models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)
    rasa_core.run.serve_application(agent, channel='cmdline', port=4005)

    return agent


if __name__ == '__main__':
    train_dialogue()
    run_house_bot()
