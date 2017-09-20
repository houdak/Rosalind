"""
Finding a Shared Spliced Motif
Solved September 8, 2017
"""

import FileOperations as f

def MakeMatrix(matrix,k,l,p,q):
    """ Makes a dynamic matrix for finding lcs
    Uses algorithm from Tushar vid!"""
    # initializes and fills in matrix
    # rows for p, columns for q
    matrix = [[0 for _ in range(l+1)] for __ in range(k+1)]
       
    # Go through matrix row by row, comparing p & q
    for i in range(1,k+1): #i for row, j for column
        for j in range(1,l+1):            
            if p[i-1] == q[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])
    return matrix

def LastElement(matrix, p, length):
    """ Given the matrix and length of the lcs,
    will return the last element of the lcs"""
    query = length - 1
    c = len(matrix[0]) #num of columns
    # Step 1 find the first column the max appears in
    # Save the row and column indices
    for col in range(c):        
        r_index = -1
        for row in matrix:
            r_index += 1
            if row[col] == length:
                maxcol = col - 1
                maxrow = r_index - 1
                return [maxcol, maxrow, [p[maxrow]], query]

def ExpandLCS(matrix, p, maxcol, maxrow, query, lcs):
    """ Continues after LastElement to find LCS based on matrix """
    for col in range(maxcol+1):
        r_index = -1
        for row in matrix[:maxrow+1]:
            r_index += 1
            if row[col] == query:
                maxcol = col - 1
                maxrow = r_index - 1
                lcs.append(p[maxrow])
                return [maxcol, maxrow, lcs, query-1]

def LCS():
    input = f.LoadFile('\\rosalind_lcsq.txt')
    [Labels, DNA] = f.FASTA(input)
    p = DNA[0]
    q = DNA[1] 
    
    # Make a matrix that compares the two strings
    k = len(p)
    l = len(q)
    matrix = []   
    matrix = MakeMatrix(matrix,k,l,p,q)
    
    # Use the length of lcs to find the location of the last element
    length = max(  [max(row) for row in matrix]  )
    [maxcol, maxrow, lcs, query] = LastElement(matrix, p, length)
    
    # Expand the lcs by finding where the next lowest # in the matrix occurs
    while len(lcs) < length:
        [maxcol, maxrow, lcs, query] = ExpandLCS(matrix, p, maxcol, maxrow, query, lcs)
    
    lcs = ''.join(list(reversed(lcs)))
    f.ExportToFile('rosalind_lcsq_output.txt',lcs)
    return

LCS()