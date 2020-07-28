#!/usr/bin/env python3

movies = {'1' : 'Harry Potter', '2' : 'Guns Akimbo', '3' : 'The Lord of the Rings', '4' : 'Thor Ragnarok', '5' : 'The Interview'}
message = 'Bad synopsis: '

print('You will choose from some of my favorite movies to reveal a title and terrible synopsis!')
synop = movies.get(input('Please select a number from 1-5 to reveal magic: '))

if synop == movies.get('1'):
    message = message + 'loser kid is convinced by giant bearded man that he can do magic and gets kidnapped. Can actually do magic.'
    print('You chose: Harry Potter')
elif synop == movies.get('2'):
    message = message + 'Harry Potter trolls online, gets pistols bolted to his hands, and now has to fight gun-toting cokehead.'
    print('You chose: Guns Akimbo')
elif synop == movies.get('3'):
    message = message + 'Small man with huge feet goes on an adventure to Mordor. One does not simply walk into Mordor. But he does, and yeets a ring and a schizophrenic man into a volcano.'
    print('You chose: The Lord of the Rings')
elif synop == movies.get('4'):
    message = message + 'God of Thunder gets mollywhopped by his sister then amasses an army to take her down because he is sad she broke his hammer. Gets his eye slapped out of his head. Still takes an L'
    print('You chose: Thor Ragnarok')
elif synop == movies.get('5'):
    message = message + 'Mediocre talk show host lands an interview with Kim Jong-un. Gets played. Blows him up with a tank.'
    print('You chose: The Interview')
else:
    message = message + 'Error: That entry is not in our database.'
    print('synopsis not found')

print(message)
