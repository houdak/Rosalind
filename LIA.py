"""
Independent Alleles
Solved August 13, 2017
"""

import FileOperations as f
from FrequentOperations import nCr

def IndependentAlleles():
    input = f.LoadFile('\\rosalind_lia.txt').split()
    k = int(input[0])
    N = int(input[1])
    
    P = 2**k
    prob = 0
    for i in range(N,P+1):
        prob += nCr(P,i)*(0.25**i)*(0.75**(P-i)) # formula for Mendel's 2nd Law
    f.ExportToFile('rosalind_lia_output.txt',str(prob))
    return

IndependentAlleles()