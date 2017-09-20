"""
Creating a Restriction Map
Unsolved 
"""

import FileOperations as f
from math import sqrt
from FrequentOperations import RemoveDuplicates
from copy import copy

def FindN(C):
    """given result of nC2, returns n """
    return int((1 + sqrt(1 + 8*C)) // 2)

def MinowskiDiff(s):
    s = sorted(s)
    k = len(s)
    minow = []
    for i in range(k):
        for j in range(i+1,k):
            minow.append(s[j]-s[i])
    return sorted(minow)

def CheckAll(set1,set2, trueset):
    """ Checks if all items in set1 are in set2
    the correct number of times! """
    test_set = list(copy(set2))
    test_set.append(max(trueset))
    for item in set1:
        if item not in test_set:
            return False
        else:
            test_set.remove(item)
    return True


def RestrictionMap():
    diff = f.LoadFile('\\rosalind_pdpl.txt').split()
    diff = sorted([int(x) for x in diff])

    # find length L based on len(diff)
    C = len(diff)
    length = FindN(C)

    """ Known values are 0 and max(diff).
    Remove max(diff) from diff """
    trueset = [0,max(diff)]
    diff.remove(max(diff))

    # Branch and Bound Algorithm
    possible_sets = [copy(list(trueset))]
    small = 0
    large = len(diff) - 1
    while len(possible_sets[0]) < length:
        # Exit while loop if large < 0
        if small > large:
            break
        new_possibles = []
        # Add largest difference to expand as two possible branches
        # Can be equal to either smallest difference or largest
        for s in possible_sets:
            new_possibles.append(sorted(s + [diff[large]]))
            new_possibles.append(sorted(s + [diff[small]]))
        new_possibles = RemoveDuplicates(new_possibles)
        # Check if any can be removed based on incombatible differences
        compatible_sets = []
        for s in new_possibles:
            mino = MinowskiDiff(s)
            if CheckAll(mino, diff,trueset) == True:
                compatible_sets.append(s)
        
        # Check if neither work...
        if compatible_sets == []:
            small += 1
            large += -1
            continue
        # Reset, change small/large
        possible_sets = compatible_sets
        small += 1
        large += -1
        print(len(possible_sets[0]),len(possible_sets))
        
    # Once loop is exited:
        
    return possible_sets
                
        
                        
print(RestrictionMap())