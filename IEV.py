"""
Calculating Expected Offspring
Solved July 27, 2017
"""

import FileOperations as f

def ExpectedOffspring():
    """ Given number of couples with the following genotypes,
    calculate t he expected number of offspring displaying the
    dominant phenotype in the next generation, under the
    assumption that every couple has 2 offspring:
        1. AA-AA
        2. AA-Aa
        3. AA-aa
        4. Aa-Aa
        5. Aa-aa
        6. aa-aa"""
    
    s = f.LoadFile('\\rosalind_iev.txt').split()
    s = [int(x) for x in s]
    expected = 2*(s[0] + s[1] + s[2] + 0.75*s[3] + 0.5*s[4])
    f.ExportToFile('rosalind_iev_output.txt',str(expected))
    return 
    
ExpectedOffspring()