"""
Wright-Fisher's Expected Behavior
Solved August 25, 2017
"""

import FileOperations as f

def ExpectedVal():
    """ Given positive int n and array P representing probabilities
    corresponding to an allel frequency, returns array B representing
    the expected allele frequency of the next generation """
    input = f.LoadFile('\\rosalind_ebin.txt').splitlines()
    n = int(input[0])
    P = [float(x) for x in input[1].split()]
    
    B = [str(round(i*n,4)) for i in P]
    f.ExportToFile('rosalind_ebin_output.txt',' '.join(B))
    return

ExpectedVal()