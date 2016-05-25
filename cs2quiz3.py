#Section 1: Terminology
# 1) What is a recursive function?
#A recursive function is a funcation that calls itself within the function
#
# 1 pt
# 2) What happens if there is no base case defined in a recursive function?
#The recursive function will keep calling itself and there will be an error.
#
#
# 3) What is the first thing to consider when designing a recursive function?
#The base case
#
#
# 4) How do we put data into a function call?
#You assign it in a variable
# wrong
# 
# 5) How do we get data out of a function call?
#You return or print the data
#
# 1 point

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables a1-d3.

#a1 = 6
#a2 = 8
#a3 = -1
# 2 points
#b1 = 2
#b2 = 1
#b3 = 3
# 1 point
#c1 = -2
#c2 = 4
#c3 = 45
#3 points
#d1 = -4 (wrong)
#d2 = 8
#d3 = -4
# 1 point
#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.


# +2 base case is present (MUST BE LABELED) 2 points
# +2 recursive case is present (MUST BE LABELED) 2 points
# +1 base case returns sum/ct (or equivalent) 0 points
# +2 recursive case filters even numbers 2 points
# +1 recursive case increments sum and ct correctly 1 point
# +1 recursive case returns correct recursive call 0 point
# +1 main function present AND called 1 point

def average(total, amount):
    number = raw_input("Next number: ")
#Base case
    if number == "" and amount != 0 and total != 0:
        print amount/total
    elif number == "" and amount == 0 and total == 0:
        print " "
#Recursive case
    elif float(number) % 2 == 0:
        average(total, amount)
#Recursive case
    else: 
        average(total + 1, amount + float(number))


def main():
    total = 0
    amount = 0
    average(total, amount)

main()

