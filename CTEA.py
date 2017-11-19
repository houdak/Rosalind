"""
Counting Optimal Alignments
Unsolved
"""

import FileOperations as f

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
                a = 0
            else:
                a = 1
            matrix[i][j] = min(matrix[i-1][j-1] + a,matrix[i][j-1] + 1,matrix[i-1][j] + 1)  
    return matrix[k][l], matrix


def ConstructPath(matrix,k,l,p,q):

    start = [(k,l,1)]
    # Last number indicates total occurances
    # Used to count total optimal paths
    
    i = k
    j = l
    
    while start[0][0:2] != (0,0):
        # test out all possible directions
        new_start = []
        for pos in start:
            i = pos[0]
            j = pos[1]
            occurances = pos[2]
                       
            # First make all possible directions
            diagonal = matrix[i-1][j-1]
            left = matrix[i][j-1]
            north = matrix[i-1][j]
            
            # possible values based on whether p & q match
            if p[i-1] == q[j-1]:
                a = 0
            else:
                a = 1
            
            # Rewrite as possible next values
            pos_diag = matrix[i][j] - a
            pos_other = matrix[i][j] - 1
            pos_dir = []
            
            # Check each direction based on fit
            if (    left == pos_other
                and i - 1 >= 0        ):
                pos_dir.append('left')
            
            if (    north == pos_other
                and j - 1 >= 0         ):
                pos_dir.append('north')

            if (    diagonal == pos_diag
                and i - 1 >= 0
                and j - 1 >= 0       ):
                pos_dir.append('diagonal')
            
            # Transfer new starts into matrix
            for direc in pos_dir:            
                new_start.append(FollowDirection(i,j,occurances,direc))
            
            if pos_dir == []:
                new_start.append((0,0) + (occurances,))
        
        """ Once we've gone through all previous starts, need to
        rewrite, taking into account duplicates, getting new occurances
        counts for each, to get accurate final count """
        start = MergeDuplicates(new_start)

    return start[0][2]
        

def MergeDuplicates(new_start):
    merged_start = []
    for s in new_start:
        # look for potential duplicate
        duplicate = [x for x in merged_start if x[0:2] == s[0:2]]
        # If no duplicates, add in new start
        if duplicate == []:
            merged_start.append(s)
        # if there is a duplicate, merge
        else:
            merge = s[0:2] + (duplicate[0][2]+s[2],)
            merged_start.remove(duplicate[0])
            merged_start.append(merge)
          
    return merged_start  


def FollowDirection(i,j,occurances, next_dir):
    """ Given the direction to follow,
    returns new i & j & matrix val at that point"""
    
    if next_dir == 'diagonal':
        i = i - 1
        j = j - 1
    
    elif next_dir == 'left':
        j = j - 1 # i stays same
    
    elif next_dir == 'north':
        i = i - 1 # j stays same
    
    return (i,j,occurances)


def CountOptimalAlignments():
    """ Uses MakeMatrix and ConstructPath to return
    number of optimal alignments. Repeats ConstructPath multiple times to get
    all possible optimal alignments """
    input = f.LoadFile('\\rosalind_ctea.txt')
    [Labels,[p,q]] = f.FASTA(input)

    k = len(p)
    l = len(q)
    matrix = []
    [editdistance,matrix] = MakeMatrixDist(matrix,k,l,p,q)
    
    return ConstructPath(matrix,k,l,p,q) % 134217727

print(CountOptimalAlignments())