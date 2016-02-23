def mul( x, y):
    return x * y
def tax(a, b):
	int(a) * int(b) = c
    return c + a
def discount(w,z):
    100 * z = r
    return w - r
def output(name, x, food, y, a):
    cost = """
Welcome our valued customer, {}!
Currently you are ordering {} {}(s), which costs ${} each.
Today we have a promotion, 15% off each product!
Your total with tax and discount is ${}
Please pay at the counter infront. 
Thank you!
Please come again! :)
""".format(name, x, food, y, a)
    return cost

def main():
    name = raw_input("What is your name?")
    food = raw_input("What is the food you want right now?")
    x = raw_input("Type how much of that food you want: ")
    y = 10.0
    e = 0.05
    discount_percent = 0.15
    
    z = mul(int(x), int(y))
    b = discount(int(z), int(discount_percent))
    a = tax(int(b), int(e))
    
    cost = output(name,  x, food, y, a)
    print cost

main()
