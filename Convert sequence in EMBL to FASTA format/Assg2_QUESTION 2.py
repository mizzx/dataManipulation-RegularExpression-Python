#Nurul Hamizah binti Che Azemin (U2004970)
#Convert a sequence from EMBL file format ("seq.embl") into a FASTA file format("seq_embl2fasta.fa")
#26 dec 2022

'''
Pseudocode

Start
Import re module
Open external file named "seq.embl.txt" in read mode and assign it into variable fileIn
Open external file named "seq_embl2fasta.fa" in write mode and assign it into variable fileOut
Read all lines in the fileIn
For loop to read each line
Extract the AC line only from 'lines' using re.match function
If match, extract the accession part only using group
Extract the OS line only from 'lines' using re.match function
If match, extract the scientific name of organism part only using group
Extract the sequence lines only from 'lines' using re.match function
If match, extract the seq line part only using group
End for loop
If sequence return value, store the splitted 'sequence' into variable named tempSplitSeq
Use len function to get length of the sequence
Set number of characters to cut off at 120
For loop to split a single line 'sequence' into multiple lines and store in 'tempSplitSeq' list
Format the header line
Print header line on command line
Write header line into an external file
For loop to print sequence lines in 120 characters per line
Print sequence lines on command prompt
Write sequence lines into an external file
Close fileIn
Close fileOut
Stop

'''

#Import re module in python
import re

print("\nThis program convert a sequence from EMBL file format ('seq.embl') into a FASTA file format ('seq_embl2fasta.fa')\n")

#Define variables to store value
accession = ""
organism = ""
sequence = ""

#open external file named "seq.embl.txt" in read mode and assign it into variable fileIn
fileIn = open("seq.embl.txt", "r+")

#open external file named "embl2fasta.fa" in write mode and assign it into variable fileOut
fileOut = open("seq_embl2fasta.fa", "w+")

#Read all lines of fileIn and assign it into variable named lines
lines = fileIn.readlines()

#for loop used to read each line
for line in lines:

    #extract the AC line only from 'lines' using re.match function
    #the matched object(s) from line is(are) assigned into variable named matchAccess
    matchAccess = re.match(r'^AC\s+(.+);$', line, re.I)

    #if matched object found, it returns TRUE
    if matchAccess:

        #to extract the accession part only using group(1)
        accession = matchAccess.group(1)

    #extract the OS line only from 'lines' using re.match function
    #the matched object(s) from line is(are) assigned into variable named matchOrganism
    matchOrganism = re.match(r'^OS\s+(([a-z]+\s+)+).*', line, re.I)
    
    #if matched object found, it returns TRUE
    if matchOrganism:

        #to extract the scientific name of organism part only using group(1)
        organism = matchOrganism.group(1)

    #extract the sequence lines only from 'lines' using re.match function
    #the matched object(s) from line is(are) assigned into variable named matchSeq
    matchSeq = re.match(r"(\s+)(([a-z_.*-]+\s+)+)\s+\d+", line, re.I)
    
    #if matched object found, it returns TRUE
    if matchSeq:

        #to extract the seq line part only using group(2)
        seqline = matchSeq.group(2)

        #to replace a space/many spaces with empty in the seqline using re.sub function
        seqline = re.sub(r" ","",seqline)
        sequence += seqline
        
#seq returns a value
if sequence:

    #To store the splitted 'sequence' into variable named tempSplitSeq
    tempSplitSeq=[]

    #Use len function to get length of the sequence
    seqLen=len(sequence)

    #Number of characters to cut off
    cutoff=120

    #To split a single line 'sequence' into multiple lines and store in 'tempSplitSeq' list
    for i in range(0, seqLen, cutoff): 
        tempSplitSeq.append(sequence[i:i+cutoff])

    #To format the header line
    head = ">" + accession.strip() + "\t" + organism.strip() + "\t" + str(seqLen) + " bp"

    #Print 'head' on command prompt
    print(head)

    #Write 'head' into an external file
    fileOut.write(head + "\n")

    #Sequence lines in 120 characters per line    
    for newLine in tempSplitSeq:

        #Print sequence lines on command prompt
        print(newLine)

        #Write sequence lines into an external file
        fileOut.write(newLine.upper()+'\n')

#Close file named "seq.embl.txt"
fileIn.close()

#Close file named "embl2fasta.fa"
fileOut.close()
