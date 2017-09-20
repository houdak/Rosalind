"""
Perfect Matchings and RNA Secondary Structure
Solved August 6, 2017
"""

import FileOperations as f
from math import factorial

def Matching():
    """ Given a string of RNA, returns
    the total possible number of perfect matchings"""
    s = f.LoadFile('\\rosalind_pmch.txt')
    p = 1
    AU = 0
    CG = 0
    for nuc in s:
        if nuc in 'AU':
            AU += 1
        else:
            CG += 1   
    
    matchings = factorial(AU//2) * factorial(CG//2)
    f.ExportToFile('rosalind_pmch_output.txt',str(matchings))
    return
    
Matching()