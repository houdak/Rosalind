"""
Finding a Spliced Motif
Solved August 8, 2017
"""

import FileOperations as f

def SplicedMotif():
    """ Given DNA strings s & t, FASTA format, returns
    a collection of indices in which symbols of t appears as a 
    subsequence of s """
    input = f.LoadFile('\\rosalind_sseq.txt')
    [Labels,DNA] = f.FASTA(input)
    s = DNA[0]
    t = DNA[1]
    
    loc = []
    i = 0
    # Go through s one nucleotide at a time
    for sym in s:
        i += 1
        # once first symbol
        if sym == t[0]:
            loc.append(str(i))
            t = t[1:]
            if t == '':
                break
    
    f.ExportToFile('rosalind_sseq_output.txt',' '.join(loc))
    return
    
SplicedMotif()