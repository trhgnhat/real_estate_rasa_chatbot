## intent:affirm
- yes sure
- yeah
- yes

## intent:ask_howdoing
- How are you today?
- nah, I'm good - how are you doing?
- how are you????
- Is everything ok?
- how have you been
- hi sara, how are you?
- how are you?
- are you ok
- is everything all right
- what's good
- What's going on?
- how are you doing today?
- is everything okay
- How are You?
- hw r u?
- how are u?
- what's up?

## intent:ask_more
- show me more options
- its good but give me more options

## intent:confirm
- confirmed
- it's okay

## intent:deny
- noope
- not today
- no

## intent:feedback
- excellence
- very stupid
- not good enough

## intent:goodbye
- bye bye
- Bye
- Bye bot
- bye
- gotta go
- Bye

## intent:greet
- heya
- hi
- good morning
- greetings
- hi Mister
- hi

## intent:house_inform
- [5](number) thanks
- i need a [house](real_estate_type) in [hochiminh](city) city
- I would love to have a [home](real_estate_type) with a [view](local_feature)
- less than [seven](number)
- [5](bath_room) bathrooms
- at most [2](number)
- [three](number) room i guess
- [two](bath_room) bathrooms please
- hey i think i will change the price to more than [200000](price) [vnd](currency)
- i need a house with [two](guess_room) guess room which is only [2 millions](price) [vnd](currency) in [Hanoi](city)
- [6](number)
- [1](number) please
- i need to travel to [central of the](city) city in less than [10](time_spent) minute
- i need a [bus stop](local_feature) nearby
- i want a house with [side of the beach](local_feature) which is less than [2 millions](price) [usd](currency) in [Hochiminh](city) city
- i need to travel to [restaurant](local_feature) in no more than [10](time_spent) minute
- I am thinking of moving  to [Hawaii](city)
- The local area also features several delicious [restaurants](local_feature), a [bakery](local_feature) and [leisure facilities](local_feature)
- [6](number) is ok
- i am find a house with [two](bed_room) bedrooms which is no more than [2 millions](price) [euro](currency) in [Ca Mau](city) city
- i need [security](house_description)
- i will pay by [vnd](currency)
- no more than [1000000](price) [vnd](currency) please

## intent:house_request
- i am looking for [flat](real_estate_type)
- is there any [houses](real_estate_type) less than [1 billion](price) [dollars](currency)?
- I have been thinking of buying a [apartment](real_estate_type) and would like to speak with you
- I would like to discuss purchasing a [home](real_estate_type) with you.
- I'm interested in the [flat](real_estate_type) in [Lang Son](city). What can you tell me about it?
- i need some information about [houses](real_estate_type) in [hanoi](city) city
- I'd like to view some [homes](real_estate_type) now
- need [apartment](real_estate_type) for sell
- i am looking for [houses](real_estate_type) in [danang](city)
- i want [houses](real_estate_type)
- I am looking to buy a [house](real_estate_type) for myself and my son
- give me some [houses](real_estate_type)
- i want to buy a [flat](real_estate_type) for [4](num_person) persons
- i am looking for [apartment](real_estate_type) in [danang](city)
- search me some [apartment](real_estate_type) in [nhatrang](city) city
- give me the list of [home](real_estate_type) in [hcm](city)
- I have been thinking of buying a [home](real_estate_type) and would like to speak with you
- would you mind give me some information about [apartment](real_estate_type) for sell?
- I'm interested in the [houses](real_estate_type) in [Danang](city). What can you tell me about it?
- I have been thinking of buying a [house](real_estate_type) and would like to speak with you.
- i want [houses](real_estate_type)
- i want to buy a [houses](real_estate_type) for [4](num_person) persons
- is there any [flat](real_estate_type) less than [1 billion](price) [dollars](currency)?
- I want to go [flat](real_estate_type) shopping

## intent:person_inform
- to [@ititiu15086](person_id) please
- [@ititiu15086](person_id)

## intent:post_action
- [delete](action_type) [all](post_id) my posts for me please
- [remove](action_type) [all](post_id) posts.

## intent:set_appointment
- next month
- right now
- arrange an appointment with [Nhat](person_name) on sunday afternoon for me please

## intent:show_dashboard
- display the [chart of trending](visual_type)
- show me the [map of contracts](visual_type)

## intent:talk_to_person
- connect me to [@ititiu15086](person_id) please
- i want to say something with [Nhat](person_name) for a moment
- contact [Nhat](person_name) for me please
- let's me talk to [@trhgnhat](person_id)

## intent:thankyou
- Thank you so much
- cool thank you
- Thank you
- perfect thank you

## synonym:0
- zero

## synonym:000
- k
- thousand
- thousands

## synonym:000000
- millions
- million
- mil
- M
- 000 000
- 000.000
- 000,000

## synonym:000000000
- billions
- bil
- B
- billion
- 000 000 000
- 000.000.000
- 000,000,000

## synonym:1
- one

## synonym:10
- ten

## synonym:2
- two

## synonym:2019-07-20T16:02:10.000+07:00
- in five minutes

## synonym:3
- three

## synonym:4
- four

## synonym:5
- five

## synonym:6
- six

## synonym:7
- seven

## synonym:8
- eight

## synonym:9
- nine

## synonym:Ho Chi Minh
- Ho Chi Minh City
- hochiminh city
- hcmc
- Sai Gon
- saigon
- hcm

## synonym:activate
- turn on
- switch on

## synonym:apartment
- apartments
- flats
- flat

## synonym:appointment
- meeting

## synonym:chart of trending
- trend of transaction
- trend of exchange
- chart of transaction

## synonym:deactivate
- turn off
- switch off

## synonym:delete
- remove
- erase
- drop

## synonym:house
- houses
- homes
- home

## synonym:map of houses
- map of contracts
- map of house

## synonym:truong hoang nhat
- Truong Hoang Nhat

## synonym:usd
- dollar
- dollars
- $

## regex:bath_room
- (\d{2}\s*(?i)(?:[b]+[a]+[t]+[h]+\s*[r]+[o]+[o]+[m]+[s]*)+)+

## regex:bed_room
- (\d{2}\s*(?i)(?:[b]+[e]+[d]+\s*[r]+[o]+[o]+[m]+[s]*)+)+

## regex:city
- [aA-zZ]+\s*(?i)[c]+[i]+[t]+[y]+

## regex:guess_room
- (\d{2}\s*(?i)(?:[g]+[u]+[e]+[s]+[s]+\s*[r]+[o]+[o]+[m]+[s]*)+)+

## regex:number
- [0-9]+

## regex:person_id
- @[aA0-zZ9\.\-\_]+

## regex:price
- (\d+\s*(?:[bB]+[iI]+[lL]+[lL]+[iI]+[oO]+[nN]+[sS]*)+)+
- (\d+\s*(?:[bB]+[iI]+[lL]+[lL]+[iI]+[oO]+[nN]+[sS]*)+)+
- (\d+\s*(?:[mM]+[iI]+[lL]+[lL]+[iI]+[oO]+[nN]+[sS]*)+)+

## regex:zipcode
- [0-9]{5}

## lookup:real_estate_type
- apartment
- flat
- house
- home

## lookup:city
  data/lookup_tables/location/city.txt

## lookup:currency
  data/lookup_tables/currency/currency.txt

## lookup:house_description
  data/lookup_tables/house_features/house_description.txt

## lookup:house_description
  data/lookup_tables/house_features/furnitures.txt

## lookup:action_type
  data/lookup_tables/post/action.txt

## lookup:visual_type
  data/lookup_tables/visualization/visual_types.txt
