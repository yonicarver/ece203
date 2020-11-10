def build_sentence( sentence ):
    "input: string containing entire sentence, output: scrambled words in a sentence"
    
    from scramble import scramble
    
    split = sentence.split()
    
    empty = ''
    
    for word in split:
        str(scramble(word))
        #empty = empty + ' ' + word
        #print(' '.join(empty))

sentence = str(raw_input() or 'helloworld this is a test')
build_sentence( sentence )
