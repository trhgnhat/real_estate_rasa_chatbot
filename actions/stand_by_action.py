from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Tracker
from rasa_sdk.events import SlotSet, FollowupAction, ReminderScheduled
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk import Action


class ActionWaitForCommand(Action):
    def name(self):
        return 'action_wait_for_command'

    def run(self, dispatcher, tracker, domain):
        return []
