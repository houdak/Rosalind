"""
Edit Distance
Solved September 8, 2017
"""

import FileOperations as f

def MakeMatrixDist(matrix,k,l,p,q):
    """ Makes matrix based on tushar vid algorithm """
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
            if p[i-1] == q[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1]) + 1
    return matrix[k][l]


def EditDistance():
    """ Given 2 strings, FASTA, returns the edit distance """
    input = f.LoadFile('\\rosalind_edit.txt')
    [Labels,[p,q]] = f.FASTA(input)

    k = len(p)
    l = len(q)
    matrix = []

    result = MakeMatrixDist(matrix,k,l,p,q)
    f.ExportToFile('rosalind_edit_output.txt',str(result))
    return

EditDistance()