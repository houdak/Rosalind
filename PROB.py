"""
Introduction to Random Strings
Solved August 6, 2017
"""

import FileOperations as f
from math import log10

def RandomStrings():
    """ Given DNA string and array, returns array representing
    log(probability) that a random string constructed with the
    GC-content found in A will match s exactly"""
    input = f.LoadFile('\\rosalind_prob.txt').splitlines()
    s = input[0]
    p = input[1].split()
    p = [float(x) for x in p]
    
    probs = []
    for gc in p:
        prob = 1
        for nuc in s:
            if nuc in 'CG':
                prob = prob * (gc/2)
            else:
                prob = prob * ((1-gc)/2)
        probs.append(str(log10(prob)))
    f.ExportToFile('rosalind_prob_output.txt',' '.join(probs))
    return

RandomStrings()