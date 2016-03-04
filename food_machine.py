#defined functions that are need for the program to work
def total_price(pricePerOne, amount, discountRate, taxRate):
    price = float(pricePerOne) * float(amount)
    rate = price * float(discountRate)
    discount = price - rate
    rate_2 = discount * float(taxRate)
    total = rate_2 + discount
    return total

def output(name, amount, food, costPerOne, total):
    cost = """
Welcome our valued customer, {}!
Today we have a promotion, 15% off your total price!
Also, just to inform you, our tax rate is 10%. 
Currently you are ordering {} {}(s), which costs ${} each.
Your total with tax and discount is ${}
Please pay at the counter infront. 
Thank you!
Please come again! :)
""".format(name, amount, food, costPerOne, total)
    return cost


#The main function includes all the functions define above and calls them so the program works
def main():
    name = raw_input("What is your name?")
    food = raw_input("What is the food you want right now?")
    amount = raw_input("Type how much of that food you want: ")
    costPerOne = 10.0
    tax_percent = 0.10
    discount_percent = 0.15
    
    total = total_price(float(amount), float(costPerOne), discount_percent, tax_percent)
    
    cost = output(name, amount, food, costPerOne, total)
    print cost


#calling main function
main()
