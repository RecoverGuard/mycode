import random

def mainfun():   
    x= float(input("How would you rank your day today on a scale of 1-10?"))
    if x == 10:
        print("Attaboy! Stay positive!")
    elif x >= 8:
        print("Sounds lovely! Keep on truckin'!")
    elif x >= 6:
        print("Chin up, buttercup!")                    
    elif x >= 4:            
        print("I recommend some hot chocolate and a hug, maybe...")               
    elif x >= 2:
        print("Dude, are you ok?")                   
    else:
        print("Geez!!! You might as well just go back to bed!")

mainfun()

# Part 2
adj1 = input("Choose an adjective: ")
adj2 = input("Choose another adjective: ")

def python_props(x, y):
    print(f"Python is {x} and {y}!")

python_props(adj1, adj2)


# Part 3

meme = input("What phrase would you like to meme today? ")
new_meme = []
x = 0

#for x in meme:
 #   case = random.randint(0,1)
  #  print("case= ", case)
   # if case == 0:
     #   print("here0")
    #new_meme += meme[x].lower() # append to the list
   # else:
     #   print("here1")
     #   new_meme += meme[x].upper() # append to the list
    #x += 1
    #print ("new meme = ", new_meme)

# to print as string
   # new_sent = ''.join(new_meme)
    #print(new_sent)
