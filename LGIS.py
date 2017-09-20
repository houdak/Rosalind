"""
Longest Increasing Subsequence
Solved September 6, 2017
"""

import FileOperations as f
                                                                                
def LIS(seq):
    """ Returns longest increasing subsequence in a given sequence"""
    #initialize dynamic array with 1, since lis is at least 1 at each position
    dyn = [1 for x in range(len(seq))]

    i = 1
    j = 0
    
    # Generate array based on algorithm (Tushar Roy vid)
    while i<len(seq):
        if seq[j] < seq[i]:
            dyn[i] = max([dyn[i],dyn[j] + 1])
            j += 1
            if j == i:
                j = 0
                i += 1
        else:
            j += 1
            if j == i:
                j = 0
                i += 1
    
    # Use array to get actual sequence
    start = max(dyn)
    start_index = dyn.index(start)
    lis = [seq[start_index]]
    
    for i in range(start_index-1,-1,-1):
        if (    seq[i] < lis[0]
            and dyn[i] == start - 1):
            lis.insert(0,seq[i])
            start = start - 1
    
    return lis 


def LongestIncDec():
    """ Returns Longest Increasing Subsequence and Longest Decreasing Subsequence,
    given a positive integer n followed by a permutation of length n"""
    input = f.LoadFile('\\rosalind_lgis.txt').splitlines()
    p = input[1].split()
    p = [int(x) for x in p]    
    rev_p = list(reversed(p))
    
    # Get decreasing by submitting reversed permutation,
    # and returning reversed result
    increasing = LIS(p)
    decreasing = list(reversed(LIS(rev_p)))        
                          
    output = [(' '.join(str(x) for x in increasing)),(' '.join(str(x) for x in decreasing))]                                                                        
    f.ExportToFile('rosalind_lgis_output.txt', '\n'.join(output))
    return

LongestIncDec()