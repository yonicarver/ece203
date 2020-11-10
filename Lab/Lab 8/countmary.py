mary = open('mary.txt','r')
mary = mary.read().replace('\n',' ').replace(',',' ').replace('.',' ').replace('?',' ').replace('"',' ')

mary = mary.split()

count = {}

for word in mary:
    if len(word) >=1 and not count.get(word):
        count[word] = mary.count(word)
for x,y in count.items():
    print('%s: %s') %(x,y)    

