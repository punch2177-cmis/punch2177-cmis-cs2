import random
def guess():
    number1 = int(raw_input("What is the minimun number?"))
    number2 = int(raw_input("What is the maximum number?"))
    random = random.randint(number1, number2)
    print "I am thinking of a number in between", number1, "to", number2
    think = int(raw_input("What do you think it is?: "))
    if think == random:
        return True
    else:
        return False

def template( 
       

