"""
Expected Number of Restriction Sites
Solved August 13, 2017
"""

import FileOperations as f
from FrequentOperations import nCr

# Expected Number of Restriction Sites
def RestrictionPrediction():
    """ Returns array B representing the expected number of times
    that s will appear as a substring of a random DNA string t of
    length n, where t is formed with GC-content from A"""
    input = f.LoadFile('\\rosalind_eval.txt').splitlines()
    n = int(input[0])
    s = input[1]
    A = [float(x) for x in input[2].split()]
    
    B = []
    C = nCr(n-len(s)+1,1)
    for gc in A:
        prob = 1
        for nuc in s:
            if nuc in 'CG':
                prob = prob * (gc/2)
            else:
                prob = prob * ((1-gc)/2)
        P = C*prob
        B.append(str(P))
    
    f.ExportToFile('rosalind_eval_output.txt',' '.join(B))
    return

RestrictionPrediction()