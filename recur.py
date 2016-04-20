

def countup(n):
    if n >= 10:
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
          
            
        
def main():
    number = countup_2(-89,2)

main()

