#My script will determine how you will die, whether it is in the near furture or 30 years away. I will take in random information about the player and ask them to make desicions. There desicions will consequently tell them about how they die. First, they will be asked how old they are and what their favorite number is to determine how long they have left to live. The second question asks about their favorite vacation spot in order to help determine how they will die in the next function. The second question is to determine how many enemies they have. The vacation spot and the number of enemies will determine whether the "how" function will return True or False. The next questions asks what they like to do on the weekends and how many friends they think they have. The value from the two functions will be used in the "calculation2" function and it will either return true or false. If true is returned in both the "how" and the "calculation2" function, then they will die a peaceful death. If, however, both of the fuctions return false then they will die a painful death. Another option is if at least one of the functions return true, then it will tell them that they are actually immortal.  
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

def weekend():
    hobby = raw_input("""
Which of these would you most likely be doing over the weekends?
a. Playing videogames
b. Watching TV
c. Playing sports
d. Reading
Answer (type a, b, c, or d):             
                        """)
    if hobby == "a":
        return 1
    elif hobby == "b":
        return 2
    elif hobby == "c":
        return 3
    elif hobby == "d":
        return 4
    else:
        return random.randint(1, 4)

def friendQuestion():
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
    determine = random.randint(1,10)
    situation = (calculation * determine) - abs(calculation - determine)    
    counterSituation = calculation * random.random()
    if situation > counterSituation:
        return True
    else: 
        return False

def calculation2(friend, hobby):
    target = random.random()
    target2 = random.random()
    result = (friend * target) - hobby
    counterResult = (friend * target2) - hobby
    if result > counterResult:
        return True
    else:
        return False 

def death(years, how, calculation2):
    if how and calculation2:
        return """
You will die in {} years. You will die while you are asleep. Congratulations, it will be a peaceful death.
            """.format(years)
    elif how and calculation2 == False:
        return """
You will die in {} years. There will be a devastating car crash that will ultimately result in your death. Sorry, it will be a painful death.
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
    Friends = friendQuestion()
    freeTime = weekend()

    calc = calculation(location, numberOfEnemies)   
    determine = how(calc)
    anotherCalculation = calculation2(Friends, freeTime)

    output = death(numberOfYears, determine, anotherCalculation)

    print output

main()
        
