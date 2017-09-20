"""
Sex-Linked Inheritance
Solved August 24, 2017
"""

import FileOperations as f

# Sex-Linked Inheritance
def Sex():
    """ Given array of proportion of males exhibiting some total
    recessive X-linked genes, returns array with probabilities that a
    randomly selected female will be a carrier for the gene """
    p = f.LoadFile('\\rosalind_sexl.txt').split()
    p = [float(x) for x in p]
    
    B = []
    for i in p:
        q = 1 - i
        B.append(str(round(2*i*q,4)))
    
    f.ExportToFile('rosalind_sexl_output.txt',' '.join(B))
    return
    
Sex()