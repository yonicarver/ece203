print "Fahrenheit    Celcius"                           # print headers for columns


for F in range(0, 110, 10):                             # range 0 to 110 (non inclusive) with step size of 10
    C = (5.0/9)*(F-32)                                  # conversion formula from Celcius to Fahrenheit
    conversion = "%.2f          %.2f" % (F, C)          # assign variable for conversions (spaces for formatting)
    print conversion                                    # print conversions


