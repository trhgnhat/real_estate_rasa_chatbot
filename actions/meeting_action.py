from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Tracker
from rasa_sdk.events import SlotSet, FollowupAction, ReminderScheduled
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk import Action


class FormSetupMeeting(FormAction):

    def name(self):
        return "form_setup_meeting"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["person_id", "person_name", "time"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        return {"person_name": self.from_entity(entity="person_name",
                                                intent=["talk_to_person", "set_appointment", "person_inform"]),
                "person_id": self.from_entity(entity="person_id",
                                              intent=["talk_to_person", "set_appointment", "person_inform"]),
                "time": self.from_entity(entity="time", intent=["set_appointment"])}

    def validate_time(self,
                      value: Text,
                      dispatcher: CollectingDispatcher,
                      tracker: Tracker,
                      domain: Dict[Text, Any]) -> Optional[dict]:
        from dateutil.parser import parse
        from dateutil.relativedelta import relativedelta
        import datetime
        dt_obj = parse(value)
        dt_obj = dt_obj.date() + relativedelta(hours=dt_obj.hour, minutes=dt_obj.minute, second=dt_obj.second)

        # meeting date is only valid if it happens after current time.
        if dt_obj > datetime.datetime.now():
            return {"time": value}
        else:
            dispatcher.utter_template('utter_wrong_meeting_time', tracker)
            return {"time": None}

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
            return_value = {"person_id": None, "person_name": None}
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
        return_value = {"person_id": None, "person_name": None}
        return return_value

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        person_id = tracker.get_slot("person_id")
        person_name = tracker.get_slot("person_name")
        time = tracker.get_slot("time")
        from dateutil.parser import parse
        from dateutil.relativedelta import relativedelta
        dt_obj = parse(time)
        dt_obj = dt_obj.date() + relativedelta(hours=dt_obj.hour, minutes=dt_obj.minute, second=dt_obj.second)
        remind_dt_obj = dt_obj + relativedelta(minutes=-5)  # 5 minutes before
        # dt_obj.date().ctime() Mon Jul 15 00:00:00 2019
        # dt_obj.ctime() Mon Jul 15 10:00:00 2019
        # dt_obj.time() 10:00:00
        # dt_obj.timetz() 10:00:00+07:00
        # new_dt_obj.isoformat() 2019-07-15T09:55:00
        response = "I have setup the meeting for you and {person_name} ({person_id}) at {time}".format(
            person_id=person_id, person_name=person_name, time=dt_obj.ctime())
        dispatcher.utter_message(response)
        response2 = "This is the end of meeting setup implementation."
        dispatcher.utter_message(response2)

        return [ReminderScheduled("action_remind_meeting", trigger_date_time=remind_dt_obj,
                                  kill_on_user_message=False)]


class ActionRemindMeeting(Action):
    def name(self):
        return 'action_remind_meeting'

    def run(self, dispatcher, tracker, domain):
        person_id = tracker.get_slot("person_id")
        person_name = tracker.get_slot("person_name")
        response = "you will have a meeting with {person_name} ({person_id}) in 5 minutes. Please prepare!".format(
            person_id=person_id, person_name=person_name)
        dispatcher.utter_message(response)
        response2 = "This is the end of meeting setup implementation."
        dispatcher.utter_message(response2)
        return []
