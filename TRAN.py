"""
Transitions and Transversions
Solved August 6, 2017
"""

import FileOperations as f

def TT():
    """ Given 2 DNA strings of equal length, FASTA format,
    returns the transition / transversion ratio
    Transitions: A<->G, C<->T
    Transversions: A<->T, A<->C, G<->C, G<->T """
    input = f.LoadFile('\\rosalind_tran.txt')
    [Labels,DNA] = f.FASTA(input)
    p = DNA[0]
    q = DNA[1]
    
    transition = 0
    transversion = 0
    for i in range(len(p)):
        if p[i] == q[i]:
            continue
        else:
            if (p[i] in 'AG') and (q[i] in 'AG'):
                transition += 1
            elif (p[i] in 'CT') and (q[i] in 'CT'):
                transition += 1
            else:
                transversion +=1
    ratio = str(transition/transversion)
    f.ExportToFile('rosalind_tran_output.txt',ratio)
    return

TT()