"""
Creating a Distance Matrix
Solved August 20, 2017
"""

import FileOperations as f
from FrequentOperations import HammingDistance

def DistanceMatrix():
    """ Given n DNA strings (FASTA), returns distance matrix """
    input = f.LoadFile('\\rosalind_pdst.txt')
    [Label,DNA] = f.FASTA(input)
    
    # Initialize distance matrix
    D = []
    for _ in DNA:
        D.append([])
    for i in range(len(D)):
        for _ in range(len(D)):
            D[i].append(0)
    
    # Calculate Hamming Distance, add to matrix
    for i in range(len(DNA)):
        for j in range(len(DNA)):   
            dist = HammingDistance(DNA[i],DNA[j])
            D[i][j] = str(dist/len(DNA[0]))
    
    # Properly format
    D_formatted = []
    for line in D:
        D_formatted.append(' '.join(line)) 
    f.ExportToFile('rosalind_pdst_output.txt','\n'.join(D_formatted))
    return

DistanceMatrix()