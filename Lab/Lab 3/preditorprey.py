import math

print 'Enter the rate at which prey birth exceeds natural death >', 
defaultA = 0.1
A = float(raw_input() or defaultA)

print 'Enter the rate of predation >',
defaultB = 0.01
B = float(raw_input() or defaultB)

print 'Enter the rate at which predator deaths exceeds births without food >',
defaultC = 0.01
C = float(raw_input() or defaultC)

print 'Enter the predator increase in the presence of food >',
defaultD = 0.00009
D = float(raw_input() or defaultD)

print 'Enter the initial population size >',
defaultprey = 1000
preyt = float(raw_input() or defaultprey)

print 'Enter the initial predator size >',
defaultpred = 20
predt = float(raw_input() or defaultpred)

print 'Enter the years to simulate >',
defaultyear = 30
y = int(raw_input() or defaultyear)

oldprey = preyt
oldpred = predt

for item in range(y + 1):
    preyt = preyt * (1 + A - B * oldpred)
    predt = predt * (1 - C + D * oldprey)
    oldprey = preyt
    oldpred = predt
    print 'The population of prey is %i' % (preyt)
    print 'The population of predators is %i' % (predt)
