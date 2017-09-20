"""
Reversal Distance
Solved September 7, 2017
"""

import FileOperations as f
from itertools import permutations
from FrequentOperations import CountBreakagePoints
from FrequentOperations import TransformIndex

# Reversal Distance
def GenerateReversals(q):
    """ Generates all possible reversals of a given permutation """
    reversals = []
    pairs = list(permutations([x for x in range(11)],2))
    
    # remove pairs where j < i
    newpairs = []
    for tup in pairs:
        if tup[0] +1 < tup[1]:
            newpairs.append(tup)
    pairs = newpairs
    
    for i,j in pairs:
        newq = q[:i] + list(reversed(q[i:j])) + q[j:]
        if newq != q:
            reversals.append(newq)
    return reversals 

def Generate2Reversals(q):
    """ Generates all possible *double* reversals of a given permutation
    Used if no breakage points removed from a single reversal"""
    reversals2 = []
    reversals = GenerateReversals(q)
    pairs = list(itertools.permutations([x for x in range(11)],2))
    # remove pairs where j < i
    newpairs = []
    for tup in pairs:
        if tup[0] +1 < tup[1]:
            newpairs.append(tup)
    pairs = newpairs
    
    for pattern in reversals:
        for i,j in pairs:
            newpattern = pattern[:i] + list(reversed(pattern[i:j])) + pattern[j:]
            if newpattern != pattern:
                reversals2.append(newpattern)
    return reversals2
        
def ReversalDistance(p,q):
    """ Computes reversal distance from p to q """
    q = TransformIndex(p,q)
    
    # If p & q are equal, distance = 0
    if p == q:
        return 0
    
    else:
        distance = 0
        while CountBreakagePoints(q) != 0:
            breakage = CountBreakagePoints(q)
            # Generate all the possible reversals
            reversals = GenerateReversals(q)
            # Go through each one
            # Find the one that removes the most breakage points
            minbreakage = breakage
            for pattern in reversals:
                if CountBreakagePoints(pattern) < minbreakage:
                    q = pattern
                    minbreakage = CountBreakagePoints(pattern)
            """If no closer pattern can be found...
               generate all possible 2 reversals and try again"""
            if minbreakage == breakage:
                distance += 1
                reversals = Generate2Reversals(q)
                for pattern in reversals:
                    if CountBreakagePoints(pattern) < minbreakage:
                        q = pattern
                        minbreakage = CountBreakagePoints(pattern)
            
            # Replace q with closer pattern, repeat until q == p    
            distance += 1
    return str(distance)

def FindReversalDistances():
    """ Computes multiple reversal distances
    between several pairs of strings """
    input = f.LoadFile('\\rosalind_rear.txt').splitlines()
    k = len(input)
    
    p_str = [input[i].split() for i in range(0,k+1,3)]
    q_str = [input[i].split() for i in range(1,k+1,3)]
    p_all = []
    q_all = []
    for line in p_str:
        p_all.append([int(x) for x in line])
    for line in q_str:
        q_all.append([int(x) for x in line])
    
    distances = []
    for i in range(len(p_all)):
        p = p_all[i]
        q = q_all[i]
        distances.append(ReversalDistance(p,q))
    
    f.ExportToFile('rosalind_rear_output.txt',' '.join(distances))    
    return

FindReversalDistances()