"""
Enumerating k-mers Lexicographically
Solved August 1, 2017
"""

import FileOperations as f

def Lex():
    """ Given a collection of symbols and a +integer n, returns
    all strings of length n that can be formed from the alphabet,
    ordered lexicographically"""
    input = f.LoadFile('\\rosalind_lexf.txt').splitlines()
    sym = input[0].split()
    r = int(input[1])
    
    n = len(sym)
    lex_list = []
    
    # for first round
    for _ in range((n**r)//n): # should match 1/n of total in list
        for i in sym:
            lex_list.append(i)
    lex_list = sorted(lex_list)
    
    # First go through whole list correct number of times (j)
    m = (n**r)//n
    k = 0
    for j in range(1,r):      
        i = -1 # index resets each go-through
        m = m // n # Smaller number of each sym in a row each round
        k += 1 # More cycles each time to get through list
        
        for __ in range(n**k):
            for s in sym:
                for _ in range(m):
                    i += 1
                    lex_list[i] += s
    
    f.ExportToFile('rosalind_lexf_output.txt', '\n'.join(lex_list))
    return
    
Lex()