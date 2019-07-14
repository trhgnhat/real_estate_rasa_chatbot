import logging
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.channels.slack import SlackInput
from rasa_core.tracker_store import MongoTrackerStore
from rasa_core.domain import TemplateDomain
from utils.constant import *
logger = logging.getLogger(__name__)


def run_house_bot():
    nlu_interpreter = RasaNLUInterpreter(NLU_DATA_PATH)
    action_endpoint = EndpointConfig(url=ACTION_ENDPOINT)
    domain = TemplateDomain.load(TRACKER_DOMAIN_DATA_PATH)
    db = MongoTrackerStore(
        domain,
        host=DB_HOST,
        db=DB_NAME,
        collection=DB_COLLECTION
    )
    agent = Agent.load(CORE_DATA_PATH,
                       interpreter=nlu_interpreter,
                       action_endpoint=action_endpoint,
                       tracker_store=db)

    input_channel = SlackInput(
        slack_token=SLACK_BOT_API_TOKEN,
        slack_channel=""
    )

    run = agent.handle_channels([input_channel], http_port=APP_PORT, serve_forever=True)


run_house_bot()
