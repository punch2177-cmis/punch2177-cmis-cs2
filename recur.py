
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

def adder():
    running_total = 0
    print "Running total = 0"
    number = raw_input("Next number: ")
    if number == "":
        print "Running total: " + running_total
    else: 
        total = running_total += float(number)
        print total
        adder()
      

def main():
     smth = adder()

main()


          
            

