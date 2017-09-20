"""
The Founder Effect and Genetic Drift
Solved August 25, 2017
"""

import FileOperations as f
from math import log10
from FrequentOperations import nCr

# The Founder Effect and Genetic Drift
def DriftToNone(N,g,m):
    """ Algorithm for time to loss of recessive allele """
    # N will be N from founder
    n = 2*N
    k = 0
    
    curr_gen = [0 for i in range(n+1)]
    curr_gen[m] = 1

    for gen in range(g):
        next_gen = [0 for i in range(n+1)]
        for x in range(n+1):
            for y in range(n+1):
                temp_term = nCr(n,x) * (y/n)**x * (1-(y/n))**(n-x)
                next_gen[x] += temp_term * curr_gen[y]
        
        curr_gen = next_gen    
    return curr_gen[0]
    
def Founder():
    """ Returns matrix representing log(prob) that after i
    generations, no copies of the recessive allele will 
    remain in the population """
    input = f.LoadFile('\\rosalind_foun.txt').splitlines()
    [N, m] = [int(x) for x in input[0].split()]
    A = [int(x) for x in input[1].split()]
    
    # initialize matrix
    B = []
    for i in range(m): #possible generations
        B.append([])
        for j in range(len(A)): #possible initial copies
            B[i].append(0)
       
    # Add DriftToNone to correct box
    for i in range(1,m+1):
        for j in range(len(A)):
            B[i-1][j] = str(log10(DriftToNone(N,i,A[j])))
    
    # print in format
    B_print = []
    for line in B:
        B_print.append(' '.join(line))
    f.ExportToFile('rosalind_foun_output.txt','\n'.join(B_print))
    return

Founder()