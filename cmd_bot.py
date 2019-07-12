import rasa_core
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.run import serve_application
import os
from rasa_core.tracker_store import MongoTrackerStore
from rasa_core.domain import TemplateDomain

DATA_PATH = os.getcwd() + "/"

username = "realestate_bot"
pw = "n4hveYoloO9OB8lt"
mongoDB = "mongodb+srv://{username}:{password}@nhathoangtruong-r4udi.mongodb.net/test?retryWrites=true&w=majority".format(
    username=username, password=pw)


def run_house_bot():
    nlu_model_dir = "custom_nlu_config_3"
    nlu_interpreter = RasaNLUInterpreter(DATA_PATH + 'models/nlu/default/official')
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    domain = TemplateDomain.load(DATA_PATH + "tracker_store.yml")
    db = MongoTrackerStore(
        domain,
        host="localhost",
        db="real-estate-bot",
        collection="conversation-tracking",
    )
    agent = Agent.load(DATA_PATH + "models/core/official",
                       interpreter=nlu_interpreter,
                       action_endpoint=action_endpoint,
                       tracker_store=db)
    rasa_core.run.serve_application(agent, channel='cmdline', port=5000)
    return agent


run_house_bot()
