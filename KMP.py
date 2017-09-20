"""
Speeding Up Motif Finding
Solved August 19, 2017
"""

import FileOperations as f

# Speeding Up Motif Finding
def FailureArray():
    """ Given DNA string (FASTA), returns failure array"""
    input = f.LoadFile('\\rosalind_kmp.txt')
    [Label,s] = f.FASTA(input)
    
    # initialize P
    P = []
    for _ in range(len(s)):
        P.append(0)
    
    k = 0
    
    for i in range(2,len(s)+1):      
        
        while k > 0 and s[k] != s[i-1]:
           k = P[k-1]
        
        if s[k] == s[i-1]:
           k+=1
        P[i-1] = k
    f.ExportToFile('rosalind_kmp_output.txt',' '.join(str(x) for x in P))
    return

FailureArray()