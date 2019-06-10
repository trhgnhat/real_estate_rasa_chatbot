## Generated Story 1484301423811423976
* house_inform{"real_estate_type": "house", "city": "hanoi", "price": "2 billions", "currency": "usd", "bed_room": "2"}
    - slot{"bed_room": "2"}
    - slot{"city": "hanoi"}
    - slot{"currency": "usd"}
    - slot{"price": "2 billions"}
    - slot{"real_estate_type": "house"}
    - house_form
    - form{"name": "house_form"}
    - slot{"real_estate_type": "house"}
    - slot{"city": "hanoi"}
    - slot{"price": "2 billions"}
    - slot{"currency": "usd"}
    - slot{"bed_room": "2"}
    - slot{"requested_slot": "bath_room"}
* form: house_inform{"number": "2"}
    - form: house_form
    - slot{"bath_room": "2"}
    - slot{"requested_slot": "guess_room"}
* form: house_inform{"number": "1"}
    - form: house_form
    - slot{"guess_room": "1"}
    - slot{"requested_slot": "null"}
    - utter_ask_request_more_info
* form: affirm
    - utter_please_to_hear
* form: house_inform{"house_description": "comfortable", "real_estate_type": "house"}
    - form: house_form
    - slot{"house_description": "comfortable"}
    - slot{"real_estate_type": "house"}
    - utter_understand
    - utter_ask_request_more_info
* form: house_inform{"num_persons": "4"}
    - form: house_form
    - slot{"num_persons": "4"}
    - utter_understand
    - utter_ask_request_more_info
* form: deny
    - utter_understand
    - action_deactivate_form
    - form{"name": null}
    - action_house
    - slot{"found": "Not implement yet"}
    - utter_ask_satisfaction
* affirm
    - utter_ask_feedback
* feedback
    - utter_thanks_for_feedback
    - utter_call_if_need_help
* affirm