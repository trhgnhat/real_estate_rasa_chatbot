import logging
import rasa_core
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.channels.slack import SlackInput
from rasa_core.tracker_store import MongoTrackerStore
from rasa_core.domain import TemplateDomain
import os

logger = logging.getLogger(__name__)

DATA_PATH = os.getcwd() + "/"


def run_house_bot():
    nlu_interpreter = RasaNLUInterpreter(DATA_PATH + 'models/nlu/default/official')
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    db = MongoTrackerStore(
        TemplateDomain.load(DATA_PATH + "tracker_store.yml").compare_with_specification(DATA_PATH),
        host="localhost",
        db="real-estate-bot",
        collection="conversation-tracking",
    )
    agent = Agent.load(DATA_PATH + "models/core/official",
                       interpreter=nlu_interpreter,
                       action_endpoint=action_endpoint,
                       tracker_store=db)

    bot_oauth_token = ""  # is slack_token
    input_channel = SlackInput(
        slack_token=bot_oauth_token,
        slack_channel=""
    )

    run = agent.handle_channels([input_channel], 5000, serve_forever=True)


run_house_bot()
