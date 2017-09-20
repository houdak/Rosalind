"""
Newick Format with Edge Weights
Solved August 21, 2017
"""

import FileOperations as f
from Bio import Phylo
import io

def NewickDistanceWeights():
    """ Gives distances between pair of nodes in trees (Newick) """
    input = f.LoadFile('\\rosalind_nkew.txt').splitlines()
    
    # Separate into Trees and Pairs
    Trees = []
    Pairs = []
    for line in input:
        if ';' in line:
            Trees.append(line)
        elif line != '':
            Pairs.append(line.split())
    
    # For each tree in the file
    distances = []
    for i in range(len(Trees)):
        tree = Phylo.read(io.StringIO(Trees[i]),'newick')
        # If no edgeweights specified, use code below (weight=1)
        """clades = tree.find_clades()
        for clade in clades:
            clade.branch_length = 1"""
        
        d = tree.distance(Pairs[i][0],Pairs[i][1])
        distances.append(str(d))
    
    f.ExportToFile('rosalind_nkew_output.txt',' '.join(distances))
    return
   
NewickDistanceWeights() 