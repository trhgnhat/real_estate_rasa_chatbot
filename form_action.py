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
        return ["real_estate_type", "city", "price", "currency", "bed_room", "bath_room", "guess_room", "feedback"]

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
                "price": [self.from_entity(entity="price",
                                           intent=["house_inform",
                                                   "house_request"]),
                          self.from_entity(entity="number",
                                           intent=["house_inform",
                                                   "house_request"])
                          ],
                "currency": self.from_entity(entity="currency",
                                             intent=["house_inform",
                                                     "house_request"]),
                "time_spent": self.from_entity(entity="time_spent",
                                               intent=["house_inform",
                                                       "house_request"]),
                "guess_room": [self.from_entity(entity="guess_room",
                                                intent=["house_inform",
                                                        "house_request"]),
                               self.from_entity(entity="number",
                                                intent=["house_inform",
                                                        "house_request"])
                               ],
                "transportation": self.from_entity(entity="transportation",
                                                   intent=["house_inform",
                                                           "house_request"]),
                "bath_room": [self.from_entity(entity="bath_room",
                                               intent=["house_inform",
                                                       "house_request"]),
                              self.from_entity(entity="number",
                                               intent=["house_inform",
                                                       "house_request"])
                              ],
                "bed_room": [self.from_entity(entity="bed_room",
                                              intent=["house_inform",
                                                      "house_request"]),
                             self.from_entity(entity="number",
                                              intent=["house_inform",
                                                      "house_request"])
                             ],
                "location": self.from_entity(entity="location",
                                             intent=["house_inform",
                                                     "house_request"]),
                "local_feature": self.from_entity(entity="local_feature",
                                                  intent=["house_inform",
                                                          "house_request"]),
                "house_feature": self.from_entity(entity="house_feature",
                                                  intent=["house_inform",
                                                          "house_request"]),
                "house_description": self.from_entity(entity="house_description",
                                                      intent=["house_inform",
                                                              "house_request"]),
                "feedback": [self.from_entity(entity="feedback"),
                             self.from_text()]}

    @staticmethod
    def re_type_db():
        # type: () -> List[Text]
        """Database of supported cuisines"""
        return ["house", "apartment"]

    @staticmethod
    def currency_db():
        # type: () -> List[Text]
        """Database of supported cuisines"""
        return ["vnd", "usd", "euro"]

    @staticmethod
    def city_remove(value):
        """Database of supported cuisines"""
        value = value.replace("city", "")
        return value

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False

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
        value.lower()
        value = self.city_remove(value)
        if value:
            # validation succeeded
            return value
        else:
            dispatcher.utter_template('utter_wrong_city', tracker)
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return None

    def real_estate_type(self,
                         value: Text,
                         dispatcher: CollectingDispatcher,
                         tracker: Tracker,
                         domain: Dict[Text, Any]) -> Optional[Text]:
        if value[-1] == "s":
            value = value[:-1]
        if value.lower() in self.re_type_db():
            # validation succeeded
            return value
        else:
            dispatcher.utter_template('utter_wrong_real_estate_type', tracker)
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return None

    def real_estate_type(self,
                         value: Text,
                         dispatcher: CollectingDispatcher,
                         tracker: Tracker,
                         domain: Dict[Text, Any]) -> Optional[Text]:
        if value.lower() in self.currency_db():
            # validation succeeded
            return value
        else:
            dispatcher.utter_template('utter_wrong_currency', tracker)
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return None

    def validate_price(self,
                       value: Text,
                       dispatcher: CollectingDispatcher,
                       tracker: Tracker,
                       domain: Dict[Text, Any]) -> Optional[Text]:

        if self.is_float(value) and float(value) > 0:
            return value
        else:
            dispatcher.utter_template('utter_wrong_price', tracker)
            # validation failed, set slot to None
            return None

    def validate_bed_room(self,
                          value: Text,
                          dispatcher: CollectingDispatcher,
                          tracker: Tracker,
                          domain: Dict[Text, Any]) -> Optional[Text]:

        if self.is_int(value) and int(value) > 0:
            return value
        else:
            dispatcher.utter_template('utter_unclear', tracker)
            # validation failed, set slot to None
            return None

    def validate_bath_room(self,
                           value: Text,
                           dispatcher: CollectingDispatcher,
                           tracker: Tracker,
                           domain: Dict[Text, Any]) -> Optional[Text]:

        if self.is_int(value) and int(value) > 0:
            return value
        else:
            dispatcher.utter_template('utter_unclear', tracker)
            # validation failed, set slot to None
            return None

    def validate_guess_room(self,
                            value: Text,
                            dispatcher: CollectingDispatcher,
                            tracker: Tracker,
                            domain: Dict[Text, Any]) -> Optional[Text]:

        if self.is_int(value) and int(value) > 0:
            return value
        else:
            dispatcher.utter_template('utter_unclear', tracker)
            # validation failed, set slot to None
            return None

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        location = tracker.get_slot("location")
        price = tracker.get_slot("price")
        feedback = tracker.get_slot("feedback")
        bed_room = tracker.get_slot("bed_room")
        bath_room = tracker.get_slot("bath_room")
        guess_room = tracker.get_slot("guess_room")

        dispatcher.utter_template('utter_ask_for_more_info', tracker)

        return [SlotSet('location', location), SlotSet('price', price), SlotSet('feedback', feedback),
                SlotSet('bed_room', bed_room), SlotSet('bath_room', bath_room), SlotSet('guess_room', guess_room)]
