"""
Genome Assembly with Perfect Coverage
Solved August 27, 2017
"""

import FileOperations as f
import random

def Cyclic():
    """ Given several DNA strings, returns cyclic syperstring """
    Graph = f.LoadFile('\\rosalind_pcov.txt').splitlines()
    
  # Construct adjacency dict
    adj_dict = {}
    for kmer in Graph:
        adj_dict[kmer[:-1]] = 0  

    for i in adj_dict:
        for j in Graph:
            if i == j[:-1]: # Look for strings with that prefix
                adj_dict[i] = j[1:] #If so, add suffix    

    cycle = []
    node = random.choice(list(adj_dict.keys()))
    
    for _ in range(len(Graph)):
        cycle.append(node)
        node = adj_dict[node]
    
    superstring = ''
    for i in cycle:
        superstring += i[-1]
    
    f.ExportToFile('rosalind_pcov_output.txt',superstring)
    return
    
Cyclic()