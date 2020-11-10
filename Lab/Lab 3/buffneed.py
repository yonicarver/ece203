from random import random
from math import pi, sin

hits = float(0)
miss = 0

print 'Enter a number of attempts >',
ran = int(raw_input())

for item in range(1, ran+1):
    yhead = (2.0*random()) + sin(pi*random())

    if yhead >= 2.0:
        hits = hits + 1
    else:
        miss = miss + 1

ratio = float(ran/hits)
print'''
    ratio: %g
    %g      %g
''' % (ratio, hits, ran)
