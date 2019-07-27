import os

DB_HOST = "localhost"
DB_NAME = "real-estate-bot"
DB_COLLECTION = "conversation-tracking"  # For mongoDB only
DB_USERNAME = ""
DB_PASSWORD = ""

DATA_PATH = os.getcwd() + "/"
NLU_DATA_PATH = DATA_PATH + 'models/nlu/default/official'
CORE_DATA_PATH = DATA_PATH + "models/core/official"
TRACKER_DOMAIN_DATA_PATH = DATA_PATH + "tracker_store.yml"
ACTION_ENDPOINT = "http://localhost:5055/webhook"
APP_PORT = 5000

SLACK_BOT_API_TOKEN = ""
