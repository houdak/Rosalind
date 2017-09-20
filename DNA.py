"""
Counting DNA Nucleotides
Solved July 26, 2017
"""

import FileOperations as f

def CountingNucleotides():
    """Returns counts of A,C,G,and T nucleotides in that order"""
    s = f.LoadFile('\\rosalind_dna.txt')
    count = [0,0,0,0]
    for nuc in s:
        if nuc == 'A':
            count[0] += 1
        if nuc == 'C':
            count[1] += 1
        if nuc == 'G':
            count[2] += 1
        if nuc == 'T':
            count[3] += 1
    f.ExportToFile('rosalind_dna_output.txt', ' '.join(str(x) for x in count))
    return

CountingNucleotides()