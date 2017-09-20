"""
Introduction to Pattern Matching
Solved September 19, 2017
"""

import FileOperations as f
import time

def BranchOff(trie,string,parent,x):
    """ Adds a new branch starting from the parent
    Parent = last matching letter, or root if none """
    p = parent[1] # name of parent
    n = trie[-1][1] + 1 # name of last node + 1
    for letter in string[x:]:
        trie.append((p,n,letter))
        p = n # updates to previous letter
        n += 1
    return trie

def FindParent(trie,string):
    """ Goes through trie to find last matching letter (parent).
    Returns root, and index of first non-matching letter"""
    x = 0 # letter of string you are looking for
    # matches are the tups  that have a matching letter and have correct parent
    # simple here, but more complicated when the parent needs to be followed...
    matches = [tup for tup in trie if (tup[0] == 1 and tup[2] == string[x])]
    if matches == []: # means no match was ever found... meaning root is parent
        return trie[0], 0 # index first non-matching number is the first one (0)
    
    newmatches = []    
    # Look further down tree, following parent in matches
    while x < len(string): # can only go down as far as the string goes        
        x += 1
        for match in matches:
            newmatches = [tup for tup in trie if (tup[0] == match[1] and tup[2] == string[x])]
        if newmatches != []:
            matches = newmatches #update and continue down the string!
        else:
            return matches[0], x # if there are multiple, just return one of them
                    
def Trie():
    strings = f.LoadFile('\\rosalind_trie.txt').splitlines()
    """ Puts together all of above functions to make a trie! """
    trie = [(0,1,'')] # root!
    for string in strings:
        [parent,x] = FindParent(trie,string)
        trie = BranchOff(trie,string,parent,x)
    
    # Format for printing!
    trief = []
    for tup in trie[1:]: # Don't include root
        trief.append(' '.join([str(x) for x in tup]))
    f.ExportToFile('rosalind_trie_output.txt','\n'.join(trief))
    return
    
Trie()    