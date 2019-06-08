## intent:affirm
- okay
- yes yes yes

## intent:ask_howdoing
- How are You?
- and you
- how have you been
- Ahoy matey how are you?
- how's life been treating you?
- Are you ok?
- how's it going?
- Do you feel good?
- How are you men?
- How are you today?
- how is your evening
- hw r u?
- how are you doing today my sweet friend
- What's new?
- how r u
- are you ok
- How are things?

## intent:deny
- no thank you
- not today

## intent:goodbye
- goodbye
- Bye!
- catch you later
- goodbye
- we'll speak soon
- see you later alligator

## intent:greet
- greetings
- hi again
- hi pal!
- hi there
- hi
- good morning

## intent:house_inform
- no more than [$](lookup_tables/currency)[100000](price)
- it will be perfect if there is [two](bed_room) bedrooms with [king-size beds](furniture)
- We have several generations of family living in our household and so need a [very large](house_description)  home
- i need a [free parking](local_feature) available nearby
- i need [metro](transportation) nearby to travel around
- [4](number)
- it will be perfect if there is [two](bed_room) bedrooms with [king-size beds](furniture)
- i need some [modern coach](furniture)
- i need [double](bed_room) bedroom in our [modern](house_description) new [apartment](real_estate_type) in [Lao Cai](city)
- i want a [spacous](house_description) and [comfortable](house_description)
- I would like to live in [nha trang](city)
- [Ho Chi Minh](city) city
- [Comfortable](house_description) and [bright](house_description)
- no more than [100000](price) [dollars](lookup_tables/currency)
- [5](bath_room) bathroom
- i need to go to [metro station](local_feature) in no more than [5](time_spent) minute
- i need to go to [free parking](local_feature) in no more than [5](time_spent) minute

## intent:house_request
- would you mind give me some information about [home](real_estate_type) for sell?
- is there any [houses](real_estate_type) less than [1 billion](price) [dollars](lookup_tables/currency)?
- give me the list of [apartment](real_estate_type) in [hcm](city)
- I am looking to buy a [house](real_estate_type) for myself and my son
- i want to find a [house](real_estate_type) in [Hanoi](city)
- I am interested in buying a [house](real_estate_type) and need some information.
- i need some information about houses in [hanoi](city) city
- I have been thinking of buying a [house](real_estate_type) and would like to speak with you.
- search me some [apartment](real_estate_type) in [nhatrang](city) city
- i would like to buy a [house](real_estate_type) in [DaNang](city)city with [1 billion](price) [vnd](lookup_tables/currency)
- give me the list of [houses](real_estate_type) in [hcm](city)
- i am looking for [home](real_estate_type) in [danang](city)
- I'm interested in the [home](real_estate_type) in [Lang Son](city). What can you tell me about it?
- search me some [houses](real_estate_type) in [nhatrang](city) city
- i would like to buy a [house](real_estate_type) in [DaNang](city)city with [1 billion](price) [vnd](lookup_tables/currency)
- i would like to buy a [house](real_estate_type) in [DaNang](city)city with [1 billion](price) [vnd](lookup_tables/currency)
- I would like to discuss purchasing a [home](real_estate_type) with you.
- i need some information about [apartment](real_estate_type) in [hanoi](city) city
- i am looking for [apartment](real_estate_type)
- i want to find a [house](real_estate_type) in [Hanoi](city)
- I have been thinking of buying a [home](real_estate_type) and would like to speak with you
- I am interested in buying a [house](real_estate_type) and need some information.
- Is there a [house](real_estate_type) in range [4 millions](price) [dollars](lookup_tables/currency)?
- I am interested in buying a [apartment](real_estate_type) and need some information.

## intent:thankyou
- ok thanks!
- Thank you so much
- Thanks for that

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

## synonym:HCM city
- Ho Chi Minh City
- HoChiMinh City
- hochiminh city
- ho chi minh
- hcmc
- Sai Gon
- Saigon
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
