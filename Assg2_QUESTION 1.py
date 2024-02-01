#Nurul Hamizah binti Che Azemin (U2004970)
#Extract multiple sequence lines and print it into a single line
#26 dec 2022

'''
Pseudocode
s
Start
Import re module
Prompt user to input file name in .txt type
Open input file to read
Read all lines in the file
Define variable singleSeq to store value
Display a message according input file format either in embl or gcg
For loop to read each item and extract sequence lines only from 'lines' using re.match function
If matched object found, it returns TRUE
Extract the sequence part only using group
Concate all sequence parts into a single sequence line
Print singleSeq
Print the length of singleSeq using len function
Stop

'''

#Import re module in python
import re

print("\nThis program extract multiple sequence lines from EMBL or GCG file format and print it into a single line of sequence.\n")

#Prompt user to input file name in .txt type
inpFile=input("Enter the input file name: \n")

#Open file inpFile to read
#By default, the open file is in read mode
fo = open(inpFile)

#Read all lines in the file using readlines()
lines = fo.readlines()

#Define variable singleSeq to store value
singleSeq = ""

#Once file name is entered, the system will recognize the input file
#Message is displayed in EMBL format if input in embl
if re.search(r"embl", inpFile):
    print("\nThe sequence file is in EMBL flat file format.")

    #for loop to read each item
    for line in lines:

        #extract the sequence lines only from 'lines' using re.match function
        #the matched object(s) from line is(are) assigned into variable named mSeq
        mSeq = re.match(r"(\s+)(([a-z_.*-]+\s+)+)\s+\d+",line, re.I)

        #if matched object found, it returns TRUE
        if mSeq:

            #to extract the sequence part only using group(2)
            sequence = mSeq.group(2)

            #to replace a space/many spaces with empty in the sequence part using re.sub function
            sequence = re.sub(r" ","",sequence)

            #to concate all sequence parts into a single sequence line
            singleSeq += sequence
            
#Message is displayed in GCG format if input in gcg        
else:
    print("\nThe sequence file is in GCG flat file format.")

    #for loop to extract the sequence lines only from 'lines' using re.match function
    for line in lines:

        #the matched object(s) from line is(are) assigned into variable named mSeq
        mSeq = re.match(r"\s*\d+\s+(.+)",line)

        #if matched object found, it returns TRUE    
        if mSeq:

            #to extract the sequence part only using group(2)
            sequence = mSeq.group(1)

            #to replace a space/many spaces with empty in the sequence part using re.sub function
            sequence = re.sub(r" ","",sequence)

            #to concate all sequence parts into a single sequence line
            singleSeq += sequence

#Print output singleSeq
print("\nSequence in a single line:",singleSeq)
#print(singleSeq)

#Print the length of singleSeq using len function
print("\nThe length of the sequence: ",len(singleSeq),"bp")
          
    
    
