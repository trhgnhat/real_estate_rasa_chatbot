import logging
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import AugmentedMemoizationPolicy
from rasa_core.policies.form_policy import FormPolicy
from rasa_core.policies.embedding_policy import EmbeddingPolicy
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.train import interactive
from rasa_core.utils import EndpointConfig

logger = logging.getLogger(__name__)


def run_house_agent(interpreter,
                    domain_file="house_domain.yml",
                    training_data_file='data/stories_form.md'):
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")

    agent = Agent(domain_file,
                  policies=[
                      AugmentedMemoizationPolicy(max_history=6),
                      FormPolicy(),
                      KerasPolicy(max_history=6, epochs=200, batch_size=5, validation_split=0.1),
                      FallbackPolicy(fallback_action_name="utter_unclear", core_threshold=0.3, nlu_threshold=0.3)],
                  interpreter=interpreter, action_endpoint=action_endpoint)

    data = agent.load_data(training_data_file)
    agent.train(data)
    agent.persist("./models/dialogue")
    interactive.run_interactive_learning(agent, training_data_file)
    return agent


if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    model_dir = "custom_nlu_config_2"
    nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/' + model_dir)
    run_house_agent(nlu_interpreter)
