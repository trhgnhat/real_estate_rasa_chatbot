from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


class ActionHouse(Action):
    def name(self):
        return 'action_house'

    @staticmethod
    def required_slots(tracker):
        """A list of required slots that the form has to fill"""

        return ["location", "price"]

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        price = tracker.get_slot('price')

        num_houses = 4

        response = """there is {} houses on the {} with the money of {}""".format(num_houses, loc, price)

        dispatcher.utter_message(response)
        return [SlotSet('location', loc), SlotSet('price', price)]
