def focallength( R1, R2, d, n):
    "input radii R1 R2, thickness d, and refractive index n to return focal length"
  
    f = 1.0/((n - 1.0)*((1.0/R1)-(1.0/R2)+(((n-1.0)*d)/(n*R1*R2))))
    print 'Effective focal length f of a double sided convex lens: %.2f' % (f)
