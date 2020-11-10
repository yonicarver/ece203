import logging
logging.basicConfig(filename = 'missing_words.log', level = logging.INFO)

words = open('/usr/share/dict/words','r')
words = words.read().split()

mispell = open('mispell.txt','r')
mispell = mispell.read().replace('\n',' ').replace(',',' ').replace(';',' ').replace('-',' ').replace('.',' ').replace("'"," ").split()

inwords = []
notinwords = []

for x in mispell:
    if x in words:
        inwords.append(x)
    else:
        notinwords.append(x)
        
notin = []
for item in notinwords:
    logging.info('%s\n'%item)
