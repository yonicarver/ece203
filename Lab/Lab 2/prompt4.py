a = 3
b = 5
a2 = int(a)**2
b2 = int(b)**2

eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2

eq1_pow = (a + b)**2
eq2_pow = (a - b)**2

print '1st equation: %.2f = %.2f' % (eq1_sum, eq1_pow)
print '2nd equation: %.2f = %.2f' % (eq2_sum, eq2_pow)

