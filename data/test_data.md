## intent:affirm
- absolutely
- yes sure

## intent:ask_howdoing
- how you doing
- how is your day going
- how are you doing
- how are you ?
- how are you
- hi how are you?
- Do you feel good?
- and you
- What's going on?
- hi sara, how are you?
- How's it hanging?
- how do you do?
- how are xou
- how's life been treating you?
- is everything all right
- hw r u?
- what's up?

## intent:deny
- no thanks
- no thank you

## intent:feedback
- very stupid
- not good enough

## intent:goodbye
- Bye bot
- goodbye
- gotta go
- See you later
- Bye!
- Goodbye friend

## intent:greet
- Hi
- Hi bot
- hi folks
- hello robot
- nice to meet you
- hi there

## intent:house_inform
- i need to travel to [central of the](city) city in less than [10](time_spent) minute
- i need [one](number)
- I am willing to raise my offer to [$](currency)[330K](price)
- The local area also features several delicious [restaurants](local_feature), a [bakery](local_feature) and [leisure facilities](local_feature)
- in [Ho Chi Minh](city) city
- i need [2](number) only
- i think [1](number)
- i need [two](guess_room) guess room
- i need [metro](transportation) nearby to travel around
- i need to go to [metro station](local_feature) in no more than [5](time_spent) minute
- The asking price has recently gone down to two hundred and [25k](price) [usd](currency)
- no more than [$](currency)[100000](price)
- more than [3](number)
- The room i want has a [queen size bed](furniture) ideal for [2](num_persons) persons
- it is better if i can go to [the bus](transportation) in [25](time_spent) minutes
- About [5](time_spent) minutes to the closest [metro station](local_feature)
- i need [double](bed_room) bedroom in our [modern](house_description) new [apartment](real_estate_type) in [Lao Cai](city)
- at least [one](number)
- i want a house with [side of the beach](local_feature) which is less than [2 millions](price) [usd](currency) in [Hochiminh](city) city
- i am find a house with [two](bed_room) bedrooms which is no more than [2 millions](price) [euro](currency) in [Ca Mau](city) city
- i need a house with [two](guess_room) guess room which is only [2 millions](price) [vnd](currency) in [Hanoi](city)

## intent:house_request
- would you mind give me some information about [apartment](real_estate_type) for sell?
- I would like to discuss purchasing a [home](real_estate_type) with you.
- i need some information about [houses](real_estate_type) in [hanoi](city) city
- Is there a [house](real_estate_type) in range [4 millions](price) [dollars](currency)?
- give me some [flat](real_estate_type)
- is there any [flat](real_estate_type) less than [1 billion](price) [dollars](currency)?
- I am interested in buying a [home](real_estate_type) and need some information.
- give me some [houses](real_estate_type) for [4](num_persons) persons
- I'd like to view some [homes](real_estate_type) now
- I have been thinking of buying a [house](real_estate_type) and would like to speak with you.
- I am looking to buy a [house](real_estate_type) for myself and my son
- i want to buy a [home](real_estate_type) for [4](num_persons) persons
- give me some [apartment](real_estate_type) for [4](num_persons) persons
- would you mind give me some information about [flat](real_estate_type) for sell?
- I would like to discuss purchasing a [home](real_estate_type) with you.
- give me some [home](real_estate_type) for [4](num_persons) persons
- I have been thinking of buying a [home](real_estate_type) and would like to speak with you
- I have been thinking of buying a [houses](real_estate_type) and would like to speak with you
- I want to go [flat](real_estate_type) shopping
- i am looking for [flat](real_estate_type)
- i would like to buy a [house](real_estate_type) in [DaNang](city)city with [1 billion](price) [vnd](currency)
- I am interested in buying a [house](real_estate_type) and need some information.
- give me some [houses](real_estate_type) for [4](num_persons) persons
- i am looking for [houses](real_estate_type)

## intent:thankyou
- Thank you so much
- thanks a lot
- perfect thank you

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

## synonym:apartment
- apartments
- flats
- flat

## synonym:house
- houses
- homes
- home

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
