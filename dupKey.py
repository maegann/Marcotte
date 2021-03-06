# Used on database when throw out duplicates.
# DB: Shows duplicates thrown out (column 2)
rep = ""
with open("uniprot_dup.fasta.clstr") as inFile:
    with open("duplicates_key.txt", "w") as outFile:
        for line in inFile:
            if line.startswith("0"):
                rep = line.split()
            else:
                if ">sp" in line:
                    dup = line.split()
                    outFile.write(rep[2] + "\t" + dup[2] + "\n")
