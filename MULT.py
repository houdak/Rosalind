"""
Multiple Alignment
Solved September 20, 2017
"""


""" I suspect this code does not work all of the time - for example,
if the longest sequence given would be better aligned with gaps.
However, this works ok, for what it needs to do. A more useful
solution would need to be able to handle more strings at a time anyway. """

import itertools as k
import FileOperations as f
from FrequentOperations import HammingDistance

def GappedStrings(strings):  
    """ Given 4 strings of different lengths, produces all possible
    gaps into the strings, returns as a list of 4 nested lists
    containing all of these possibilities """
    length = len(max(strings, key=len))
    permuted_strings = []
    for dna in strings:
        permuted_strings.append([])
        if len(dna) < length:
            gaps = length - len(dna)
            indices = [x for x in range(len(dna)+1)]
            possible_locs = k.combinations_with_replacement(indices,gaps)
            possible_locs = sorted(list(possible_locs))
            for combo in possible_locs:
                gappeddna = list(dna)
                x = -1
                for i in combo:
                    x += 1
                    gappeddna.insert(i+x,'-')
                permuted_strings[-1].append(''.join(gappeddna))            
        else:
            permuted_strings[-1].append(dna)
    return permuted_strings

def MultiAlignScore(g):
    """ Adds up Hamming distances between all
    of the gapped strings paired up """
    score = 0
    for i in range(len(g)):
        for j in range(i+1,len(g)):
            score += HammingDistance(g[i],g[j])
    return -1*score
    
def MultipleAlignment():
    """ Returns multiple alignment score, and aligned scores.
    Input is meant to be very short, so this will take advantage of that.
    Thus, not useful for longer or more numerous sequences. """
    input = f.LoadFile('\\rosalind_mult.txt')
    [labels, strings] = f.FASTA(input)
    [a,b,c,d] = GappedStrings(strings)
    alignment_combos = list(k.product(a,b,c,d))
    maxscore = -100000000000000000
    
    for combo in alignment_combos:
        if MultiAlignScore(combo) > maxscore:
            maxscore = MultiAlignScore(combo)
            minalignments = combo
    
    output = [str(maxscore),'\n'.join(minalignments)]
    f.ExportToFile('rosalind_mult_output.txt','\n'.join(output))
    return

MultipleAlignment()