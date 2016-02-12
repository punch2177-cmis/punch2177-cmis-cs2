def add(a,b):
	return a+b
def sub(c,d):
    return c-d
def mul(e,f):
    return e*f
def div(g,h):
	return g/h
def hours_from_seconds(seconds):
    return seconds / 3600
import math
def circle_area(radius):
    return math.pi * radius**2
def sphere_volume(radius):
    return 4.0/3 * math.pi * radius **3
def avg_volume(a, b):
    return ((1.0/6 * math.pi * a**3) + (1.0/6 * math.pi * b**3)) / 2
def area(a, b, c):
    s = (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c)) ** 0.5
def right_align(word):
	return str((80 - len(word))*" " + word)
def center(word):
	return str((40 - len(word))*" "+word) 
def msg_box(word):  
	return "+" + ((len(word) + 4)*"-") + "+" + '\n' + "|" + (2*" ") + word + (2*" ") + "|" + '\n' + "+" + ((len(word) + 4)*"-") + "+"
w = add(2,3)
print w
w = add(2,3)
print w
x = sub(3,2)
print x
x = sub(3,2)
print x
y = mul(4,4)
print y
y = mul(4,4)
print y
t = div(2,3)
print t
t = div(2,3)
print t
u = hours_from_seconds(86400)
print u
u = hours_from_seconds(86400)
print u
f = circle_area(5)
print f
f = circle_area(5)
print f
h = sphere_volume(5)
print h
h = sphere_volume(5)
print h
i = avg_volume(10,20)
print i
i = avg_volume(10,20)
print i
k = area(1,2,2.5)
print k
k = area(1,2,2.5)
print k
l = right_align("Hello")
print l
l = right_align("Hello")
print l
hi = center("Hello") 
print hi
hi = center("Hello") 
print hi
message = msg_box("Hello")
print message
message_2 = msg_box ("I eat cats!")
print message_2
