## Generated Story 3490283781720101690 (example from interactive learning, "form: " will be excluded from training)
* greet
    - utter_greet
* house_request
    - house_form
    - form{"name": "house_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "nhatrang"}
    - slot{"location": "nhatrang"}
    - form: house_form
    - slot{"location": "nhatrang"}
    - slot{"requested_slot": "price"}
* form: inform{"number": "2000$"}
    - form: house_form
    - slot{"price": "2000$"}
* form: inform
    - form: house_form
    - slot{"requested_slot": "feedback"}
* form: inform{"feedback": "great"}
    - slot{"feedback": "great"}
    - form: house_form
    - slot{"feedback": "great"}
    - slot{"requested_slot": null}
    - utter_slots_values

## Generated Story 336012439966948292
* greet
    - utter_greet
* house_request
    - house_form
    - form{"name": "house_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "nhatrang"}
    - form: house_form
    - slot{"location": "nhatrang"}
    - slot{"requested_slot": "price"}
* form: inform{"price": "2000$"}
    - form: house_form
    - slot{"price": null}
    - slot{"requested_slot": "price"}
* form: inform{"price": "2000 dollar"}
    - form: house_form
    - slot{"price": null}
    - slot{"requested_slot": "price"}
* form: inform{"price": "2000"}
    - form: house_form
    - slot{"price": "2000"}
    - slot{"requested_slot": "feedback"}
* form: inform{"feedback": "look like you are very smart"}
    - form: house_form
    - form: house_form
    - slot{"requested_slot": "feedback"}
* form: inform
    - form: house_form
    - slot{"feedback": "you are smart"}
    - slot{"location": "nhatrang"}
    - slot{"price": "2000"}
    - slot{"feedback": "you are smart"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slots_values
* thanking
    - utter_noworries

