
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

def sumofOdds(n):
    total = 0
    while n > 0:
        if n % 2 !=0:
            total += n 
        n -= 1
    while n < 0:
        if n % 2 != 0:
            return total + n
        else:
            return 0
        n += 1

print sumofOdds(5)


