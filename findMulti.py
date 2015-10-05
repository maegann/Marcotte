#Creates a file with a list of all the proteins in alphabetical order
#Takes that file and creates a file of proteins that have isoforms.
with open("test.txt") as inFile:
    with open("unique_proteins.txt", "w") as outFile:
        for line in inFile:
            if not(line.startswith('CONTAMINANT') or line.startswith('#')):
                sline = line.split()
                outFile.write(sline[0]+'\n')
protein = ''
possible = ''
newProtein = False
with open("unique_proteins.txt") as inFile2:
    with open("multi_isoforms.txt", "w") as outFile2:
        for line in inFile2:
            temp = line.rstrip('\n')
            possible = temp.split('-')
            if protein != '' and possible[0] == protein[0]:
                if newProtein == True:
                    outFile2.write('-'.join(protein)+'\n')
                    newProtein = False
                    outFile2.write('-'.join(possible)+'\n')
                else:
                    outFile2.write('-'.join(possible)+'\n')
            else:
                 protein = possible
                 newProtein = True
