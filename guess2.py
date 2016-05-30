def guess(random, tries):
    think = int(raw_input("What do you think it is?: "))
    if tries == 0:
        print "You are not good at this game"
        return float(0)
    elif think > random:
        print "You are too high"
        guess(random, tries-1)
        return float(0)
    elif think < random:
    	print "You are too low"
        guess(random, tries-1)
        return float(0)
    elif think == random:
        print "You are correct"
        return float(1)

def rounds(tries, numberofRounds, correct):
    import random
    random = random.randint(0,100) 
    if numberofRounds == 0:
        print correct
    elif numberofRounds != 0:
        print "I am thinking of a number between 0 and 100" 
        round1 = guess(random, tries)
        total1 = correct + round1
        print "\nYou have " + str(numberofRounds - 1) + " rounds left\n"
        rounds(tries, numberofRounds - 1, total1)

def bonus(computer, tries, highest, lowest):
    if tries == 0:
        print "The computer is not good at this game"
        return float(0)
    print "The computer thinks it is ", computer
    correct = raw_input("""
If it is too low, type "Low"
If it is too high, type "High"
If it is correct, type "Correct"
""")
    if correct == "High":
        bonus((computer + ((computer - highest)/2)), tries - 1, computer, lowest)
        return float(0)
    elif correct == "Low":
        bonus(((highest-computer)/2) + computer, tries - 1, highest, computer)
        return float(0)
    elif correct == "Correct":
        print "You are correct"
        return float(1)
    
def bonus_rounds(tries, numberofRounds, correct):
    import random
    computer = 50   
    if numberofRounds == 0:
        print correct
    elif numberofRounds != 0:
        user = int(raw_input("Pick a number from 0 to 100: "))
        highest = 100
        lowest = 0
        rounds = bonus(computer, tries, highest, lowest)
        total1 = correct + rounds
        print "\nYou have " + str(numberofRounds - 1) + " rounds left\n"
        bonus_rounds(tries, numberofRounds - 1, total1)    

def main():
    import random
    tries = 4
    numberofRounds = 3
    correct = 0
    computer = random.randint(0,100)
    a = rounds(tries, numberofRounds, correct)
    b = bonus_rounds(tries, numberofRounds, correct)

main()
