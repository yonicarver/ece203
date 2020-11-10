
print 'Please enter a value for M >',                           # Print instructions for user input
M = float(raw_input())                                          # assign variable 'M' to hold user input number

sum = 0                                                         # begin sum at 0

for k in range(1, int(M+1)):                                    # for a value of 'k' in range of 1 to value of 'M' -- range does not include end bound, so add 1 here
    sum = sum + (1.0/k)                                         # sum is equal to previous value of sum and 1/k

print 'Summation of 1/k from 1 to %i is %.4f' % (M, sum)        # print results in a pretty format (print value of sum to 4 decimal points)
