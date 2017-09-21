"""
Finding Disjoint Motifs in a Gene
Solved September 20, 2017
"""

import FileOperations as f

def MakeMatrixWoven(p,q,w):
    """ Makes dynamic matrix to decern whether
    window (w) is an interweaving of p & q """
    # initialize matrix
    k = len(p)
    l = len(q)
    # row/i = p, col/j = q
    matrix = [['' for j in range(l+1)] for i in range(k+1)]
    # fill in first row & col
    matrix[0][0] = 'T'
    for j in range(1,l+1):
        refchar = w[j-1]
        if (    q[j-1] == refchar
            and matrix[0][j-1] == 'T' ):
            matrix[0][j] = 'T'
        else:
            matrix[0][j] = 'F'
    
    for i in range(1,k+1):
        refchar = w[i-1]
        if (    p[i-1] == refchar
            and matrix[i-1][0] == 'T'):
            matrix[i][0] = 'T'
        else:
            matrix[i][0] = 'F'
    
    # Now fill up the rest!
    for i in range(1,k+1): # row
        for j in range(1,l+1): # col
            refchar = w[i+j-1]
            if (    p[i-1] == refchar
                and matrix[i-1][j] == 'T'):
                matrix[i][j] = 'T'
            elif (    q[j-1] == refchar
                  and matrix[i][j-1] == 'T'):
                matrix[i][j] = 'T'
            else:
                matrix[i][j] = 'F'
        
    if matrix[k][l] == 'T':
        return '1'
    else:
        return '0'

def InterwovenStrings(t,p,q):
    """ Returns 1 if substring of t
    is p &q interwoven, 0 if false. """
    substrings = FindWindows(t,p,q)
    if substrings == []:
        return '0'
    else:
        # Check if substring actually is p&q interwoven
        for window in substrings:
            if MakeMatrixWoven(p,q,window) == '1':
                return '1'
        return '0'

def FindWindows(t,p,q):
    """ Looks for regions in t which match the following properties:
    (1) Start with first char in p or q
    (2) len(window) == len(p) + len(q)
    (3) all characters in window are in either p or q
    returns list of those windows as strings """
    k = len(p) + len(q)
    windows = []
    for i in range(0,len(t)-k+1):
        temp_window = t[i:i+k]
        if (    temp_window[0] != p[0]
            and temp_window[0] != q[0]):
            continue # won't work, not right starting char
        else:
            check = True
            for char in temp_window:
                if (char not in p and char not in q):
                    check = False
                    break
            if check == True:
                windows.append(temp_window)
    return windows

def DisjointMotifs():
    """ Uses above functions to make matrix pitting
    multiple strings against each other """
    input = f.LoadFile('\\rosalind_itwv.txt').splitlines()
    t = input[0]
    strings = input[1:]
    n = len(strings)
    
    # initialize matrix
    matrix = [['' for y in range(n)] for x in range(n)]
    # Solve for each p x q
    for x in range(n):
        for y in range(n):
            p = strings[x]
            q = strings[y]
            matrix[x][y] = InterwovenStrings(t,p,q)
    
    # Format and write into file!
    output = [' '.join(row) for row in matrix]
    f.ExportToFile('rosalind_itwv_output.txt','\n'.join(output))   
    return

DisjointMotifs()    