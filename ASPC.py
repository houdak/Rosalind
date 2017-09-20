"""
Introduction to Alternative Splicing
Solved August 20, 2017
"""

import FileOperations as f
from FrequentOperations import nCr

def Splicing():
    """ Returns sum of combinations C(n,k) for m<=k<=n, modulo 1000000 """
    [n,m] = f.LoadFile('\\rosalind_aspc.txt').split()
    n = int(n)
    m = int(m)
    
    count = 0
    for k in range(m,n+1):
        count += nCr(n,k)
    
    f.ExportToFile('rosalind_aspc_output.txt',str(count % 1000000))
    return
    
Splicing()