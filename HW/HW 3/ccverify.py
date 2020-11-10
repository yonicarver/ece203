print 'Enter an 8 digit credit card number > ',                     # display prompt for user input
ccnum = int(raw_input())                                            # assign variable 'ccnum' to user input number
string = str(ccnum)                                                 # convert user input to a string
everydigit = []                                                     # create an empty list
otherdigs = []                                                      # create an empty list

for digit in string:                                                # for every digit in string of 'ccnum'
    everydigit.append (int(digit))                                  # convert string to a list

rmd = int(sum(everydigit[::-2]))                                    # starting at the right most digit, sum of every other digit

d = everydigit[:-1:][::-2]                                          # list of digits not summed above

c = int(''.join(map(str, d)))                                       # convert string into one integer

for digit in str(c):                                                # for every digit in string of 'c'
    otherdigs.append (int(digit))                                   # convert string to a list

twoeveryother = int(sum(otherdigs[::1]))                            # sum of digits

check = int(rmd + twoeveryother)                                    # sum of (sum of right most digit) and (2 * sum of every other digit)

ones = str(check)[-1]                                               # find the value of the ones place of 'check'

if ones == '0':                                                     # if the ones place of 'check' is 0...
    print '%i is a VALID credit card number' % (ccnum)              # true, print this string
else:
    print '%i is NOT a valid credit card number' % (ccnum)          # false, print this string
