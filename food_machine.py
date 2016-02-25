#defined functions that are need for the program to work
def total_price(a, b, c, d):
    g = float(a) * float(b)
    h = g * float(c)
    i = g - h
    j = i * float(d)
    k = j + i
    return k

def output(name, x, food, y, b):
    cost = """
Welcome our valued customer, {}!
Today we have a promotion, 15% off your total price!
Also, just to inform you, our tax rate is 10%. 
Currently you are ordering {} {}(s), which costs ${} each.
Your total with tax and discount is ${}
Please pay at the counter infront. 
Thank you!
Please come again! :)
""".format(name, x, food, y, b)
    return cost


#The main function includes all the functions define above and calls them so the program works
def main():
    name = raw_input("What is your name?")
    food = raw_input("What is the food you want right now?")
    x = raw_input("Type how much of that food you want: ")
    y = 10.0
    tax_percent = 0.10
    discount_percent = 0.15
    
    b = total_price(float(x), float(y), discount_percent, tax_percent)
    
    cost = output(name,  x, food, y, b)
    print cost


#calling main function
main()
