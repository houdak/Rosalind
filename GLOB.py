"""
Global Alignment with Scoring Matrix
Solved September 10, 2017
"""

import FileOperations as f

""" Dictionary with scores according to BLOSUM62 scoring matrix """
BLOSUM62_dict = {
'A':{'A':4, 'C':0, 'D':-2,'E':-1,'F':-2,'G':0, 'H':-2,'I':-1,'K':-1,'L':-1,'M':-1,'N':-2,'P':-1,'Q':-1,'R':-1,'S':1, 'T':0, 'V':0, 'W':-3,'Y':-2},
'C':{'A':0, 'C':9, 'D':-3,'E':-4,'F':-2,'G':-3,'H':-3,'I':-1,'K':-3,'L':-1,'M':-1,'N':-3,'P':-3,'Q':-3,'R':-3,'S':-1,'T':-1,'V':-1,'W':-2,'Y':-2},
'D':{'A':-2,'C':-3,'D':6, 'E':2, 'F':-3,'G':-1,'H':-1,'I':-3,'K':-1,'L':-4,'M':-3,'N':1, 'P':-1,'Q':0, 'R':-2,'S':0, 'T':-1,'V':-3,'W':-4,'Y':-3},
'E':{'A':-1,'C':-4,'D':2, 'E':5, 'F':-3,'G':-2,'H':0, 'I':-3,'K':1, 'L':-3,'M':-2,'N':0, 'P':-1,'Q':2, 'R':0, 'S':0, 'T':-1,'V':-2,'W':-3,'Y':-2},
'F':{'A':-2,'C':-2,'D':-3,'E':-3,'F':6, 'G':-3,'H':-1,'I':0, 'K':-3,'L':0, 'M':0, 'N':-3,'P':-4,'Q':-3,'R':-3,'S':-2,'T':-2,'V':-1,'W':1, 'Y':3 },
'G':{'A':0, 'C':-3,'D':-1,'E':-2,'F':-3,'G':6, 'H':-2,'I':-4,'K':-2,'L':-4,'M':-3,'N':0, 'P':-2,'Q':-2,'R':-2,'S':0, 'T':-2,'V':-3,'W':-2,'Y':-3},
'H':{'A':-2,'C':-3,'D':-1,'E':0, 'F':-1,'G':-2,'H':8, 'I':-3,'K':-1,'L':-3,'M':-2,'N':1, 'P':-2,'Q':0, 'R':0, 'S':-1,'T':-2,'V':-3,'W':-2,'Y':2 },
'I':{'A':-1,'C':-1,'D':-3,'E':-3,'F':0, 'G':-4,'H':-3,'I':4, 'K':-3,'L':2, 'M':1, 'N':-3,'P':-3,'Q':-3,'R':-3,'S':-2,'T':-1,'V':3, 'W':-3,'Y':-1},
'K':{'A':-1,'C':-3,'D':-1,'E':1, 'F':-3,'G':-2,'H':-1,'I':-3,'K':5, 'L':-2,'M':-1,'N':0, 'P':-1,'Q':1, 'R':2, 'S':0, 'T':-1,'V':-2,'W':-3,'Y':-2},
'L':{'A':-1,'C':-1,'D':-4,'E':-3,'F':0, 'G':-4,'H':-3,'I':2, 'K':-2,'L':4, 'M':2, 'N':-3,'P':-3,'Q':-2,'R':-2,'S':-2,'T':-1,'V':1, 'W':-2,'Y':-1},
'M':{'A':-1,'C':-1,'D':-3,'E':-2,'F':0, 'G':-3,'H':-2,'I':1, 'K':-1,'L':2, 'M':5, 'N':-2,'P':-2,'Q':0, 'R':-1,'S':-1,'T':-1,'V':1, 'W':-1,'Y':-1},
'N':{'A':-2,'C':-3,'D':1, 'E':0, 'F':-3,'G':0, 'H':1, 'I':-3,'K':0, 'L':-3,'M':-2,'N':6, 'P':-2,'Q':0, 'R':0, 'S':1, 'T':0, 'V':-3,'W':-4,'Y':-2},
'P':{'A':-1,'C':-3,'D':-1,'E':-1,'F':-4,'G':-2,'H':-2,'I':-3,'K':-1,'L':-3,'M':-2,'N':-2,'P':7, 'Q':-1,'R':-2,'S':-1,'T':-1,'V':-2,'W':-4,'Y':-3},
'Q':{'A':-1,'C':-3,'D':0, 'E':2, 'F':-3,'G':-2,'H':0, 'I':-3,'K':1, 'L':-2,'M':0, 'N':0, 'P':-1,'Q':5, 'R':1, 'S':0, 'T':-1,'V':-2,'W':-2,'Y':-1},
'R':{'A':-1,'C':-3,'D':-2,'E':0, 'F':-3,'G':-2,'H':0, 'I':-3,'K':2, 'L':-2,'M':-1,'N':0, 'P':-2,'Q':1, 'R':5, 'S':-1,'T':-1,'V':-3,'W':-3,'Y':-2},
'S':{'A':1, 'C':-1,'D':0, 'E':0, 'F':-2,'G':0, 'H':-1,'I':-2,'K':0, 'L':-2,'M':-1,'N':1, 'P':-1,'Q':0, 'R':-1,'S':4, 'T':1, 'V':-2,'W':-3,'Y':-2},
'T':{'A':0, 'C':-1,'D':-1,'E':-1,'F':-2,'G':-2,'H':-2,'I':-1,'K':-1,'L':-1,'M':-1,'N':0, 'P':-1,'Q':-1,'R':-1,'S':1, 'T':5, 'V':0, 'W':-2,'Y':-2},
'V':{'A':0, 'C':-1,'D':-3,'E':-2,'F':-1,'G':-3,'H':-3,'I':3, 'K':-2,'L':1, 'M':1, 'N':-3,'P':-2,'Q':-2,'R':-3,'S':-2,'T':0, 'V':4, 'W':-3,'Y':-1},
'W':{'A':-3,'C':-2,'D':-4,'E':-3,'F':1, 'G':-2,'H':-2,'I':-3,'K':-3,'L':-2,'M':-1,'N':-4,'P':-4,'Q':-2,'R':-3,'S':-3,'T':-2,'V':-3,'W':11,'Y':2 },
'Y':{'A':-2,'C':-2,'D':-3,'E':-2,'F':3, 'G':-3,'H':2, 'I':-1,'K':-2,'L':-1,'M':-1,'N':-2,'P':-3,'Q':-1,'R':-2,'S':-2,'T':-2,'V':-1,'W':2, 'Y':7 },
}

