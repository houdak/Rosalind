"""
Matching Random Motifs
Solved August 13, 2017
"""

import FileOperations as f

def RandomMotifs():
    """ Gives probability that if n random DNA strings having the
    same length as s are constructed with GC-content x, then at
    least one of the strings equals s"""
    input = f.LoadFile('\\rosalind_rstr.txt').splitlines()
    input2 = input[0].split()
    N = int(input2[0])
    x = float(input2[1])
    s = input[1]
    
    prob = 1
    for nuc in s:
        if nuc in 'CG':
            prob = prob * (x/2)
        else:
            prob = prob * ((1-x)/2)
    P = 1 - (1-prob)**N
    
    f.ExportToFile('rosalind_rstr_output.txt',str(P))
    return

RandomMotifs()