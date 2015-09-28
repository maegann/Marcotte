# Counts how many prot_count files do not exist
import os
directories = os.listdir(os.getcwd())
nonexistant = 0
tried = 0
for i in directories:
    if '.combined-Results' in i:
        tried += 1
        try:
            inFile = open (i + '/msblender.prot_count_mFDRpsm001', 'r')
            inFile.close()
        except IOError:
            print "Error: File doesn't exist in", i
            nonexistant += 1
print "Number of directories that should have file is", tried
print "Number of files not found is", nonexistant
print "Should see", tried-nonexistant, "files in prot_counts directory."
