#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
# the symbol "=" is called the assignment operator 
# it is used to put a value into a variable
#
#2 3pts) Write a technical definition for 'function'
# a function is a named sequence of statements that performs a computation
#
#
#3 1pt) What does the keyword "return" do?
# the keyword "return" gives the output from the function
#
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: Boolean ex. True, False
#	2: Integer ex. 3, 4
#	3: Float ex. 1.3, 2.3
#	4: String ex. "Hello", "Hi"
#	5: Tuple ex. ("Hi", "Hello") , (3, "Cats")
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
# A function definition specifies the name of a new function and the sequence of statements that execute when the function is called.
# However, a function call is an expression that passes control and arguments to a function.
#
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1:Input: In this phase the computer program accepts data and instructions
#	2:Processing: The calculating happens here, this is where most of the work takes place
#	3:Output: It gives you the result of the computer program
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi
import math 
def area_diameter(x): 
    radius = math.sqrt(x/ math.pi)
    return radius * 2

def output(d1, d2, d3, total):
    out = """
Circle  Diameter
c1      {}
c2      {}
c3      {}
Totals  {}
""".format(d1, d2, d3, total)
    return out

def main():

    C1 = raw_input("Area of C1: ")
    C2 = raw_input("Area of C2: ")
    C3 = raw_input("Area of C3: ")
    
    d1 = area_diameter(float(C1))
    d2 = area_diameter(float(C2))
    d3 = area_diameter(float(C3))
    total = d1 + d2 + d3
    
    out = output(d1, d2, d3, total)
    print out

main()

