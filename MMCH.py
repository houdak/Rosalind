"""
Maximum Matchings and RNA Secondary Structures
Solved August 20, 2017
"""

import FileOperations as f
from math import factorial

def nPr(n,r):
    """ n Permutation r """
    return factorial(n) // factorial(n-r)

def MaxMatching():
    """ Given RNA string (FASTA), return total
    possible number of maximum matchings"""
    input = f.LoadFile('\\rosalind_mmch.txt')
    [Label, s] = f.FASTA(input)
    
    nuc_dict = {'A': 0, 'U': 0, 'C': 0, 'G': 0}
    for nuc in s:
        nuc_dict[nuc] += 1
 
    minAU = min([nuc_dict['A'],nuc_dict['U']])
    minCG = min([nuc_dict['C'],nuc_dict['G']])
    maxAU = max([nuc_dict['A'],nuc_dict['U']])
    maxCG = max([nuc_dict['C'],nuc_dict['G']])    
    
    matches = str(  nPr(maxAU,minAU) * nPr(maxCG,minCG)  )
    f.ExportToFile('rosalind_mmch_output.txt',matches)
    return
    
MaxMatching()