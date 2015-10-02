# run on prot_count files .
# Find all with a specific amount of unique
# can then sort and inspect to see if canonical and isoform of a certain uniprot id are both present

import os
directories = os.listdir(os.getcwd())
outFile = open ('MS_uniques.txt', 'w')
for i in directories:
    if '.combined-Results' in i:
        try:
            inFile = open (i + '/msblender.prot_count_mFDRpsm001', 'r')
            for line in inFile:
                if (not line.startswith('#')) and (not line.startswith("CONTAMINANT")):
                    spLine = line.split()
                    if spLine[3] > '1':
                        #outLine = line.replace(*'sp|', 'sp|'
                       # outFile.write(i + '\t' + line)
                       outFile.write(line)
            inFile.close()
        except IOError:
            print "Error: File doesn't exist in", i

outFile.close()
