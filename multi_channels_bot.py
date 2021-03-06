import logging
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.channels.slack import SlackInput
from rasa_core.channels import RestInput
from rasa_core.tracker_store import MongoTrackerStore
from rasa_core.domain import TemplateDomain
from rasa_core import server
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
        collection=DB_COLLECTION,
        username=DB_USERNAME,
        password=DB_PASSWORD,
        auth_source="admin"
    )
    agent = Agent.load(CORE_DATA_PATH,
                       interpreter=nlu_interpreter,
                       action_endpoint=action_endpoint,
                       tracker_store=db)

    input_channel = SlackInput(
        slack_token=SLACK_BOT_API_TOKEN,
        slack_channel=""
    )

    server.create_app(
        agent.handle_channels([input_channel, RestInput()], http_port=APP_PORT, serve_forever=True),
        cors_origins="*")


run_house_bot()
