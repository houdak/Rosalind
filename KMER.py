"""
k-mer Composition
Solved August 8, 2017
"""

import FileOperations as f
from FrequentOperations import Lex

# k-Mer Composition
def kmerComp():
    """ Given DNA string s (FASTA), returns the 4-mer composition of s"""
    input = f.LoadFile('\\rosalind_kmer.txt')
    [Label,s] = f.FASTA(input)
    
    # Generate all 4-mers, ordered lexographically
    lex_list = Lex('ACGT', 4)
    A = []
    # go through lex_list, count frequency of each 4-mer
    for kmer in lex_list:
        count = 0
        for i in range(len(s)-3): #-k+1
            test = s[i:i+4]
            if test == kmer:
                count +=1
        A.append(str(count))
    f.ExportToFile('rosalind_kmer_output.txt',' '.join(A))    
    return

kmerComp()