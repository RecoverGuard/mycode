#!/usr/bin/env

astro= {"message": "success", "number": 5, "people": [{"craft": "ISS", "name": "Chris Cassidy"}, {"craft": "ISS", "name": "Anatoly Ivanishin"}, {"craft": "ISS", "name": "Ivan Vagner"}, {"craft": "ISS", "name": "Doug Hurley"}, {"craft": "ISS", "name": "Bob Behnken"}]}

print(f'People in space: {astro["number"]}')  
print()
for x in astro['people']:
    print(x['name'] + ' is on the ' + x['craft'])
