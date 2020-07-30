#!/usr/bin/env python3
## create file object in "r"ead mode

user_input = input('Please specify a name for your file: ')
count = 0
with open("/home/student/mycode/cfgread/"  + user_input, "w") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

    for lines in configlist:
        count += 1

print(count)

## file was just auto closed (no more indenting)

## display list with no "\n"
print(configlist)

