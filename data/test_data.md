## intent:affirm
- si
- yes sure

## intent:ask_howdoing
- how are you today
- is everything all right
- hw r u?
- how are you doing today my sweet friend
- how are you'
- Hi Sara! How are you?
- how is your day going
- what's up
- How are you?
- how you doing?
- how are things with you?
- hello, how are you?
- how are you feeling
- How's life treating you friend?
- how are u?
- How was your day?
- nah, I'm good - how are you doing?

## intent:ask_more
- is there anything else?
- more options please,

## intent:confirm
- i confirm
- ok

## intent:deny
- do you have something else
- not today

## intent:feedback
- it is a great experience
- it is a great experience

## intent:goodbye
- bye
- bye
- goodbye
- Goodbye
- bye bye
- Goodbye friend

## intent:greet
- hello everybody
- hi
- hi pal!
- hi again
- heya
- Hey

## intent:house_inform
- Yes, we want to stay in the [hanoi](city)
- We really want to live in a [lakeside](local_feature) [home](real_estate_type) with a [dock](local_feature) for our boat
- no more than [$](currency)[100000](price)
- at least [1](number)
- i need some [modern coach](furniture)
- more than [3](number)
- in [Ho Chi Minh](city) city
- i need [metro](transportation) nearby to travel around
- i need local is a [quiet](house_description) area and [security](house_description)
- i think [1](number)
- [one](number:1) please
- The room i want has a [queen size bed](furniture) ideal for [2](num_person) persons
- You can get to the [city center](city) in [25 min](time_spent) by [metro](transportation)
- i think [three](number)
- there is must be a [free parking](local_feature)
- only [1](number) is okay
- no more than [$](currency)[1M](price)
- i need [2](number) only
- We have one [parking](local_feature) available, [5](time_spent) minutes to the[bus station](local_feature) and [10](time_spent) minutes to [the metro](local_feature)
- at most [2](number)
- This is a [residential neighborhood](house_description), [coffee shops](local_feature) and no [bars](local_feature)

## intent:house_request
- i need some information about houses in [hanoi](city) city
- I am interested in buying a [house](real_estate_type) and need some information.
- i need some information about [home](real_estate_type) in [hanoi](city) city
- give me some [houses](real_estate_type) for [4](num_person) persons
- give me the list of [apartment](real_estate_type) in [hcm](city)
- search me some [houses](real_estate_type) in [nhatrang](city) city
- would you mind give me some information about [apartment](real_estate_type) for sell?
- is there any [apartment](real_estate_type) less than [1 billion](price) [dollars](currency)?
- need [flat](real_estate_type) for sell
- I want to go [flat](real_estate_type) shopping
- I have been thinking of buying a [house](real_estate_type) and would like to speak with you.
- I'm interested in the [home](real_estate_type) in [Lang Son](city). What can you tell me about it?
- I am looking to buy a [house](real_estate_type) for myself and my son
- give me the list of [home](real_estate_type) in [hcm](city)
- Is there a [house](real_estate_type) in range [4 millions](price) [dollars](currency)?
- I would like to discuss purchasing a [home](real_estate_type) with you.
- give me some [apartment](real_estate_type) for [4](num_person) persons
- i want to buy a [flat](real_estate_type) for [4](num_person) persons
- search me some [houses](real_estate_type) no more than [1 million](price) in [nha trang](city) city
- I am looking to buy a [house](real_estate_type) for myself and my son
- I'm interested in the [houses](real_estate_type) in [Danang](city). What can you tell me about it?
- i would like to buy a [house](real_estate_type) in [DaNang](city)city with [1 billion](price) [vnd](currency)
- I would like to discuss purchasing a [home](real_estate_type) with you.
- Is there a [house](real_estate_type) in range [4 millions](price) [dollars](currency)?

## intent:thankyou
- Thanks for that
- Thanks bot
- thanks a bunch for everything

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
