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

