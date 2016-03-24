#My script will determine how you will die, whether it is in the near furture or 30 years away. I will take in random information about the player and ask them to make desicions. There desicions will consequently tell them about how they die. First, they will be asked how old they are and what their favorite number is to determine how long they have left to live. The second question asks about their favorite vacation spot in order to help determine how they will die in the next function. The vacation spot will determine whether the how function will return true or false. If true is returned then they will die a peaceful death but if false is returned then they will die a painful death.  
import random
import math
def yearsLeft(age, favNumber):
    import random
    import math
    leftToLive = (age + favNumber) * int(random.random())
    if leftToLive > 100 or leftToLive < 0:
        return random.randint(0,100)
    finalResult = leftToLive + 2
    return finalResult

def vacation():
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

def enemy():
    enemies = raw_input("""
How many enemies do you think you have?
a. 1 or 2
b. I have a few but not that much 
c. I have a lot 
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

def determine():
    friend = raw_input("""
How many friends do you think you have?
a. Only imaginary ones
b. I have tons, you could say I'm the popular kid
c. I have a small group of tight-knit friends 
d. I have one really close best friend	
Answer (type a, b, c, or d):             
                        """)
    if friend == "a":
        return 1
    elif friend == "b":
        return 2
    elif friend == "c":
        return 3
    elif friend == "d": 
        return 4
    else:
        return random.randint(1,4)

def calculation(vacation, enemies):    
    add = enemies + vacation
    if add > 3 and add < 7:
        return 100
    elif not add != 8:
        return 50
    else:
        return 30
    return add

def how(calculation):
    determine = int(random.randint(1, 10))
    situation = calculation * determine - abs(determine - calculation)  
    counterSituation = calculation * random.random()
    if situation < counterSituation:
        return False
    else: 
        return True

def calculation2(friend):
    target = random.random()
    target2 = random.random()
    result = friend * target
    counterResult = friend * target2
    if result > counterResult:
        return True
    else:
        return False 

def death(years, how, calculation2):
    if how and calculation2:
        return """
You will die in {} years. You will die while you are asleep. Congratulations, it will be a peaceful death.
            """.format(years)
    elif how or calculation2:
        return """
Surprise! You are actually immortal and can live as long as possible without aging. This could be a blessing and a curse.
"""
    else:
        return """
You will die in {} years. There will be a devastating car crash that will ultimately result in your death. Sorry, it will be a painful death.
            """.format(years)

def main():
    print "Hello, and welcome to the Death Guessing Game"
    age = (raw_input("How old are you? "))
    favNumber = (raw_input("What is your favorite number? "))

    numberOfYears = yearsLeft(age, favNumber)
    location = vacation()
    numberOfEnemies = enemy()
    calc = calculation(location, numberOfEnemies)   
    situation = how(calc)
    anotherQuestion = determine()
    anotherCalculation = calculation2(anotherQuestion)

    output = death(numberOfYears, situation, anotherCalculation)

    print output

main()
        
