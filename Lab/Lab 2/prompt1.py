M = 1000
n = 5
p = .95

interest = M*(1.0+(p/100.0))**n
print 'The amount of interest acquired with an initial amount of $%d and %.2f percent APR after %d years is $%.2f' % (M, p, n, interest)
