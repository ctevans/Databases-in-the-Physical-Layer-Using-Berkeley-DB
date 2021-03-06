import sys

# Given files with the current format that we do already have them in
# We must now make it so that we have the given files turned into 
# the format that the db_load command actually does like! And so that all
# being said... we're going to have it so that this file takes in a file and
# then splits each line by the first comma.
#
# db_load expects the following sort of format:
# 1: FIRST LINE MUST BE KEY
# 2: SECOND LINE MUST BE DATA

#open the file that is given to python
line  = True


outputFile = open(sys.argv[2], 'w')
inputFile = open(sys.argv[1], 'r')

while line:
    line = inputFile.readline()
    line.strip('\n') 
    splittingFunction = line.split(",",1)

    if splittingFunction[0].strip() != "" and splittingFunction[1].strip() != "":
        outputFile.write(splittingFunction[0].strip())
        outputFile.write("\n")
        outputFile.write(splittingFunction[-1].strip())
        outputFile.write("\n")
