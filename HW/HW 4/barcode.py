zip = int(raw_input('Please enter a 5 digit zip code > ') or 95014)         # user input: zip code -or- test zip code

def printDigit( dig ):                                                      # define function printDigit
    "input: single digit between 0&9, output: cluster of '.' and '!' "
    
    bars = []                                                               # placeholder for individual bars
    
    # 'if statements' depending on input 'dig', set bars placeholder to corresponding barcode
    if dig == 1:
        bars = '...!!'
    elif dig == 2:
        bars = '..!!.'
    elif dig == 3:    
        bars = '..!!.'
    elif dig == 4:    
        bars = '.!..!'
    elif dig == 5:    
        bars = '.!.!.'
    elif dig == 6:    
        bars = '.!!..'
    elif dig == 7:    
        bars = '!...!'
    elif dig == 8:    
        bars = '!..!.'
    elif dig == 9:    
        bars = '!.!..'
    else:    
        bars = '!!...'
    
    return bars                                                             # return barcode for specific number

def printBarCode( zip ):                                                            # define function printBarCode
    "input: 5 digit zip code, output: full bar code (5+1) cluster with frame bars"
    szip = str(zip)                                                                 # convert input zip to string
    lzip = []                                                                       # placeholder for list zip
    
    for digit in szip:                                                              # for every digit in string of zip
        lzip.append(int(digit))                                                     # add integer value of string to placeholder for list zip
    
    sumzip = sum(lzip)                                                              # sum all integers in list zip
    checkdig = 10 - (int(str(sumzip)[-1::]))                                        # find checkdigit by subtracting sum from 10
    if checkdig == 10:                                                              # if checkdigit == 10
        checkdig = printDigit(0)                                                    # set value of checkdig == barcode of '0'
    
    zstr = []                                                                       # placeholder for zip string
    
    for item in lzip:                                                               # for every item in list zip
        zstr += printDigit(item) + ' '                                              # add barcode value and space to placeholder zip string
    
    zipbar = "!" + ''.join(zstr) + " " + printDigit(checkdig) + "!"                 # format final barcode with frame bars, spaces, and check digit
    
    return zipbar                                                                   # return value of zipbar


def main():                             # define function main
    print printBarCode(zip)             # print final value of zip code barcode
if __name__ == "__main__":
    main()


