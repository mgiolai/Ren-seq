#calculate modal value of read lengths
import sys
from Bio import SeqIO #biopython
from collections import Counter

sequences = []

input_file = (sys.argv[-1])

for read in SeqIO.parse(input_file, "fasta"):
    i = float(len(read.seq))
    j=round(i/1000,1)
    sequences.append(j)
print("(1) Mode, (2) n")
print(Counter(sequences).most_common(1)) #first number = mode, second number = number of elements



