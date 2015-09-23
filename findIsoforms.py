#run in the project directory
# Finds isoforms where unique is greater than 0
import os
directories = os.listdir(os.getcwd())
outFile = open ('MS_Isoforms.txt', 'w')
for i in directories:
    if '.combined-Results' in i:
        try:
            inFile = open (i + '/msblender.prot_count_mFDRpsm001', 'r')
            for line in inFile:
                if (not line.startswith('#')) and (not line.startswith("CONTAMINANT")):
                    spLine = line.split()
                    if '-' in line and spLine[3] != '0':
                        outFile.write(i + '\t' + line)
        except IOError:
            print "Error: File doesn't exist in", i
        inFile.close()
outFile.close()
