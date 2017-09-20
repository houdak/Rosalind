"""
Open Reading Frames
Solved August 1st, 2017
"""

import FileOperations as f
from FrequentOperations import RemoveDuplicates
from FrequentOperations import ReverseComplement
from FrequentOperations import DNAtoRNA
from FrequentOperations import RNAtoProtein

def ORF():
    """ Returns all distinct candidate protein strings that can be 
    translated from ORFs of the given DNA string, FASTA format"""
    input = f.LoadFile('\\rosalind_orf.txt')
    [Labels,DNA] = f.FASTA(input)
    allDNA = []
    allDNA.append(ReverseComplement(DNA))
    
    # Convert to RNA
    RNA = []
    for i in allDNA:
        RNA.append(DNAtoRNA(i))
        
    # Get all strings from start codon to first stop
    seq = []
    for r in RNA:
        start = []
        stop = []
        for i in range(len(r)):
            if r[i:i+3] == 'AUG':
                start.append(i)
            elif r[i:i+3] in ['UAA', 'UAG', 'UGA']:
                stop.append(i)          
        
    for i in start:
        for j in stop:
            if (    j > i
                and (j-i) % 3 == 0):
                seq.append(r[i:j])
                break

    # Convert to Protein
    proteins = []
    for s in seq:
        proteins.append(RNAtoProtein(s))
    proteins = RemoveDuplicates(proteins)
    f.ExportToFile('rosalind_orf_output.txt', '\n'.join(proteins))
    return
    
ORF()