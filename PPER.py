"""
Partial Permutations
Solved August 6, 2017
"""

import FileOperations as f
from FrequentOperations import nCr
from math import factorial

def PP():
    """ Given the total collection (n) and size of partial permutation (k),
    returns the total number of partial permutations, modulo 1000000"""
    input = f.LoadFile('\\rosalind_pper.txt').split()
    n = int(input[0])
    k = int(input[1])
    
    # First find number of combinations (no repeats)
    c = nCr(n,k)
    # Multiply that times number of permutations for each combo
    p = factorial(k)
    total = (p * c) % 1000000
    f.ExportToFile('rosalind_pper_output.txt',str(total))
    return

PP()