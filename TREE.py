"""
Completing a Tree
Solved August 20, 2017
"""

import FileOperations as f

def CompletingaTree():
    """ Given positive integer n and an adjacency list
    corresponding to a graph on n nodes that contains no cycles,
    returns the minimum number of edges that can be added to
    the graph to product a tree"""
    input = f.LoadFile('\\rosalind_tree.txt').splitlines()
    n = int(input[0])
    edges = len(input[1:])
    minimum = str(n - edges - 1)
    f.ExportToFile('rosalind_tree_output.txt',minimum)
    return
    
CompletingaTree()