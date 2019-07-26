# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Tracker
from rasa_sdk.events import SlotSet, FollowupAction, ReminderScheduled
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk import Action


class FormHouse(FormAction):
    """Example of a custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""
        return "form_house_request"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        if tracker.get_slot('real_estate_type') == "house":
            return ["real_estate_type", "city", "price", "currency", "bed_room", "bath_room", "guess_room"]
        else:
            return ["real_estate_type", "city", "price", "currency", "bed_room", "bath_room"]
            # return ["real_estate_type", "city", "price", "currency", "bed_room", "bath_room", "guess_room", "request_more_info", "is_satisfied"]

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
                "price": [self.from_entity(entity="amount-of-money",
                                           intent=["house_inform",
                                                   "house_request",
                                                   "number"])
                          ],
                "currency": self.from_entity(entity="currency",
                                             intent=["house_inform",
                                                     "house_request"]),
                "time_spent": self.from_entity(entity="time_spent",
                                               intent=["house_inform",
                                                       "house_request"]),
                "guess_room": [self.from_entity(entity="guess_room",
                                                intent=["house_inform",
                                                        "house_request",
                                                        "number"]),
                               self.from_entity(entity="number",
                                                intent=["house_inform",
                                                        "house_request",
                                                        "number"])
                               ],
                "transportation": self.from_entity(entity="transportation",
                                                   intent=["house_inform",
                                                           "house_request"]),
                "bath_room": [self.from_entity(entity="bath_room",
                                               intent=["house_inform",
                                                       "house_request",
                                                       "number"]),
                              self.from_entity(entity="number",
                                               intent=["house_inform",
                                                       "house_request",
                                                       "number"])
                              ],
                "bed_room": [self.from_entity(entity="bed_room",
                                              intent=["house_inform",
                                                      "house_request",
                                                      "number"]),
                             self.from_entity(entity="number",
                                              intent=["house_inform",
                                                      "house_request",
                                                      "number"])
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
                             self.from_text(intent="feedback")]}

    @staticmethod
    def return_information(tracker: Tracker) -> Optional[Text]:
        try:
            response = """information (collecting from form_house_request):\n"""
            for entity_name, entity in tracker.current_slot_values().items():
                if tracker.get_slot(entity_name) is not None:
                    response += "- {}: {}\n".format(entity_name, entity)
            return response
        except Exception as e:
            print(e)
            print(tracker.current_slot_values().items())

    @staticmethod
    def re_type_db():
        # type: () -> List[Text]
        """Database of supported cuisines"""
        return ["house", "home", "apartment", "flat"]

    @staticmethod
    def currency_db():
        # type: () -> List[Text]
        """Database of supported cuisines"""
        return ["vnd", "usd", "euro"]

    @staticmethod
    def city_remove(value):
        """Database of supported cuisines"""
        value = value.replace("city", "").strip()
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
        value = value.lower()
        value = self.city_remove(value)
        if value:
            # validation succeeded
            return {"city": value}
        else:
            dispatcher.utter_template('utter_wrong_city', tracker)
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"city": None}

    def validate_real_estate_type(self,
                                  value: Text,
                                  dispatcher: CollectingDispatcher,
                                  tracker: Tracker,
                                  domain: Dict[Text, Any]) -> Optional[Text]:
        if value.lower() in self.re_type_db():
            # validation succeeded
            return {"real_estate_type": value}
        else:
            dispatcher.utter_template('utter_wrong_real_estate_type', tracker)
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"real_estate_type": None}

    def validate_currency(self,
                          value: Text,
                          dispatcher: CollectingDispatcher,
                          tracker: Tracker,
                          domain: Dict[Text, Any]) -> Optional[Text]:
        if value.lower() in self.currency_db():
            # validation succeeded
            return {"currency": value}
        else:
            dispatcher.utter_template('utter_wrong_currency', tracker)
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"currency": None}

    def validate_price(self,
                       value: Text,
                       dispatcher: CollectingDispatcher,
                       tracker: Tracker,
                       domain: Dict[Text, Any]) -> Optional[Text]:
        word_rm_dict = {
            "k": "000",
            "thousand": "000",
            "thousands": "000",
            "millions": "000000",
            "million": "000000",
            "mil": "000000",
            "M": "000000",
            "billions": "000000000",
            "bil": "000000000",
            "B": "000000000",
            "billion": "000000000",
        }
        import re
        regex = "(?i)(" + "|".join([each for each in word_rm_dict]) + ")"
        for match in re.findall(regex, value):
            if match in word_rm_dict:
                value = value.replace(match, word_rm_dict[match])
        value = value.replace(" ", "").replace(".", "").replace(",", "")
        if self.is_float(value) and float(value) > 0:
            return {"price": value}
        else:
            dispatcher.utter_template('utter_wrong_price', tracker)
            # validation failed, set slot to None
            return {"price": None}

    def validate_bed_room(self,
                          value: Text,
                          dispatcher: CollectingDispatcher,
                          tracker: Tracker,
                          domain: Dict[Text, Any]) -> Optional[Text]:

        if self.is_int(value) and int(value) > 0:
            return {"bed_room": value}
        else:
            dispatcher.utter_template('utter_unclear', tracker)
            # validation failed, set slot to None
            return {"bed_room": None}


    def validate_bath_room(self,
                           value: Text,
                           dispatcher: CollectingDispatcher,
                           tracker: Tracker,
                           domain: Dict[Text, Any]) -> Optional[Text]:

        if self.is_int(value) and int(value) > 0:
            return {"bath_room": value}
        else:
            dispatcher.utter_template('utter_unclear', tracker)
            # validation failed, set slot to None
            return {"bath_room": None}

    def validate_guess_room(self,
                            value: Text,
                            dispatcher: CollectingDispatcher,
                            tracker: Tracker,
                            domain: Dict[Text, Any]) -> Optional[Text]:

        if self.is_int(value) and int(value) > 0:
            return {"guess_room": value}
        else:
            dispatcher.utter_template('utter_unclear', tracker)
            # validation failed, set slot to None
            return {"guess_room": None}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        return [SlotSet("matches", None), FollowupAction("action_post_house_info")]


class ActionHouse(Action):
    def name(self):
        return 'action_house'

    def run(self, dispatcher, tracker, domain):
        try:
            if tracker.get_slot("matches") is not None:
                list_houses = tracker.get_slot("matches")
            else:
                list_houses = ["house 1", "house 2", "house 3", "house 4"]
            response = "Link: {}".format(list_houses[0])
            list_houses.append(list_houses[0])
            list_houses.pop(0)
            dispatcher.utter_message(response)
            return [SlotSet("matches", list_houses)]
        except Exception as e:
            print(e)
            print(tracker.current_slot_values().items())


class ActionPostHouseInfo(Action):
    def name(self):
        return 'action_post_house_info'

    def run(self, dispatcher, tracker, domain):
        try:
            response = """information (processing in action):\n"""
            for entity_name, entity in tracker.current_slot_values().items():
                if entity_name in ["request_more_info", "is_satisfied", "confirm_information"]:
                    continue
                if tracker.get_slot(entity_name) is not None:
                    response += "- {}: {}\n".format(entity_name, entity)
            dispatcher.utter_message(response)
            dispatcher.utter_template("utter_ask_confirm_information", tracker)
        except Exception as e:
            print(e)
            print(tracker.current_slot_values().items())


