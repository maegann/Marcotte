# Writes only human entries to a new fasta file from a fasta file with some non-human entries
human = False
with open("uniprot_complete.fasta") as inFile:
    with open("out.txt", "w") as outFile:
        for line in inFile:
            if line.startswith(">"):
                if "HUMAN" in line:
                    human = True
                    outFile.write(line)
                else:
                    human = False
            elif human == True:
                outFile.write(line)
