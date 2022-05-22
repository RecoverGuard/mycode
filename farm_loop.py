#!/usr/bing/env

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

zero = '0'
for x in zero:
    print(*farms[0]["agriculture"])

    #########################

user_input = input('Please select a farm (NE Farm, W Farm, or SE Farm: ')

if user_input == 'NE Farm':
    print('here at NE Farm, we have:')
    print(*farms[0]['agriculture'])

elif user_input == 'W Farm':
    print('Here at W Farm, we have:')
    print(*farms[1]['agriculture'])

elif user_input == 'SE Farm':
    print('Here at SE Farm, we have:')
    print(*farms[2]['agriculture'][0])

#add [0] after the agriculture to return just animals for farm 3

else:
    print('That is not a farm')
