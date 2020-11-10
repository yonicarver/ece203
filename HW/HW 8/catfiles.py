from sys import argv

if len(argv) < 3:
    exit('error -- must supply at least one input file and an output file')

filenames = []
for param in argv[1:-1]:
    filenames.append(str(param))

# concat files: argv[1:-1]
#run file: argv[0]
#output file: argv[-1]

with open(argv[-1],'w') as outfile:
    for chapter in filenames:
        with open(chapter) as infile:
            for line in infile:
                outfile.write(line)


