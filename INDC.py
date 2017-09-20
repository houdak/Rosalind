"""
Independent Segregation of Chromosomes
Solved August 20, 2017
"""

import FileOperations as f
from FrequentOperations import nCr
from math import log10

def Segregation():
    """ Given positive integer n, returns array A of length 2n
    with A[k] representing log(probability) that 2 diploid siblings
    share at least k of their 2n chromosomes"""    
    n = int(f.LoadFile('\\rosalind_indc.txt'))
    # P at least k match = P at least 2n-k differ
    N = 2*n
    A = []
    for k in range(1,2*n+1):
        prob = 0
        # Subtract probability of all other possiblities
        # ex. k = 2, and N = 5 means probability that there a 4 tails, 5 tails (0-3 is fine)    
        for i in range(k,N+1):
            prob += nCr(N,i) * (0.5)**i * (0.5)**(N-i)
        A.append(str(log10(prob)))
    
    f.ExportToFile('rosalind_indc_output.txt',' '.join(A))
    return
    
Segregation()