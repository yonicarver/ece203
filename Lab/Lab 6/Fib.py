end = int(raw_input('input an end > ') or 20)

a = 1
b = 1
fib_numbers = [a]

for item in xrange(1,end+1):
    fib_numbers.append(a)
    a,b = b, a + b

print fib_numbers
