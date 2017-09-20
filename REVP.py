"""
Locating Restriction Sites
Solved August 1, 2017
"""

import FileOperations as f
from FrequentOperations import ReverseComplement

def ReversePalindromes():
    """ Identifies all reverse palindromes in DNA string, FASTA format,
    of length 4 - 12"""
    input = f.LoadFile('\\rosalind_revp.txt')
    [Label,s] = f.FASTA(input)
  
    k = len(s)
    pal_tuples = []
    # Adjust start of window
    for i in range(k):
        # Adjust size of window
        for j in range(i+3,k+1):
            if j - i <= 12:
                if s[i:j] == ReverseComplement(s[i:j]):
                    pal_tuples.append(' '.join((str(i+1),str(j-1))))
    
    f.ExportToFile('rosalind_revp_output.txt', '\n'.join(pal_tuples))
    return
    
ReversePalindromes()