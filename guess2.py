def guess(random, tries):
    think = int(raw_input("What do you think it is?: "))
    if think == random:
        print  """
You are correct. You must be psychic!
"""
    elif think > random:
        print "You are too high"
        guess(random, tries-1)
    elif think < random:
    	print "You are too low"
        guess(random, tries-1)
       
def main():
    import random
    random = random.randint(0, 100)
    tries = 5
    a = guess(random, tries)

main()
