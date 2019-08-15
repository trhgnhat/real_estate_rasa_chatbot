## Generated Story 1484301423811423976
* house_inform{"real_estate_type": "house", "city": "hanoi", "price": "2 billions", "currency": "usd", "bed_room": "2"}
    - slot{"bed_room": "2"}
    - slot{"city": "hanoi"}
    - slot{"currency": "usd"}
    - slot{"price": "2 billions"}
    - slot{"real_estate_type": "house"}
    - form_house_request
    - form{"name": "form_house_request"}
    - slot{"real_estate_type": "house"}
    - slot{"city": "hanoi"}
    - slot{"price": "2 billions"}
    - slot{"currency": "usd"}
    - slot{"bed_room": "2"}
    - slot{"requested_slot": "bath_room"}
* form: house_inform{"number": "2"}
    - form: form_house_request
    - slot{"bath_room": "2"}
    - slot{"requested_slot": "guess_room"}
* form: house_inform{"number": "1"}
    - form: form_house_request
    - slot{"guess_room": "1"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_request_more_info
* affirm
    - utter_please_to_hear
* form: house_inform{"house_description": "comfortable", "real_estate_type": "house"}
    - slot{"house_description":"comfortable"}
    - slot{"real_estate_type":"house"}
    - form: form_house_request
    - form{"name": "form_house_request"}
    - slot{"house_description": "comfortable"}
    - slot{"real_estate_type": "house"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_understand
    - utter_ask_request_more_info
* form: house_inform{"num_person": "4"}
    - slot{"num_person": "4"}
    - form: form_house_request
    - form{"name": "form_house_request"}
    - slot{"num_person": "4"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_understand
    - utter_ask_request_more_info
* deny OR confirm
    - action_post_house_info
    - utter_ask_confirm_information
* deny
    - utter_need_change_info
    - utter_please_to_hear
* house_inform{"bed_room": "2"}
    - slot{"bed_room": "2"}
    - form_house_request
    - form{"name": "form_house_request"}
    - slot{"bed_room": "2"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_understand
    - utter_ask_request_more_info
* deny OR confirm
    - action_post_house_info
    - utter_ask_confirm_information
* deny
    - utter_need_change_info
    - utter_please_to_hear
* house_inform{"bed_room": "3"}
    - slot{"bed_room": "3"}
    - form_house_request
    - form{"name": "form_house_request"}
    - slot{"bed_room": "3"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_understand
    - utter_ask_request_more_info
* deny OR confirm
    - action_post_house_info
    - utter_ask_confirm_information
* affirm OR confirm
    - utter_understand
    - action_house
    - slot{"found": "Not implement yet"}
    - utter_ask_satisfaction
* deny OR ask_more
    - utter_next_recommendation
    - action_house
    - utter_ask_satisfaction
* deny OR ask_more
    - utter_next_recommendation
    - action_house
    - utter_ask_satisfaction
* thankyou
    - utter_noworries
    - utter_ask_feedback
* deny
    - utter_understand
    - utter_call_if_need_help
    - action_wait_for_command
* affirm OR thankyou
    - utter_goodbye
* goodbye
    - action_wait_for_command

## Generated Story 3368241047826805535
* greet
    - utter_greet
* house_request{"real_estate_type": "house", "city": "hanoi"}
    - slot{"city": "hanoi"}
    - slot{"real_estate_type": "house"}
    - form_house_request
    - form{"name": "form_house_request"}
    - slot{"real_estate_type": "house"}
    - slot{"city": "hanoi"}
    - slot{"requested_slot": "price"}
* form: house_inform{"price": "1 billions", "currency": "usd"}
    - slot{"currency": "usd"}
    - slot{"price": "1 billions"}
    - form: form_house_request
    - slot{"currency": "usd"}
    - slot{"price": null}
    - slot{"requested_slot": "price"}
* form: house_inform{"price": "1 billion", "currency": "usd"}
    - slot{"currency": "usd"}
    - slot{"price": "1 billion"}
    - form: form_house_request
    - slot{"currency": "usd"}
    - slot{"price": null}
    - slot{"requested_slot": "price"}
* form: house_inform{"price": "1 million", "currency": "usd"}
    - slot{"currency": "usd"}
    - slot{"price": "1 million"}
    - form: form_house_request
    - slot{"currency": "usd"}
    - slot{"price": "1000000"}
    - slot{"requested_slot": "bed_room"}
* form: number{"number": "1"}
    - form: form_house_request
    - slot{"bed_room": "1"}
    - slot{"requested_slot": "bath_room"}
* form: house_inform{"number": "1", "guess_room": "1"}
    - slot{"guess_room": "1"}
    - form: form_house_request
    - slot{"guess_room": "1"}
    - slot{"bath_room": "1"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_request_more_info
* deny OR confirm
    - action_post_house_info
    - utter_ask_confirm_information
* deny
    - utter_need_change_info
    - utter_please_to_hear
* house_inform{"bed_room": "2"}
    - slot{"bed_room": "2"}
    - form_house_request
    - form{"name": "form_house_request"}
    - slot{"bed_room": "2"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_understand
    - utter_ask_request_more_info
* deny OR confirm
    - action_post_house_info
    - utter_ask_confirm_information
* deny
    - utter_need_change_info
    - utter_please_to_hear
* house_inform{"bed_room": "3"}
    - slot{"bed_room": "3"}
    - form_house_request
    - form{"name": "form_house_request"}
    - slot{"bed_room": "3"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_understand
    - utter_ask_request_more_info
* deny OR confirm
    - action_post_house_info
    - utter_ask_confirm_information
* affirm OR confirm
    - utter_understand
    - action_house
    - slot{"found": "Not implement yet"}
    - utter_ask_satisfaction
* deny OR ask_more
    - utter_next_recommendation
    - action_house
    - utter_ask_satisfaction
* deny OR ask_more
    - utter_next_recommendation
    - action_house
    - utter_ask_satisfaction
* deny OR ask_more
    - utter_need_change_info
* deny
    - utter_next_recommendation
    - action_house
    - utter_ask_satisfaction
* thankyou
    - utter_noworries
    - utter_ask_feedback
* feedback
    - utter_thanks_for_feedback
    - utter_call_if_need_help
    - action_wait_for_command
* affirm OR thankyou
    - utter_goodbye
* goodbye
    - action_wait_for_command

## Generated Story 3368241047826805555
* greet
    - utter_greet
* house_request{"real_estate_type": "house", "city": "hanoi"}
    - slot{"city": "hanoi"}
    - slot{"real_estate_type": "house"}
    - form_house_request
    - form{"name": "form_house_request"}
    - slot{"real_estate_type": "house"}
    - slot{"city": "hanoi"}
    - slot{"requested_slot": "price"}
* form: house_inform{"price": "1 billions", "currency": "usd"}
    - slot{"currency": "usd"}
    - slot{"price": "1 billions"}
    - form: form_house_request
    - slot{"currency": "usd"}
    - slot{"price": null}
    - slot{"requested_slot": "price"}
* form: house_inform{"price": "1 billion", "currency": "usd"}
    - slot{"currency": "usd"}
    - slot{"price": "1 billion"}
    - form: form_house_request
    - slot{"currency": "usd"}
    - slot{"price": null}
    - slot{"requested_slot": "price"}
* form: house_inform{"price": "1 million", "currency": "usd"}
    - slot{"currency": "usd"}
    - slot{"price": "1 million"}
    - form: form_house_request
    - slot{"currency": "usd"}
    - slot{"price": "1000000"}
    - slot{"requested_slot": "bed_room"}
* form: number{"number": "1"}
    - form: form_house_request
    - slot{"bed_room": "1"}
    - slot{"requested_slot": "bath_room"}
* form: house_inform{"number": "1", "guess_room": "1"}
    - slot{"guess_room": "1"}
    - form: form_house_request
    - slot{"guess_room": "1"}
    - slot{"bath_room": "1"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_request_more_info
* deny OR confirm
    - action_post_house_info
    - utter_ask_confirm_information
* deny
    - utter_need_change_info
    - utter_please_to_hear
* house_inform{"bed_room": "2"}
    - slot{"bed_room": "2"}
    - form_house_request
    - form{"name": "form_house_request"}
    - slot{"bed_room": "2"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_understand
    - utter_ask_request_more_info
* deny OR confirm
    - action_post_house_info
    - utter_ask_confirm_information
* deny
    - utter_need_change_info
    - utter_please_to_hear
* house_inform{"bed_room": "3"}
    - slot{"bed_room": "3"}
    - form_house_request
    - form{"name": "form_house_request"}
    - slot{"bed_room": "3"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_understand
    - utter_ask_request_more_info
* deny OR confirm
    - action_post_house_info
    - utter_ask_confirm_information
* affirm OR confirm
    - utter_understand
    - action_house
    - slot{"found": "Not implement yet"}
    - utter_ask_satisfaction
* deny OR ask_more
    - utter_next_recommendation
    - action_house
    - utter_ask_satisfaction
* deny OR ask_more
    - utter_next_recommendation
    - action_house
    - utter_ask_satisfaction
* deny OR ask_more
    - utter_need_change_info
* affirm
    - utter_ask_request_more_info
* house_inform{"bed_room": "3"}
    - slot{"bed_room": "3"}
    - form_house_request
    - form{"name": "form_house_request"}
    - slot{"bed_room": "3"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_understand
    - action_post_house_info
    - utter_ask_confirm_information
* affirm OR confirm
    - action_house
    - utter_ask_satisfaction
* deny OR ask_more
    - utter_next_recommendation
    - action_house
    - utter_ask_satisfaction
* affirm OR confirm
    - utter_ask_feedback
* feedback
    - utter_thanks_for_feedback
    - utter_call_if_need_help
* affirm OR goodbye
    - utter_goodbye
    - action_wait_for_command
    
## Generated Story 5649617401339704074
* greet
    - utter_greet
* house_inform{"real_estate_type": "house", "city": "hochiminh"}
    - slot{"city": "hochiminh"}
    - slot{"real_estate_type": "house"}
    - form_house_request
    - form{"name": "form_house_request"}
    - slot{"real_estate_type": "house"}
    - slot{"city": "hochiminh"}
    - slot{"requested_slot": "price"}
* form: house_inform{"price": "1 million", "currency": "usd"}
    - slot{"currency": "usd"}
    - slot{"price": "1 million"}
    - form: form_house_request
    - slot{"currency": "usd"}
    - slot{"price": "1000000"}
    - slot{"requested_slot": "bed_room"}
* form: house_inform{"number": "1"}
    - form: form_house_request
    - slot{"bed_room": "1"}
    - slot{"requested_slot": "bath_room"}
* form: house_inform{"number": "two"}
    - form: form_house_request
    - slot{"bath_room": null}
    - slot{"requested_slot": "bath_room"}
* form: house_inform{"bath_room": "two"}
    - slot{"bath_room": "two"}
    - form: form_house_request
    - slot{"bath_room": null}
    - slot{"requested_slot": "bath_room"}
* form: house_inform{"number": "1"}
    - form: form_house_request
    - slot{"bath_room": "1"}
    - slot{"requested_slot": "guess_room"}
* form: house_inform{"number": "6"}
    - form: form_house_request
    - slot{"guess_room": "6"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_request_more_info
* affirm
    - utter_please_to_hear
* house_inform{"local_feature": "bus station", "house_feature": "large windows", "real_estate_type": "house"}
    - slot{"house_feature": ["large windows"]}
    - slot{"local_feature": ["bus station"]}
    - slot{"real_estate_type": "house"}
    - form_house_request
    - form{"name": "form_house_request"}
    - slot{"real_estate_type": "house"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_understand
    - utter_ask_request_more_info
* affirm
    - utter_please_to_hear
* house_inform{"furniture": "sofa"}
    - slot{"furniture": ["sofa"]}
    - utter_understand
    - utter_ask_request_more_info
* house_inform{"num_person": "four", "real_estate_type": "house", "house_description": "big"}
    - slot{"house_description": ["big"]}
    - slot{"num_person": "four"}
    - slot{"real_estate_type": "house"}
    - form_house_request
    - form{"name": "form_house_request"}
    - slot{"real_estate_type": "house"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_request_more_info
* deny
    - action_post_house_info
    - utter_ask_confirm_information
* house_inform{"currency": "vnd"}
    - slot{"currency": "vnd"}
    - utter_understand
    - action_post_house_info
    - utter_ask_confirm_information
* confirm
    - action_house
    - slot{"found": "Not implement yet"}
    - utter_ask_satisfaction
* deny
    - utter_next_recommendation
    - action_house
    - slot{"found": "Not implement yet"}
    - utter_ask_satisfaction
* ask_more
    - utter_next_recommendation
    - action_house
    - slot{"found": "Not implement yet"}
    - utter_ask_satisfaction
* affirm
    - utter_ask_feedback
* feedback
    - utter_thanks_for_feedback
    - utter_call_if_need_help
* thankyou
    - utter_noworries
    - action_wait_for_command
    
## user connection 1
* talk_to_person{"person_id": "@trhgnhat"}
    - slot{"person_id":"@trhgnhat"}
    - form_setup_meeting
    - form{"name": "form_setup_meeting"}
    - slot{"person_id":"trhgnhat"}
    - slot{"person_name":"Truong Hoang Nhat"}
    - form{"name": "null"}
* thankyou
    - utter_noworries
    
## user connection 2
* talk_to_person{"person_name":"Truong Hoang Nhat"}
    - slot{"person_name":"Truong Hoang Nhat"}
    - form_setup_meeting
    - form{"name": "form_setup_meeting"}
    - slot{"person_name":"Truong Hoang Nhat"}
    - slot{"person_id":"trhgnhat"}
    - form{"name": "null"}
* thankyou
    - utter_noworries
    - utter_call_if_need_help
    
## meeting setup 1
* set_appointment{"person_id": "@trhgnhat", "time": "2019-07-15T10:00:00.000+07:00"}
    - slot{"person_id":"@trhgnhat"}
    - slot{"time":"2019-07-15T10:00:00.000+07:00"}
    - form_setup_meeting
    - form{"name": "form_setup_meeting"}
    - slot{"person_id":"trhgnhat"}
    - slot{"time":"2019-07-15T10:00:00.000+07:00"}
    - form{"name": "null"}
* thankyou
    - utter_noworries
    - utter_call_if_need_help
    
## meeting setup 2
* set_appointment{"person_id": "@trhgnhat"}
    - slot{"person_id":"@trhgnhat"}
    - form_setup_meeting
    - form{"name": "form_setup_meeting"}
    - slot{"person_id":"trhgnhat"}
    - slot{"requested_slot": "time"}
* set_appointment{"time": "2019-07-15T10:00:00.000+07:00"}
    - slot{"time":"2019-07-15T10:00:00.000+07:00"}
    - form_setup_meeting
    - form{"name": "form_setup_meeting"}
    - slot{"time":"2019-07-15T10:00:00.000+07:00"}
    - form{"name": "null"}
    - slot{"requested_slot": "null"}
* thankyou
    - utter_noworries
    - utter_call_if_need_help
    
## Generated Story 6795522051165450699
* talk_to_person{"person_id": "@nhat97"}
    - slot{"person_id": "@nhat97"}
    - form_connect_to_person
    - form{"name": "form_connect_to_person"}
    - slot{"person_id": null}
    - slot{"person_id": null}
    - slot{"requested_slot": "person_id"}
* form: person_inform{"person_id": "@trhgnhat"}
    - slot{"person_id": "@trhgnhat"}
    - form: form_connect_to_person
    - slot{"person_id": "trhgnhat"}
    - slot{"person_name": "Truong Hoang Nhat"}
    - form: followup{"name": "action_listen"}
    - form{"name": null}
    - slot{"requested_slot": null}
* thankyou
    - utter_noworries
    - utter_call_if_need_help

## Generated Story 5613579522888608487
* set_appointment{"person_name": "truong hoang nhat", "time": "2019-07-20T16:02:10.000+07:00"}
    - slot{"person_name": "truong hoang nhat"}
    - slot{"time": "2019-07-20T16:02:10.000+07:00"}
    - form_setup_meeting
    - form{"name": "form_setup_meeting"}
    - slot{"person_name": "Truong Hoang Nhat"}
    - slot{"time": "2019-07-20T16:02:10.000+07:00"}
    - slot{"person_id": "trhgnhat"}
    - slot{"person_name": "Truong Hoang Nhat"}
    - slot{"time": "2019-07-20T16:02:10.000+07:00"}
    - slot{"person_id": "trhgnhat"}
    - form: reminder{"action": "action_remind_meeting", "date_time": "2019-07-20T15:57:10", "name": "87fd5e36-aacc-11e9-bb1d-b46d839b8bc8", "kill_on_user_msg": false}
    - form{"name": null}
    - slot{"requested_slot": null}
* thankyou
    - utter_noworries
    - utter_call_if_need_help
* confirm

## Generated Story post action
* post_action{"action_type": "delete", "post_id": "all"}
    - slot{"action_type": "delete"}
    - slot{"post_id": "all"}
    - form_post_action
    - form{"name": "form_post_action"}
    - slot{"action_type": "delete"}
    - slot{"post_id": "all"}
    - form{"name": null}
    - slot{"requested_slot": null}
* thankyou
    - utter_noworries
    - utter_call_if_need_help
* confirm

## Generated Story show_dashboard
* post_action{"visual_type": "chart of trending"}
    - slot{"visual_type": "chart of trending"}
    - form_post_action
    - form{"name": "form_post_action"}
    - slot{"visual_type": "chart of trending"}
    - form{"name": null}
    - slot{"requested_slot": null}
* thankyou
    - utter_noworries
    - utter_call_if_need_help
* confirm

