def guess(random, tries):
    think = int(raw_input("What do you think it is?: "))
    if tries == 0:
        print "You are not good at this game"
        return float(0)
    elif think > random:
        print "You are too high"
        guess(random, tries-1)
        return 0
    elif think < random:
    	print "You are too low"
        guess(random, tries-1)
        return 0
    elif think == random:
        print "You are correct"
        return 1

def rounds(tries, numberofRounds, correct):
    import random
    random = random.randint(0,100) 
    print "I am thinking of a number between 0 and 100"  
    if numberofRounds == 0:
        print correct
    elif numberofRounds != 0:
        round1 = guess(random, tries)
        total1 = float(correct) + float(round1)
        print "\nYou have " + str(numberofRounds - 1) + " rounds left\n"
        rounds(tries, numberofRounds - 1, total1)


def main():
    import random
    tries = 4
    numberofRounds = 3
    correct = 0
    a = rounds(tries, numberofRounds, correct)

main()
