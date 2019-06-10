## Generated Story -9059401830618429968
* greet
    - utter_greet
* house_request{"real_estate_type": "house", "city": "nhatrang"}
    - slot{"city": "nhatrang"}
    - slot{"real_estate_type": "house"}
    - house_form
    - form{"name": "house_form"}
    - slot{"real_estate_type": "house"}
    - slot{"city": "nhatrang"}
    - slot{"requested_slot": "price"}
* form: house_inform{"price": "1 billions", "currency": "vnd"}
    - slot{"price": "1 billions"}
    - form: house_form
    - slot{"price": null}
    - slot{"requested_slot": "price"}
* form: house_inform{"price": "1000000", "currency": "vnd"}
    - slot{"price": "1000000"}
    - form: house_form
    - slot{"price": "1000000"}
    - slot{"requested_slot": "bed_room"}
* form: house_inform{"number": "2"}
    - form: house_form
    - slot{"bed_room": "2"}
    - slot{"requested_slot": "bath_room"}
* form: house_inform{"number": "1"}
    - form: house_form
    - slot{"bath_room": "1"}
    - slot{"requested_slot": "guess_room"}
* form: house_inform{"number": "1"}
    - form: house_form
    - slot{"guess_room": "1"}
    - slot{"requested_slot": "request_more_info"}
    - form: house_form
    - slot{"requested_slot": "request_more_info"}
    - utter_ask_request_more_info
    - action_listen
* form: house_inform{"house_description": "great", "local_feature": "bus stop"}
    - slot{"house_description": "great"}
    - slot{"local_feature": "bus stop"}
    - house_form
    - slot{"request_more_info": true}
    - slot{"requested_slot": "feedback"}
* form: house_inform
    - form: house_form
    - utter_ask_request_more_info
* deny
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_submit
    - utter_slots_values
    - action_house
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
    - slot{"requested_slot": "request_more_info"}
* form: affirm
    - form: house_form
    - slot{"request_more_info": true}
    - utter_please_to_hear
* house_inform{"house_description": "comfortable", "real_estate_type": "house"}
    - slot{"house_description": "comfortable"}
    - slot{"real_estate_type": "house"}
    - utter_understand
    - utter_ask_request_more_info
* house_inform{"num_persons": "4"}
    - utter_understand
    - utter_ask_request_more_info
* deny
    - utter_understand
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_house
    - slot{"found": "Not implement yet"}
    - utter_ask_satisfaction
* affirm
    - utter_ask_feedback
* feedback
    - utter_thanks_for_feedback
    - utter_call_if_need_help
* affirm

