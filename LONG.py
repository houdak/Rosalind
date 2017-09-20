"""
Genome Assembly as Shortest Superstring
Solved August 27, 2017
"""

import FileOperations as f
import copy
from FrequentOperations import Overlap
from FrequentOperations import Combine

def MaxMatrix(m):
    """ Returns location for maximum in matrix """
    max = 0
    index = [0,1]
    for i in m:
        for j in i:
            if j > max:
                max = j
                index = [m.index(i),i.index(j)]
    return index 

def SuperString():
    """ Given several DNA strings, FASTA format,
    returns shortest possible superstring"""
    input = f.LoadFile('\\rosalind_long.txt')
    [Labels, DNA] = f.FASTA(input)
    
             
    while len(DNA) > 2: # Repeat cycle until only one string left 
        # Find pair of strings with greatest overlap
        ## Initialize overlap matrix
        overlap_matrix = []
        for i in range(len(DNA)):
            overlap_matrix.append([])
            for j in range(len(DNA)):
                overlap_matrix[i].append(0)
        
        ## Fill in with overlaps
        for i in DNA:
            for j in DNA:               
                overlap_matrix[DNA.index(i)][DNA.index(j)] = Overlap(i,j)
        
        # Replace strings with max overlap with superstring
        ## Find index of max overlap + value
        max_overlap = MaxMatrix(overlap_matrix)
        ind1 = max_overlap[0]
        ind2 = max_overlap[1]
        ## Make superstring based on this info
        s = Combine(DNA[ind1],DNA[ind2])
        ##  Remove shorter strings, add superstring
        x = copy.copy(DNA[ind1])
        y = copy.copy(DNA[ind2])
        DNA.remove(x)
        DNA.remove(y)
        DNA.append(s)
    
    superstring = Combine(DNA[0],DNA[1])
    f.ExportToFile('rosalind_long_output.txt', superstring)     
    return

SuperString()