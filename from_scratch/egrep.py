import sys, re

# sys.argv is the list of command-line arguments
# sys.argv[0] is the list of the program itself
# sys.argv[1] will be the regex specified at the command line
regex = sys. argv[1]

# for every line passed into the script
for line in sys.stdin:
    #if it matches the regex, write it to stdout
    if re.search(regex, line):
        sys.stdout.write(line)
