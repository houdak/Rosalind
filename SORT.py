"""
Sorting by Reversals
Solved September 7, 2017
"""

import FileOperations as f
from itertools import permutations
from FrequentOperations import CountBreakagePoints
from FrequentOperations import TransformIndex

def GenerateReversalsWithPairs(q):
    """ Given a permutation, generates all possible reversals
    along with the indices encoding each reversal"""
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
            reversals.append([newq,i,j])
    return reversals
    
def ReversalDistanceWithPairs(p,q):
    """ Calculates reversal distance from p to q while also
    returning the indices encoding those each reversal """
    # Make it easier to work with by changing index to match p
    # as if p = [1,2,3,4,5,6,7,8,9,10]
    q = TransformIndex(p,q)
    
    # If p & q are equal, distance = 0
    if p == q:
        return 0
    
    else:
        distance = 0
        indices_all = []
        while CountBreakagePoints(q) != 0:
            breakage = CountBreakagePoints(q)
            # Generate all the possible reversals
            reversals = GenerateReversalsWithPairs(q)
            # Go through each one
            # Find the one that removes the most breakage points
            minbreakage = breakage
            for item in reversals:
                pattern = item[0]
                if CountBreakagePoints(pattern) < minbreakage:
                    q = pattern
                    indices = [item[1]+1,item[2]]
                    minbreakage = CountBreakagePoints(pattern)
            """If no closer pattern can be found...
               generate all possible 2 reversals and try again
            if minbreakage == breakage:
                distance += 1
                reversals = Generate2Reversals(q)
                for pattern in reversals:
                    if CountBreakagePoints(pattern) < minbreakage:
                        q = pattern
                        minbreakage = CountBreakagePoints(pattern)"""
            
            # Replace q with closer pattern, repeat until q == p    
            indices_all .append(indices)
            distance += 1
    return distance, indices_all   

def SortingByReversals():
    """ Uses ReversalDistanceWithPairs() to report back
    reversal distance and pairs encoding the reversal """
    input = f.LoadFile('\\rosalind_sort.txt').splitlines()
    q = [int(x) for x in input[0].split()]
    p = [int(x) for x in input[1].split()]
    
    output = []
    [distance,indices] = ReversalDistanceWithPairs(p,q)
    output.append(str(distance))
    for i in indices:
        output.append(' '.join(str(x) for x in i))
    f.ExportToFile('rosalind_sort_output.txt','\n'.join(output))   
    return
    
SortingByReversals()