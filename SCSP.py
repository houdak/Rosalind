"""
Interleaving Two Motifs
Solved September 15, 2017
"""

import FileOperations as f

# Length of supersequence = (sum of lengths of given 2 strings)
 # - length of LCS of two given strings

def MakeMatrixSCS(matrix,k,l,p,q):
    """ Makes matrix based on geeksforgeeks algorithm """
    # initializes and fills in matrix
    # rows for p, columns for q
    matrix = [[0 for _ in range(l+1)] for __ in range(k+1)]
    matrix[0] = [x for x in range(len(matrix[0]))]
    i = -1
    for row in matrix:
        i += 1
        row[0] = i
    
    # Go through matrix row by row, comparing p & q
    for i in range(1,k+1):
        for j in range(1,l+1):
            left = matrix[i-1][j]
            north = matrix[i][j-1]
            diag = matrix[i-1][j-1]
            
            if p[i-1] == q[j-1]:
                matrix[i][j] = diag + 1
            else:
                matrix[i][j] = min([left,north]) + 1
    
    return matrix

def InterpretMatrixSCS(matrix,k,l,p,q):
    """ Returns shortest common supersequence by interpreting dynamic matrix """
    # i = row, j = col, p = row, q = col
    scs = []
    # Start at the bottom-rightmost corner
    i = k
    j = l
    
    while i > 0 and j > 0:
        # If characters match...
        if p[i-1] == q[j-1]:
            scs.insert(0,p[i-1])
            i = i-1
            j = j-1
        elif matrix[i-1][j] > matrix[i][j-1]:
            scs.insert(0,q[j-1])
            j = j-1
        else:
            scs.insert(0,p[i-1])
            i = i-1
    
    if len(scs) == matrix[k][l]:
        return ''.join(scs)
    elif i > j:
        while i > 0:
            scs.insert(0,p[i-1])
            i = i - 1
    elif j > i:
        while j > 0:
            scs.insert(0,q[j-1])
            j = j - 1
    
    return ''.join(scs)
                 
    
def InterleavingMotifs():
    [p,q] = f.LoadFile('\\rosalind_scsp.txt').splitlines()
    
    k = len(p)
    l = len(q)
    matrix = []
    matrix = MakeMatrixSCS(matrix,k,l,p,q)

    scs = InterpretMatrixSCS(matrix,k,l,p,q)
    f.ExportToFile('rosalind_scsp_output.txt',scs)
    return
    
InterleavingMotifs()