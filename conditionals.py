#My script will determine how you will die, whether it is in the near furture or 30 years away. I will take in random information about the player and ask them to make desicions. There desicions will consequently tell them about how they die. First, they will be asked 
import random
import math
def yearsLeft():
    import random
    import math
    print "Hello, and welcome to the Death Guessing Game"
    age = float(raw_input("How old are you? "))
    favNumber = float(raw_input("What is your favorite number? "))
    leftToLive = (age + favNumber) * random.random()
    if leftToLive > 100:
        return random.randint(0,100)

def question():
    vacation = raw_input("""
What is your favorite vacation spot?
a. Paris
b. Maldives
c. Iceland
d. Home
Answer (type a, b, c, or d):             
                        """)
    if vacation == "a":
        return 1
    elif vacation == "b":
        return 2
    elif vacation == "c":
        return 3
    elif vacation == "d":
        return 4
    else:
        return random.randint(1, 4)
    
   
def how(vacation):
    determine = random.random()
    situation = vacation * determine - abs(vacation - determine) 
    counterSituation = vacation * random.random()
    if situation > counterSituation:
        return True
    else: 
        return False


def death(years, vacation, how):
    
