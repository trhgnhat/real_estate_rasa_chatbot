## Generated Story 1: buy house
* greet
    - utter_greet
* buy_house
    - utter_ask_location
* buy_house{"location": "Saigon"}
    - slot{"location": "Saigon"}
    - utter_ask_price
* buy_house{"price": "10000"}
    - slot{"price": "10000"}
    - action_house
* goodbye
    - utter_goodbye

## Generated Story 2: buy house
* buy_house
    - utter_ask_price
* buy_house{"location": "10000"}
    - slot{"location": "10000"}
    - utter_ask_location
* buy_house{"price": "Saigon"}
    - slot{"price": "Saigon"}
    - action_house
* goodbye
    - utter_goodbye

## Generated Story 3: buy house
* buy_house
    - utter_ask_location
* buy_house{"location": "Hanoi"}
    - slot{"location": "Hanoi"}
    - utter_ask_price
* buy_house{"price": "1K dollar"}
    - slot{"price": "1K dollar"}
    - action_house
* goodbye
    - utter_goodbye


## fallback
- utter_unclear  

## Generated Story -1215971627746700505
    - utter_greet
* buy_house
    - utter_ask_price
* buy_house{"price": "1m dollar"}
    - slot{"price": "1m dollar"}
    - utter_ask_location
* buy_house{"location": "saigon"}
    - slot{"location": "saigon"}
    - action_house
* thanks
    - utter_welcome
    - utter_goodbye
* goodbye

## Generated Story 1048030250816580225
* greet
    - utter_greet
* buy_house
    - utter_ask_location
* buy_house{"location": "hanoi"}
    - utter_ask_price
* buy_house{"price": " 1m dollars"}
    - action_house

## Generated Story 2548024168404657165
* greet
    - utter_greet
* house_request{"location": "danang"}
    - house_form
    - form{"name": "house_form"}
    - slot{"location": "danang"}
    - slot{"requested_slot": "price"}
* form: inform{"price": "$1M"}
    - form: house_form
    - slot{"price": null}
    - slot{"requested_slot": "price"}
* inform
    - utter_unclear
    - utter_ask_price
    - action_listen
* form: inform{"price": "100000"}
    - house_form
    - slot{"price": "100000"}
    - slot{"requested_slot": "feedback"}
* form: inform
    - form: house_form
    - slot{"feedback": "it is pretty stupid for now"}
    - slot{"location": "danang"}
    - slot{"price": "100000"}
    - slot{"feedback": "it is pretty stupid for now"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slots_values
* thanking
    - utter_noworries
* inform{"price": "200000"}
    - house_form
    - form{"name": "house_form"}
    - slot{"price": "200000"}
    - slot{"location": "danang"}
    - slot{"price": "200000"}
    - slot{"feedback": "it is pretty stupid for now"}
    - form{"name": null}
    - slot{"requested_slot": null}
* inform{"local_feature": "free parking"}

