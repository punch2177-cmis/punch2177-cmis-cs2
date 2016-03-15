
def guess():
    import random
    number1 = int(raw_input("What is the minimun number?"))
    number2 = int(raw_input("What is the maximum number?"))
    random = random.randint(number1, number2)
    print "I am thinking of a number in between", number1, "to", number2
    think = int(raw_input("What do you think it is?: "))
    if think == random:
        print  """
The target was {}
Your guess was {}
You are correct. You must be psychic!
""".format(random, think)
    elif think > random:
        difference = think - random
        print """
The target was {}
Your guess was {}
You are over by {}
""".format(random, think, difference)
    else:
        difference = random - think
    print """
The target was {}
Your guess was {}
You are under by {}
""".format(random, think, difference)
       
guess()

