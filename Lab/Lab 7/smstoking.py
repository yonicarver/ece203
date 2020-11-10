smstoking = {'gr8': 'great', 'btw': 'by the way', 'imho': 'in my humble opinion', 'jk': 'just kidding', 'l8r': 'later', 'np': 'no problem', 'r': 'are', 'u': 'you', 'y': 'why', 'ttyl': 'talk to you later', 'l8': 'late', 'atm': 'at the moment', 'lmk': 'let me know', 'np': 'no problem', 'tia': 'thanks in advance', 'brb': 'be right back'}

sms = str(raw_input('Enter message to translate: '))
smslist = sms.split(' ')

one = []

for item in smslist:
    if item[-1] not in '.?!,;:':
        one.append(smstoking[item])
    else:
        punct = item[-1]
        neww = smstoking[item.rstrip(punct)]
        var = neww + punct
        one.append(var)

joined = (' ').join(one)

print("Message in the King's English: %s" % joined)
