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
        return ["city", "price", "feedback", "real_estate_type"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"city": self.from_entity(entity="city",
                                         intent=["house_inform",
                                                 "house_request"]),
                "real_estate_type": self.from_entity(entity="real_estate_type",
                                                     intent=["house_inform",
                                                             "house_request"]),
                "time_spent": self.from_entity(entity="time_spent",
                                               intent=["house_inform",
                                                       "house_request"]),
                "guess_room": self.from_entity(entity="guess_room",
                                               intent=["house_inform",
                                                       "house_request"]),
                "transportation": self.from_entity(entity="transportation",
                                                   intent=["house_inform",
                                                           "house_request"]),
                "bath_room": self.from_entity(entity="bath_room",
                                              intent=["house_inform",
                                                      "house_request"]),
                "bed_room": self.from_entity(entity="bed_room",
                                             intent=["house_inform",
                                                     "house_request"]),
                "location": self.from_entity(entity="location",
                                             intent=["house_inform",
                                                     "house_request"]),
                "local_feature": self.from_entity(entity="local_feature",
                                                  intent=["house_inform",
                                                  "house_request"]),
                "house_feature": self.from_entity(entity="house_feature",
                                                  intent=["house_inform",
                                                          "house_request"]),
                "feedback": [self.from_entity(entity="feedback"),
                             self.from_text()]}

    @staticmethod
    def city_db():
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

    def validate_city(self,
                      value: Text,
                      dispatcher: CollectingDispatcher,
                      tracker: Tracker,
                      domain: Dict[Text, Any]) -> Optional[Text]:
        """Validate city value."""

        if value.lower() in self.city_db():
            # validation succeeded
            return value
        else:
            dispatcher.utter_template('utter_wrong_city', tracker)
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
