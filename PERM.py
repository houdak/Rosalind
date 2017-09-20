"""
Enumerating Gene Orders
Solved August 1, 2017
"""

import FileOperations as f
from itertools import permutations

def GeneOrders():
    """ Given a positive integer n, returns the total number of permutations
    length n followed by a list of all such permutations"""
    n = int(f.LoadFile('\\rosalind_perm.txt'))
    
    p = []
    for i in range(1,n+1):
        p.append(i) # get all numbers 1-n
    p = [str(x) for x in p] # to make printing easier later on
    perms = list(permutations(p)) #returns all permutations

    # format for printing
    perms_print = [str(len(perms))]
    for tup in perms:
        perms_print.append(' '.join(tup)) 
    f.ExportToFile('rosalind_perm_output.txt', '\n'.join(perms_print))
    return
    
GeneOrders()