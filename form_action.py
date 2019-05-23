# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union, Optional

from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT


class RestaurantForm(FormAction):
    """Example of a custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "house_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["location", "price", "feedback"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"location": self.from_entity(entity="location",
                                             intent=["inform",
                                                     "house_request"]),
                "price": self.from_entity(entity="price",
                                          intent=["inform",
                                                  "house_request"]),
                # "outdoor_seating": [self.from_entity(entity="seating"),
                #                     self.from_intent(intent='affirm',
                #                                      value=True),
                #                     self.from_intent(intent='deny',
                #                                      value=False)],
                # "preferences": [self.from_intent(intent='deny',
                #                                  value="no additional "
                #                                        "preferences"),
                #                 self.from_text(not_intent="affirm")],
                "feedback": [self.from_entity(entity="feedback"),
                             self.from_text()]}

    @staticmethod
    def location_db():
        # type: () -> List[Text]
        """Database of supported cuisines"""
        return ["hanoi",
                "danang",
                "nhatrang",
                "hochiminh",
                "quynhon",
                "vinh"]

    @staticmethod
    def is_float(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            float(string)
            return True
        except ValueError:
            return False

    def validate_location(self,
                          value: Text,
                          dispatcher: CollectingDispatcher,
                          tracker: Tracker,
                          domain: Dict[Text, Any]) -> Optional[Text]:
        """Validate cuisine value."""

        if value.lower() in self.location_db():
            # validation succeeded
            return value
        else:
            dispatcher.utter_template('utter_wrong_location', tracker)
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return None

    def validate_price(self,
                       value: Text,
                       dispatcher: CollectingDispatcher,
                       tracker: Tracker,
                       domain: Dict[Text, Any]) -> Optional[Text]:
        """Validate num_people value."""

        if self.is_float(value) and int(value) > 0:
            return value
        else:
            dispatcher.utter_template('utter_wrong_price', tracker)
            # validation failed, set slot to None
            return None

    # @staticmethod
    # def validate_outdoor_seating(value: Text,
    #                              dispatcher: CollectingDispatcher,
    #                              tracker: Tracker,
    #                              domain: Dict[Text, Any]) -> Any:
    #     """Validate outdoor_seating value."""
    #
    #     if isinstance(value, str):
    #         if 'out' in value:
    #             # convert "out..." to True
    #             return True
    #         elif 'in' in value:
    #             # convert "in..." to False
    #             return False
    #         else:
    #             dispatcher.utter_template('utter_wrong_outdoor_seating',
    #                                       tracker)
    #             # validation failed, set slot to None
    #             return None
    #
    #     else:
    #         # affirm/deny was picked up as T/F
    #         return value

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        location = tracker.get_slot("location")
        price = tracker.get_slot("price")
        feedback = tracker.get_slot("feedback")

        response = "there are N houses in {} with the price about {}. Thank you for your feed back '{}'".format(
            location, price, feedback)

        dispatcher.utter_message(response)

        dispatcher.utter_template('utter_submit', tracker)
        return [SlotSet('location', location), SlotSet('price', price), SlotSet('feedback', feedback)]