def MakeMatrixGlobal(matrix,k,l,p,q):
    """ Constructs dynamic matrix for alignment based on BLOSUM62 """
    # initializes and fills in matrix
    # rows for p, columns for q
    matrix = [[0 for _ in range(l+1)] for __ in range(k+1)]
    matrix[0] = [-5*x for x in range(len(matrix[0]))]
    i = 1
    for row in matrix:
        i += -1
        row[0] = i*5
    
    # Go through matrix row by row, comparing p & q
    gap = -5
    for i in range(1,k+1):
        for j in range(1,l+1):
            leftscore = matrix[i][j-1] + gap
            northscore = matrix[i-1][j] + gap
            diagscore = matrix[i-1][j-1] + BLOSUM62_dict[p[i-1]][q[j-1]]
            matrix[i][j] = max(leftscore,northscore,diagscore)
    return matrix[k][l]
    

def GlobalAlignment():
    """ Uses MakeMatrix to return the maximum alignment score
    between 2 DNA strings (FASTA)"""
    input = f.LoadFile('\\rosalind_glob.txt')
    [Labels,[p,q]] = f.FASTA(input)

    k = len(p)
    l = len(q)
    matrix = []
    maxalign = MakeMatrixGlobal(matrix,k,l,p,q)   
    f.ExportToFile('rosalind_glob_output.txt',str(maxalign))
    return 

GlobalAlignment()