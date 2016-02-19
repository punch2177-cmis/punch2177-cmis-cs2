def mul( x, y):
    return x * y
def output(name, x, food, y, z):
    cost = """
Welcome our valued customer, {}!
Currently you are ordering {} {}(s), which costs ${} each.
Your total is ${}
Thank you!
Please come again! :)
""".format(name, x, food, y, z)
    return cost

def main():
    name = raw_input("What is your name?")
    food = raw_input("What is the food you want right now?")
    x = raw_input("Type how much of that food you want: ")
    y = 10.0
    
    z = mul(int(x), int(y))
    
    cost = output(name,  x, food, y, z)
    print cost

main()
