"""
Edit Distance Alignment
Solved September 9, 2017
"""

import FileOperations as f

def InterpretMatrix(matrix,k,l,p,q):
    """ Gives alignment strings based on matrix"""
    # k = row, l = column, p = k, q = l
    p_aligned = []
    q_aligned = []
    
    i = k
    j = l
    while i > 0:
        diagonal = matrix[i-1][j-1]
        left = matrix[i][j-1]
        north = matrix[i-1][j]
        # if value not less than diagonal & left, symbols match
        if matrix[i][j] == min(diagonal,left,north):
            p_aligned.insert(0,p[i-1])
            q_aligned.insert(0,q[j-1])
            i = i-1
            j = j-1
        
        else:
            # favor going left, results in better alignment
            if matrix[i][j] - 1 == left:
                # deletion in p
                p_aligned.insert(0,'-')
                q_aligned.insert(0,q[j-1])
                j = j-1
            elif matrix[i][j] - 1 == north:
                # deletion in q
                p_aligned.insert(0,p[i-1])
                q_aligned.insert(0,'-')
                i = i-1
            elif matrix[i][j] - 1 == diagonal:
                # substition
                p_aligned.insert(0,p[i-1])
                q_aligned.insert(0,q[j-1])
                i = i-1
                j = j-1

    return p_aligned,q_aligned        

def MakeMatrixDist(matrix,k,l,p,q):
    """ Constructs dynamic matrix based on Tushar vid algorithm """
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
    return matrix[k][l], matrix

def EditDistanceAlignment():
    """ Uses MakeMatrix and InterpretMatrix to return alignments """
    input = f.LoadFile('\\rosalind_edta.txt')
    [Labels,[p,q]] = f.FASTA(input)

    k = len(p)
    l = len(q)
    matrix = []
    [editdistance,matrix] = MakeMatrixDist(matrix,k,l,p,q)
    
    [p_aligned,q_aligned] = InterpretMatrix(matrix,k,l,p,q)
    output = [str(editdistance),''.join(p_aligned),''.join(q_aligned)]
    f.ExportToFile('rosalind_edta_output.txt','\n'.join(output))
    return

EditDistanceAlignment()