# In order for this code to work poroperly, you must create a separate file for the range of insults you would like to be generated.
# Steps: uncomment line 8 then Plug your file path into line 8.
#!/usr/bin/env python3

import random

num = int(input("How many Shakespearean insults would you like? "))

#insult_list = open("*FILE PATH*", "r")
insult = insult_list.readlines()


def insult_generator(num):
    print("you are a ", end=" ")
    for x in range(num):
        print(random.choice(insult), end="") 
      

insult_generator(num)
