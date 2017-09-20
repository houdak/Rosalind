"""
Constructing a De Bruijin Graph
Solved August 27, 2017
"""

import FileOperations as f
from FrequentOperations import ReverseComplement
from FrequentOperations import RemoveDuplicates

# Constructing a De Bruijn Graph
def DeBruijnRC():
    """ Returns adjacency list, based on
    given DNA strings and their reverse complements"""
    S = f.LoadFile('\\rosalind_dbru.txt').splitlines()

    # Make list of S U Src
    SuRC = []    
    for i in S:
        SuRC.append(ReverseComplement(i))
    SuRC.extend(S)
    SuRC = RemoveDuplicates(SuRC)
    
    # Add all prefixes to adj_dict
    adj_dict = {}
    for kmer in SuRC:
        adj_dict[kmer[:-1]] = []
      
    for i in adj_dict:
        for j in SuRC:
            if i == j[:-1]: # Look for strings with that prefix
                adj_dict[i].append(j[1:]) #If so, add suffix
    
    # Return in format
    output = []
    for i in adj_dict:
        for j in adj_dict[i]:
            output.append(('(%s, %s)' %(i,j)))
    
    f.ExportToFile('rosalind_dbru_output.txt','\n'.join(output))         
    return

DeBruijnRC()