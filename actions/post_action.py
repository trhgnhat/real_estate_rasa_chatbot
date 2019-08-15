from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Tracker
from rasa_sdk.events import SlotSet, FollowupAction, Restarted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk import ActionExecutionRejection
import logging

logger = logging.getLogger(__name__)


class FormPostAction(FormAction):

    def name(self):
        return "form_post_action"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["post_id", "action_type"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        return {"post_id": [
            self.from_entity(entity="post_id", intent=["post_action"]),
            self.from_entity(entity="number", intent=["post_action"]),
        ],
            "action_type": self.from_entity(entity="action_type", intent=["post_action"])}

    @staticmethod
    def is_number(value):
        try:
            return int(value)
        except Exception:
            return False

    def validate_post_id(self,
                         value: Text,
                         dispatcher: CollectingDispatcher,
                         tracker: Tracker,
                         domain: Dict[Text, Any]) -> Optional[dict]:
        if self.is_number(value):
            return_value = {"post_id": tracker.get_slot("post_id").append(value)}
            return return_value
        else:
            dispatcher.utter_message('Post id must be an integer')
            return_value = {"post_id": tracker.get_slot("post_id")}
            return return_value

    @staticmethod
    def db_actions():
        return ["activate", "deactivate", "delete", "create", "edit"]

    def validate_action_type(self,
                             value: Text,
                             dispatcher: CollectingDispatcher,
                             tracker: Tracker,
                             domain: Dict[Text, Any]) -> Optional[dict]:
        if value in self.db_actions():
            return_value = {"action_type": value}
            return return_value
        else:
            dispatcher.utter_message('Available actions: delete, create, edit, activate, deactivate')
            return_value = {"post_id": None}
            return return_value

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        post_id = tracker.get_slot("post_id")
        action_type = tracker.get_slot("action_type")
        response = "Perform action `{action_type} with posts: {post_id}`".format(post_id=post_id,
                                                                                 action_type=action_type)
        dispatcher.utter_message(response)
        response2 = "Need to be integrated into system to perform action. \
                    This is the end of users connection implementation."
        dispatcher.utter_message(response2)

        return [Restarted()]
