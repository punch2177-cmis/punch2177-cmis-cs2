#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a)>
#b)<
#c)==
#
#2) What does 'return' do?
#it gives you the output from the function
#
#
#
#3) What are 2 ways indentation is important in python code?
#a)It tells you when the function ends
#b)It tells you what is part of a function
#
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a)math pow of 5 and 2, and then multiply the result of that by negative 1
#problem1_b)square root of 3 multiplied by -1
#problem1_c)0
#problem1_d)-5
#
#problem2_a)True
#problem2_b)False
#problem2_c)False
#problem2_d)False
#
#problem3_a)0.3
#problem3_b)0.5
#problem3_c)0.5
#problem3_d)0.25
#
#problem4_a)24
#problem4_b)5
#problem4_c)1.25
#problem4_d)5
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)

#defing functions that are used in main
#function determines if numbers are the same or not
def different(a, b, c):
    if a != b and b!= c and a != c:
        return True
    else:
        return False

#function determines which number is the greatest
#and gives the output as well
def calculate(a, b, c):
    if a > b and a > c:
        print """
The largest number was {}
""".format(a)
    elif b > a and b > c:
        print """
The largest number was {}
""".format(b)
    elif c > a and c > b:
        print """
The largest number was {}
""".format(c)
   
#main function where function from above are called            
def main():

#taking in input from user
    print "Type in 3 different numbers (decimals are OK): "
    a = float(raw_input("A: "))
    b = float(raw_input("B: "))
    c = float(raw_input("C: "))

#processing to see if numbers are the same and which one is the greatest
    determineDifferent = different(a, b, c)
    if determineDifferent == False:
        print "You didn't follow directions"
#calling output function
    elif determineDifferent ==True:
        result = calculate(a, b, c)

#calling main    
main()
    
    
