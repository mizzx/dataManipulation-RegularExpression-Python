#Nurul Hamizah binti Che Azemin (U2004970)
#Convert a sequence from GCG file format ("seq.gcg") into a GENBANK file format
#26 dec 2022

'''
Pseudocode

Import string module in python
Import re module in python
Define variables to store value
Open external file named "seq.gcg.txt" in read mode
Open external file created named "gcg2gb.genbank" in write mode
Read all lines of fileIn
For loop to read each line
Extract the line contain locus object and length using re.match function
Extract the line contain organism name using re.match function
Extract the line contain sequence using re.match function
Append sequence list and remove spaces of string in list
Print locus line on command prompt
Write locus line into an external file
Print SOURCE on command prompt
Write SOURCE into an external file
Print organism line on command prompt
Write organism line into an external file
Convert sequence list into string using join function
Count every base sequence using count function
Print BASE COUNT line on command prompt
Write BASE COUNT line into an external file
Print ORIGIN on command prompt
Write ORIGIN into an external file
For loop to format sequence in 60 bp with the cut-off of 10 characters and separated by a white space
Print formated sequence line in upper case on command prompt
Write formated sequence line in upper case into an external file
Print "//" on command prompt
Write "//" into an external file
Close all files

'''

#Import string module in python
import string

#Import re module in python
import re 

print("\nThis program convert a sequence from GCG file format ('seq.gcg') into a GENBANK file format ('seq_gcg2gb.genbank')\n")

#Define variables to store value
locus = ""
source = ""
org = ""
sequence = []

#Open external file named "seq.gcg.txt" in read mode and assign it into variable fileIn
fileIn = open("seq.gcg.txt", "r+")

#Open external file created named "gcg2gb.genbank" in write mode and assign it into variable fileOut
fileOut = open("seq_gcg2gb.genbank", "w+")

#Read all lines of fileIn and assign it into variable named lines
lines = fileIn.readlines()

#for loop used to read each line
for line in lines:

    #extract the line contain locus object and length from 'lines' using re.match function
    inpLine = re.match(r'(.*)\s+Length:\s(\d+).*\.\.$', line, re.I)
    if inpLine:
        locobj = inpLine.group(1) #HSFAU
        lenseq = inpLine.group(2) #518
        locus = "LOCUS\t" + "   " + locobj + "\t" + lenseq + " bp\tDNA"
        source = "SOURCE"

    #extract the line contain organism name from 'lines' using re.match function
    matchOrg = re.match(r'[^!][^\s0-9].*\w$', line, re.I) 
    if matchOrg:
        org = matchOrg.group(0) #extract H.sapiens fau mRNA
        terms = org.split(" ") #split the items
        match0 = terms[0] #extract H.sapiens
        org = ("ORGANISM  " + match0)

    #extract the line contain sequence from 'lines' using re.match function
    matchSeq = re.match(r"\s*\d+\s+(.+)",line, re.I)
    if matchSeq:
        seqline = matchSeq.group(1)

        #append sequence list
        #remove spaces of string in list
        sequence.append(seqline.strip()) 

#Print locus line on command prompt
print(locus)

#Write locus line into an external file
fileOut.write(locus + "\n")

#Print SOURCE on command prompt
print(source)

#Write SOURCE into an external file
fileOut.write(source + "\n")

#Print organism line on command prompt
print(" " + org)

#Write organism line into an external file
fileOut.write(" " + org + "\n")

#Convert sequence list into string using join function
seq = ''.join(sequence)

#replace a space/many spaces with empty in the seq using replace function
#store into lineseq variable
lineseq = seq.replace(" ","")

#Count every base sequence using count function
a = lineseq.count('a')
c = lineseq.count('c')
g = lineseq.count('g')
t = lineseq.count('t')

#Print BASE COUNT line on command prompt
print("BASE COUNT    " + str(a) +" a\t" + str(c) + " c\t" + str(g) +" g\t" + str(t) + " t")

#Write BASE COUNT line into an external file
fileOut.write("BASE COUNT    " + str(a) +" a\t" + str(c) + " c\t" + str(g) +" g\t" + str(t) + " t")

#Print ORIGIN on command prompt
print('ORIGIN    '+'\n')

#Write ORIGIN into an external file
fileOut.write('\nORIGIN    '+'\n')

#Format sequence in 60 bp with the cut-off of 10 characters and separated by a white space
count = 1
cutoff = "{:10d}".format(count)+" "
for i in range(len(lineseq)):
    if(i % 10 == 0 and i>0):
        if(i%60 == 0):
            count += 60
            cutoff += "\n{:10d}".format(count)+" "+lineseq[i]
        else:
            cutoff += " "+lineseq[i]
    else:
        cutoff += lineseq[i]

#Print formated sequence line in upper case on command prompt
print(cutoff.upper())

#Write formated sequence line in upper case into an external file
fileOut.write(cutoff.upper()+"\n")

print("//")
fileOut.write("//")

#Close all files
fileIn.close()
fileOut.close()


        
        
