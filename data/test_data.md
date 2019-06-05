## intent:affirm
- yes sure
- ok

## intent:ask_howdoing
- How are you today?
- Hows it going
- what's up?
- are you ok
- How's life treating you friend?
- what about your day
- how are you doing?
- how you doing?
- Do you have a great day?
- Is everything ok?
- How was your day?
- how's your day going
- and you
- hi sara, how are you?
- are you having a good day
- how are you????
- how are u?

## intent:deny
- noope
- no this does not work for me

## intent:goodbye
- goodnight
- farewell
- goodbye
- we'll speak soon
- bye for now
- Bye

## intent:greet
- hi Mister
- hi pal!
- yo
- hey there
- hello robot
- hey

## intent:house_inform
- i want a [spacous](house_feature) and [comfortable](house_feature)
- no more than [$](lookup_tables/currency)[1M](price)
- hey i think i will change the price to more than [200000](price) [dollars](lookup_tables/currency)
- I am willing to raise my offer to [$](lookup_tables/currency)[330K](price)
- In a perfect world, we would like a [home](real_estate_type) with a [view of the lake](local_feature)
- hey i think i will change the price to more than [200000](price) [vnd](lookup_tables/currency)
- [Ho Chi Minh ](city) city
- i need [a bus stop](transportation) nearby
- There is maximum space for [6 persons](num_persons)
- no more than [100000](price) [dollars](lookup_tables/currency)
- i need to travel to [restaurant](local_feature) in no more than [10 minute](time_spent)
- no more than [$](lookup_tables/currency)[100000](price)
- the modern room features a[king-size bed](house_feature) and [large windows](house_feature)
- I would like to live in [Pasadena](city)

## intent:house_request
- i am find a [house](real_estate_type) with [two bedrooms](bed_room) which is no more than [2 millions](price) [euro](lookup_tables/currency) in [Ca Mau ](city) city
- I'd like to view some [homes](real_estate_type) now
- I am interested in buying a [houses](real_estate_type) and need some information.
- i want to buy a [flat](real_estate_type) for [4 persons](num_persons)
- I have been thinking of buying a [house](real_estate_type) and would like to speak with you.
- i am looking for [home](real_estate_type)
- I am interested in buying a [apartment](real_estate_type) and need some information.
- I would like to discuss purchasing a [home](real_estate_type) with you.
- search me some [houses](real_estate_type) no more than [1 million](price) in [nha trang ](city) city
- would you mind give me some information about [home](real_estate_type) for sell?
- I would like to discuss purchasing a [home](real_estate_type) with you.
- i want to buy a [houses](real_estate_type) for [4 persons](num_persons)
- i am looking for [apartment](real_estate_type)
- I am looking to buy a [house](real_estate_type) for myself and my son
- give me some [home](real_estate_type)
- is there any [houses](real_estate_type) less than [1 billion](price) [dollars](lookup_tables/currency)?
- search me some [flat](real_estate_type) no more than [1 million](price) in [nha trang ](city) city
- Is there a [house](real_estate_type) in range [4 millions](price) [dollars](lookup_tables/currency)?
- give me some [houses](real_estate_type)
- give me the list of [houses](real_estate_type) in [hcm](city)
- i would like to buy a [house](real_estate_type) in [DaNang](city)city with [1 billion](price) [vnd](lookup_tables/currency)
- i need some information about [houses](real_estate_type) in [hanoi](city) city
- i want [flat](real_estate_type)
- I am looking to buy a [house](real_estate_type) for myself and my son

## intent:thankyou
- perfect thank you
- Thanks for that
- Thank you

## synonym:Ho Chi Minh
- data/lookup_tables/synonyms/Ho\Chi\Minh.txt

## synonym:apartment
- flat

## synonym:house
- houses
- home

## synonym:usd
- dollars
- $
- dollar


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
