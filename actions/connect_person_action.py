from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Tracker
from rasa_sdk.events import SlotSet, FollowupAction, Restarted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk import ActionExecutionRejection
import logging

logger = logging.getLogger(__name__)


class FormConnectToPerson(FormAction):

    def name(self):
        return "form_connect_to_person"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["person_id", "person_name"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        return {"person_name": self.from_entity(entity="person_name", intent=["talk_to_person", "person_inform"]),
                "person_id": self.from_entity(entity="person_id", intent=["talk_to_person", "person_inform"])}

    @staticmethod
    def sample_db_person():
        return {"trhgnhat": "Truong Hoang Nhat", "ititiu15086": "Nhat Truong"}

    def validate_person_id(self,
                           value: Text,
                           dispatcher: CollectingDispatcher,
                           tracker: Tracker,
                           domain: Dict[Text, Any]) -> Optional[dict]:
        person_ids = self.sample_db_person()
        value = value.replace("@", "")
        if value in person_ids:
            return_value = {"person_id": value, "person_name": person_ids[value]}
            return return_value
        else:
            dispatcher.utter_template('utter_wrong_person_id', tracker)
            # validation failed, set slot to None
            return_value = {"person_id": None}
            return return_value

    def validate_person_name(self,
                             value: Text,
                             dispatcher: CollectingDispatcher,
                             tracker: Tracker,
                             domain: Dict[Text, Any]) -> Optional[dict]:
        value = value.lower()
        for person_id, name in self.sample_db_person().items():
            if value == name.lower():
                SlotSet("person_id", person_id)
                return {"person_id": person_id, "person_name": value.title()}
        dispatcher.utter_template('utter_wrong_person_name', tracker)
        # validation failed, set slot to None
        return {"person_name": None}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        person_id = tracker.get_slot("person_id")
        person_name = tracker.get_slot("person_name")
        response = "Connecting to {person_name} ({person_id})".format(person_id=person_id, person_name=person_name)
        dispatcher.utter_message(response)
        response2 = "This is the end of users connection implementation."
        dispatcher.utter_message(response2)

        return [Restarted()]
