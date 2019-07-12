
## Generated Story 3368241047826805535
* greet
    - utter_greet
* house_request{"real_estate_type": "house", "city": "hanoi"}
    - slot{"city": "hanoi"}
    - slot{"real_estate_type": "house"}
    - house_form
    - form{"name": "house_form"}
    - slot{"real_estate_type": "house"}
    - slot{"city": "hanoi"}
    - slot{"requested_slot": "price"}
* form: house_inform{"price": "1 billions", "currency": "usd"}
    - slot{"currency": "usd"}
    - slot{"price": "1 billions"}
    - form: house_form
    - slot{"currency": "usd"}
    - slot{"price": null}
    - slot{"requested_slot": "price"}
* form: house_inform{"price": "1 billion", "currency": "usd"}
    - slot{"currency": "usd"}
    - slot{"price": "1 billion"}
    - form: house_form
    - slot{"currency": "usd"}
    - slot{"price": null}
    - slot{"requested_slot": "price"}
* form: house_inform{"price": "1 million", "currency": "usd"}
    - slot{"currency": "usd"}
    - slot{"price": "1 million"}
    - form: house_form
    - slot{"currency": "usd"}
    - slot{"price": "1000000"}
    - slot{"requested_slot": "bed_room"}
* form: number{"number": "1"}
    - form: house_form
    - slot{"bed_room": "1"}
    - slot{"requested_slot": "bath_room"}
* form: house_inform{"number": "1", "guess_room": "1"}
    - slot{"guess_room": "1"}
    - form: house_form
    - slot{"guess_room": "1"}
    - slot{"bath_room": "1"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_request_more_info
* affirm
    - utter_please_to_hear
* house_inform{"local_feature": "free parking", "house_description": "comfortable"}
    - slot{"house_description": "comfortable"}
    - slot{"local_feature": "free parking"}
    - utter_ask_request_more_info
* house_inform{"furniture": "double bed"}
    - utter_understand
    - utter_ask_request_more_info
* deny
    - action_house
    - slot{"found": "Not implement yet"}
    - utter_ask_confirm_information
* deny
    - utter_please_to_hear
* house_inform{"bed_room": "2"}
    - slot{"bed_room": "2"}
    - house_form
    - form{"name": "house_form"}
    - slot{"bed_room": "2"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_request_more_info
* deny
    - utter_ask_confirm_information
* deny
    - utter_need_change_info
* affirm
    - action_house
    - slot{"found": "Not implement yet"}
    - utter_understand
    - utter_ask_satisfaction
* affirm
    - utter_ask_feedback
* feedback
    - utter_thanks_for_feedback
    - utter_call_if_need_help
* affirm
    - utter_goodbye
* goodbye