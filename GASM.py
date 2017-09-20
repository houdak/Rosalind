"""
Genome Assembly Using Reads
Solved August 27, 2017
"""

import FileOperations as f
import FrequentOperations as p
import random


def MaxOverlap(node, Graph):
    """ Returns node with the most overlap """
    overlaps = {}
    for i in Graph:
        overlaps[p.Overlap(node,i)] = i
    
    max_overlap = max(overlaps)
    
    return overlaps[max_overlap]
    

def CyclicWithRC():
    """ Generates cyclic syperstring of minimal length
    with every read OR its reverse complement """
    kmers = f.LoadFile('\\rosalind_gasm.txt').splitlines()
    Graph = p.DeBruijnRC(kmers)
    
    # Get first node
    cycle = []
    node = random.choice(list(Graph.keys()))
    
    # extend cycle
    for i in range(len(Graph)//2):
        cycle.append(node)
        if Graph[node][0] in Graph:
            node = Graph[node][0]
        else:
            # Find node with most overlap
            # Use that one          
            node = MaxOverlap(Graph[node][0],Graph)
    
    # Merge into one string based on overlap
    superstring = cycle[0]
    for i in cycle[1:]:
        superstring = p.Combine(superstring,i)
    
    # Get rid of overlap at end of string
    k = len(superstring)
    for i in range(k-1,0,-1):
        if superstring[:i] == superstring[k-i:]:
            f.ExportToFile('rosalind_gasm_output.txt',superstring[:k-i])
            return

CyclicWithRC()