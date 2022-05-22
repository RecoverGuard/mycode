#!/usr/bin/env python3
#this challenge is to create a calculator



def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x-y

def divide(x, y):
    return x / y

cont = 'yes'

while cont == 'yes' or cont == 'Yes':
    print("Welcome to 'MY CALCULATOR LITE'!")
    x = float(input("please select your first integer: "))
    y = float(input("Please select a second integer: "))
    operator = input("please select an operator(+, -, /, *): ")



    if operator == '+':
        print(f"Your answer is: {x + y}.")
    elif operator == '-':
        print(f"Your answer is: {x - y}.")
    elif operator == '*':
        print(f"Your answer is: {x * y}.")
    elif operator == '/':
        print(f"Your answer is: {x / y}.")
    else:
        print("That is not a valid entry. Please try again")
    a = input("Do you have more math you need doing? Y/N: ")
    if a == "Y".lower():
        cont = "yes"
    else:
        print("GOOD-BYE")
        break
