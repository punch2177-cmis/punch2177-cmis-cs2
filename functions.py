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
    volume_1 = (circle_area(a-(1.0/2 * a)))
    volume_2 = (circle_area(b-(1.0/2 * b)))
    return volume_1 + volume_2 /2
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
a = add(3,3)

x = sub(3,2)
b = sub(4,2)

y = mul(4,4)
c = mul(5,4)

t = div(2,3)
d = div(9,3)

u = hours_from_seconds(86400)
e = hours_from_seconds(3600)

f = circle_area(5)
q = circle_area(7)

h = sphere_volume(5)
o = sphere_volume(9)

i = avg_volume(10,20)
v = avg_volume(19,20)

k = area(1,2,2.5)
n = area(2,2,2.5)

l = right_align("Hello")
s = right_align("Hi")

hi = center("Hello") 
hi_2 = center("Hi") 

message = msg_box("Hello")
message_2 = msg_box ("I eat cats!")

print msg_box(str(w))
print msg_box(str(a))
print msg_box(str(x))
print msg_box(str(b))
print msg_box(str(y))
print msg_box(str(c))
print msg_box(str(t))
print msg_box(str(d))
print msg_box(str(u))
print msg_box(str(e))
print msg_box(str(f))
print msg_box(str(q))
print msg_box(str(h))
print msg_box(str(o))
print msg_box(str(i))
print msg_box(str(v))
print msg_box(str(k))
print msg_box(str(n))
print msg_box(str(l))
print msg_box(str(s))
print msg_box(str(hi))
print msg_box(str(hi_2))
print message
print message_2
