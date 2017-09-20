"""
Counting Point Mutations
Solved July 26, 2017
"""

import FileOperations as f

def HammingDistance():
    """Returns the Hamming Distance between 2 strings"""
    input = f.LoadFile('\\rosalind_hamm.txt').splitlines()
    p = input[0]
    q = input[1]
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist += 1
    f.ExportToFile('rosalind_hamm_output.txt',str(dist))
    return

HammingDistance()