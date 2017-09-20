"""
Counting Phylogenetic Ancestors
Solved August 20, 2017
"""

import FileOperations as f
from math import factorial

def UnrootedTree():
    """ Given positive integer n, returns the number of internal
    nodes of any unrooted binary tree having n leaves.
    n leaves --> n-2 internal nodes"""
    n = int(f.LoadFile('\\rosalind_inod.txt'))    
    f.ExportToFile('rosalind_inod_output.txt',str(n-2))
    return

UnrootedTree()


""
X = factorial(n) // factorial(n-2)

0 = n**2 - n - 2*X
n = 
"""