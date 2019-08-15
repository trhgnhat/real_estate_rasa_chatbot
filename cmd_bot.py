from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.run import serve_application
from rasa_core.tracker_store import MongoTrackerStore
from rasa_core.domain import TemplateDomain
from utils.constant import *
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level="DEBUG")
logger.info("LOG")

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
    serve_application(agent, channel='rest', port=6000, cors="*", enable_api=True)
    return agent


run_house_bot()
