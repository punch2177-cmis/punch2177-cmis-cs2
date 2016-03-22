#My script will determine how you will die, whether it is in the near furture or 30 years away. I will take in random information about the player and ask them to make desicions. There desicions will consequently tell them about how they die. First, they will be asked how old they are and what their favorite number is to determine how long they have left to live. The second question asks about their favorite vacation spot in order to help determine how they will die in the next function. The vacation spot will determine whether the how function will return true or false. If true is returned then they will die a peaceful death but if false is returned then they will die a painful death.  
import random
import math
def yearsLeft():
    import random
    import math
    print "Hello, and welcome to the Death Guessing Game"
    age = (raw_input("How old are you? "))
    favNumber = (raw_input("What is your favorite number? "))
    leftToLive = (age + favNumber) * int(random.random())
    if leftToLive > 100 or leftToLive < 0:
        return random.randint(0,100)
    finalResult = leftToLive + 2
    return finalResult

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

   enemies = raw_input("""
How many enemies do you think you have?
a. 1 or 2
b. quite a few but not that much
c. I have a lot of enemies
d. None at all
Answer (type a, b, c, or d): 
                        """)
    if enemies == "a":
        return 1
    elif enemies == "b":
        return 2
    elif enemies == "c":
        return 3
    elif enemies == "d":
        return 4
    else:
        return random.randint(1, 4)
    
    add = enemies + vacation
    if add > 3 and add < 7
        return 100
    elif not add != 8:
        return 50
    else:
        return 30
    return add

def how(question):
    determine = int(random.randint(1, 10))
    situation = question * determine - abs(determine - question)  
    counterSituation = question * int(random.random())
    if situation < counterSituation:
        return False
    else: 
        return True


def death(years, how):
    if how == True:
        return """
You will die in {} years. You will die while you are asleep. Congratulations, it will be a peaceful death.
            """.format(years)
    else:
        return """
You will die in {} years. There will be a devastating car crash that will ultimately results in your death. Sorry, it will be a painful death.
            """.format(years)

def main():
    numberOfYears = yearsLeft()
    
    location = question()
    
    situation = how(location)

    output = death(numberOfYears, situation)

    print output

main()
        
