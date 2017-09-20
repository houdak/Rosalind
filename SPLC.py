"""
RNA Splicing
Solved July 31, 2017
"""

import FileOperations as f
from FrequentOperations import DNAtoRNA
from FrequentOperations import RNAtoProtein

def Splicing():
    """ Given a DNA substring and a collection of substrings acting as introns,
    returns a protein string from transcribing and translating exons"""
    input = f.LoadFile('\\rosalind_splc.txt')
    [Label,DNA] = f.FASTA(input)
    
    t = DNA[0] # original string
    for substr in DNA[1:]:
        t = t.replace(substr, '') # remove introns
    RNA = DNAtoRNA(t)
    f.ExportToFile('rosalind_splc_output.txt', RNAtoProtein(RNA))
    return 

Splicing()