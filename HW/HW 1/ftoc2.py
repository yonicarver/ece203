print "Fahrenheit    Celcius    Celcius (approximation)    Error"                                               # print headers for columns


for F in range(0, 110, 10):                                                                                     # range 0 to 110 (non inclusive) with step size of 10
    C = (5.0/9)*(F-32)                                                                                          # conversion formula from Celcius to Fahrenheit
    C_approx = (1.0/2)*(F-30)                                                                                   # approximate conversion formulia from Celcius to Fahrenheit
    error_approx = C_approx - C
    conversion = "%.2f          %.2f          %.2f              %.2f" % (F, C, C_approx, error_approx)          # assign variable for conversions (spaces for formatting)
    print conversion                                                                                            # print conversions
            
            
         
