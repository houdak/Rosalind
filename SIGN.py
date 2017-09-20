"""
Enumerating Oriented Gene Orderings
Solved August 14, 2017
"""

import FileOperations as f
from itertools import permutations

def posneg(tup,n):
    """ Checks wheter both pos and neg values are in the tuple """
    check = 0
    for i in range(n+1):
        if (i in tup) and (i*-1 in tup):
            check += 1
    if check > 0:
        return True
    else:
        return False

def OrientedGeneOrders():
    """ Given a positive integer n, returns total number of signed
    permutations length n, followed by a list of all such permutations """
    n = int(f.LoadFile('\\rosalind_sign.txt'))
    
    # Find all possible values
    p = []
    for i in range(-n,n+1):
        if i != 0:
            p.append(i)
            
    perms = list(permutations(p,n)) # list of all permutations
    per = []
    for tup in perms:
        if posneg(tup,n) == False:
        # Check if both pos and neg s in tup
            per.append(' '.join(str(x) for x in tup))
    per.insert(0, str(len(per)))
    
    f.ExportToFile('rosalind_sign_output.txt','\n'.join(per))
    return

OrientedGeneOrders()