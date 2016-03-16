#My script will determine how you will die, whether it is in the near furture or 30 years away. I will take in random information about the player and ask them to make desicions. There desicions will consequently tell them about how they die. First, they will be asked 

def yearsLeft():
    import random
    import math
    print "Hello, and welcome to the Death Guessing Game"
    age = float(raw_input("How old are you? "))
    favNumber = float(raw_input("What is your favorite number? "))
    calculation = (age + favNumber) * random.random
    if calculation > 100:
        return random.randint(0, 100)
    leftToLive = calculation + 2
    print leftToLive

   
yearsLeft()
