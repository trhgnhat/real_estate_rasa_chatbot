import logging
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import AugmentedMemoizationPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.form_policy import FormPolicy
from rasa_core.policies.embedding_policy import EmbeddingPolicy
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.train import interactive
from rasa_core.utils import EndpointConfig

import os

logger = logging.getLogger(__name__)

DATA_PATH = os.getcwd() + "/"


def run_house_agent(interpreter,
                    domain_file="domain.yml",
                    training_data_file='data/stories.md'):
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")

    agent = Agent.load(DATA_PATH + "models/core/official", interpreter=interpreter, action_endpoint=action_endpoint)

    interactive.run_interactive_learning(agent, training_data_file, skip_visualization=True)
    return agent


if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    model_dir = "official"
    nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/' + model_dir)
    run_house_agent(nlu_interpreter)
