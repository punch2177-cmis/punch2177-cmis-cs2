
def countup(n):
    if n > 10:
        print "10"
    else:
        print n
        countup(n + 1)

def countup_2(start, stop):
    if start > stop:
        print "Done"
    else:
        print start
        countup_2(start + 1, stop)

def countdown(start, stop):
    if stop < start:
        print "Done"
    else:
        print stop
        countdown(start, stop - 1)

def adder(running_total):
    number = raw_input("Next number: ")
    if number == "":
        print "Running total: " + str(running_total)
    else: 
        total = running_total + float(number)
        print "Running total: " + str(total)
        adder(running_total + float(number))

def biggest(number):
    new = raw_input("Next: ")
    if new == "":
        print number
    elif float(new) > number:
        biggest(float(new))
    elif number > float(new):
        biggest(number)
    
def smallest(number):
    new = raw_input("Next: ")
    if new == "":
        print number
    elif float(new) < number:
        smallest(float(new))
    elif number < float(new):
        smallest(number)       
      
def pow(x, y):
    if x:
    else:
        print x * (x ** (n-1))
        


def main():
    running_total = 0
    number = 0
    number2 = float("inf")
    a = biggest(number)
    b = smallest(number2)
   


main()


          
            

