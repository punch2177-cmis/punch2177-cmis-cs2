
#while x > 0:
    #print x
   # x -= 1

def countdown(x):
    while x > 0:
        print x
        x -= 1

def counter(x):
    while x > 0:
        print x
        x -= 1
    while x < 1:
        print x
        x += 1

#counter(10)
#counter(-2)

def countfrom(x, y):
    while x > y:
        print x
        x -= 1
    while y >= x:
        print x
        x += 1

#countfrom(-1, 5)
#countfrom(5, 1)

def sumofOdds(n, total):
    while n > 0 and n % 2 != 0:
        return total + n
        n -= 1 
    while n > 0 and n % 2 == 0:
        return total + 0
        n -= 1
    while n < 0 and n % 2 != 0:
        return total + n
        n += 1
    while n < 0  and n % 2 == 0:
        return total + 0
        n += 1


def grid (w, h):
    out = ""
    while w >= 0:
        out += "."
        w -= 1
        while w == 0:
            print "\n"
            h -= 1
    print out

def main():
    grid( 10, 10)

main()

