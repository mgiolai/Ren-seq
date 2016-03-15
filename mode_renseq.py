#calculate modal value of read lengths
#biopython-1.66
#python-2.7.9
import sys
from Bio import SeqIO #biopython
from collections import Counter

sequences = []

input_file = (sys.argv[-1])

for read in SeqIO.parse(input_file, "fasta"):
    i = float(len(read.seq))
    j=round(i/1000,1) #divides read by 1000 and rounds to 1 digit after the decimal point, e.g. 3600bp -> 3.6kb
    sequences.append(j)
print("(1) Mode [kb], (2) n")
print(Counter(sequences).most_common(1)) #first number = mode, second number = number of elements



