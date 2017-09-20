"""
Ordering Strings of Varying Length Lexicographically
Solved August 6, 2017
"""

import FileOperations as f
from FrequentOperations import Lex

def OrderDifLengths():
    """ Given a permutation A and positive integer n, returns
    all strings of length n formed from A, ordered lexicographically
    (based on the order in which the symbols are given)"""    
    input = f.LoadFile('\\rosalind_lexv.txt').splitlines()
    alph = input[0].split()
    n = int(input[1])
    
    # Get lex list at each length
    lex_list = []
    for l in range(n+1):
        lex_list.extend(Lex(alph,l))
    
    # Sort lex list by ordered alphabet
    # First time using lambda :)
    sorted_lex = sorted(lex_list, key = lambda word: [alph.index(c) for c in word])
    f.ExportToFile('rosalind_lexv_output.txt','\n'.join(sorted_lex))
    return

OrderDifLengths()