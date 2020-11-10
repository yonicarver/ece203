def scramble( word ):
    "flip two letters in a word (not first or last letter)"
    import random

    length = len(word)
    lengt = length - 1
    wlist = list(word)
    
    
    if length >=4:
        randomnum1 = int(random.randrange(1,lengt,1))
        randomnum2 = int(random.randrange(1, lengt,1))
        wlist[randomnum1], wlist[randomnum2] = wlist[randomnum2], wlist[randomnum1]
        print ''.join(wlist)
        
