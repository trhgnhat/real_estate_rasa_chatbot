from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Tracker
from rasa_sdk.events import SlotSet, FollowupAction, Restarted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk import ActionExecutionRejection
import logging

logger = logging.getLogger(__name__)


class FormVisualizationAction(FormAction):

    def name(self):
        return "form_visualization_action"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return []

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        return {"visual_type": self.from_entity(entity="visual_type", intent=["show_dashboard"])}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        visual_type = tracker.get_slot("visual_type")
        if visual_type:
            response = "Display {visual_type} in dashboard page".format(visual_type=visual_type)
        else:
            response = "Display the dashboard site"
        dispatcher.utter_message(response)
        response2 = "Need to be integrated into system to perform action. \
                    This is the end of users connection implementation."
        dispatcher.utter_message(response2)

        return [Restarted()]
