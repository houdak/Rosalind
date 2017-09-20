"""
Counting Subsets
Solved August 20, 2017
"""

import FileOperations as f

def Subsets():
    """ Given positive int n, returns total number of subsets
    1:n modulo 1000000"""
    n = int(f.LoadFile('\\rosalind_sset.txt'))
    P = 2**n % 1000000
    f.ExportToFile('rosalind_sset_output.txt',str(P))
    return

# Former, more complicated, function
"""def Subsets(n):    
    count = 0
    for i in range(n+1):
        count += nCr(n,i)
    return count % 1000000"""

Subsets()