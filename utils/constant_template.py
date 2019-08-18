import os

DB_HOST = "localhost"
DB_NAME = ""
DB_COLLECTION = ""  # For mongoDB only
DB_USERNAME = ""
DB_PASSWORD = ""

DATA_PATH = os.getcwd() + "/"
NLU_DATA_PATH = DATA_PATH + 'models/nlu/default/official'
CORE_DATA_PATH = DATA_PATH + "models/core/official"
TRACKER_DOMAIN_DATA_PATH = DATA_PATH + "tracker_store.yml"
ACTION_ENDPOINT = "http://action-service:5055/webhook"
APP_PORT = 5000

SLACK_BOT_API_TOKEN = "xoxb-..."
