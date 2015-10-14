# Run in results folder for the experiment (has combined-Results)
# Uses multi_isoforms.txt, combined-Results, and elution
# Compare combined-Results to elution for multi_isoforms.txt


# Compare the proteins with multiple isoforms found to the elution file
# Create a string of the relavant elution information
import os
outFile = open('output.txt', 'w')
directory = os.listdir(os.getcwd())
multiIsoforms = open ('prot_counts/multi_isoforms.txt', 'r')
proteins = []
elution = ''
pepSorted = ''
pepCounts = ''
pepArray = []

for protein in multiIsoforms:
    with open('prot_counts/HS_CB660_uniprot.prot_count_mFDRpsm001.unique_rmzero', 'r') as elutionFile: # make it so elution file isnt as specific
        for eluLine in elutionFile:
            if eluLine.startswith(protein.rstrip('\n')+'\t'):
                tempArray = eluLine.split('\t')
                proteins.append(tempArray[0])
                elution = elution + tempArray[0] + '\t'
                for i in range(2, len(tempArray)):
                    if not tempArray[i].startswith('0'):
                        elution = elution + tempArray[i] + '\t'
                elution = elution + '\n'
multiIsoforms.close()


# Go into each combined-Results directory
for i in directory:
    if '.combined-Results' in i:
# Open log file and get the sequences for the proteins with multiple isoforms found.
# Unique sequences are stored in variable uniqSeq
        log = ''
        logArray = []
        sequences = ''
        seqsArray = []
        uniqSeq = ''
        location = ''
        try:
            logFile = open(i + '/msblender.prot_count_mFDRpsm001.log', 'r')
            for logLine in logFile:
                for j in range(len(proteins)):
                    if ('|' + proteins[j] + '|') in logLine:
                        tempSeq = logLine.split('\t')
                        sequences = sequences + tempSeq[2].rstrip('\n') + ' '
            logFile.close()
            seqsArray = (sequences.strip()).split()
            for m in range(len(seqsArray)):
                if str(seqsArray.count(seqsArray[m])) == '1':
                    uniqSeq = uniqSeq + seqsArray[m] + ' '
        except IOError:
                  pass
                
# Open the log file and create a log of the proteins and their unique sequences
# there is an error somwhere could be with pep. and when it find the shorter sequence it is added again
        try:
            logFile2 = open(i + '/msblender.prot_count_mFDRpsm001.log', 'r')
            for logLine in logFile2:
                for j in range(len(proteins)):
                    if ('|' + proteins[j] + '|') in logLine:
                        tempSeq = logLine.split('\t')
                        if tempSeq[2].rstrip('\n') in uniqSeq:
                            log = log + proteins[j] + '\t' + tempSeq[2]
            logFile2.close()
            log = log.strip()
        except IOError:
                  pass
                
# Open pep_count file and add counts to the unique sequences found
        if log != '':
            try:
                pepFile = open(i + '/msblender.pep_count_mFDRpsm001', 'r')
                logArray = log.split('\n')
                for pepLine in pepFile:
                    sequence = []
                    for j in range(len(logArray)):
                        sequence = logArray[j].split('.')
                        if pepLine.startswith(sequence[1]) and (sequence[1] + '\t') in pepLine:
                            location = (i.split('.'))[0]

                            pepArray = pepLine.split('\t')
                            pepCounts = pepCounts + location + '\t' + logArray[j] + '\t(' + pepArray[2].rstrip('\n') + ')\n'
                pepFile.close()
            except IOError:
                pass
# Sort the unique peptides found in all files by the protein
pepArray = pepCounts.split('\n')  
for i in range(len(proteins)):
    for j in range(len(pepArray)):
        if (proteins[i] + '\t') in pepArray[j]:
            pepSorted = pepSorted + pepArray[j] + '\n'

#for loop goes through protein by protein in the protein array
# protein info from elution then the name of the folder then the ones for that protein
elutionArray = []
pepSortedArray = []
elutionArrayArray = []
elutionArray = elution.split('\n')
pepSortedArray = pepSorted.split('\n')
for i in range(len(elutionArray)-1):
    outFile.write(elutionArray[i] + '\n')
    elutionArrayArray = (elutionArray[i]).split('\t')
    for j in range(len(pepSortedArray)):
        if (elutionArrayArray[0] + '\t') in pepSortedArray[j]:
            outFile.write(pepSortedArray[j] + '\n')
outFile.close()
