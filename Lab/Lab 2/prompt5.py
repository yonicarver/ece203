import math

a = 7
b = 26
c = 3

q = math.sqrt(b*b - 4*a*c)

x1 = (-b+q)/2*a
x2 = (-b-q)/2*a

print """
x1 = %.2f
x2 = %.2f
""" % (x1, x2)
