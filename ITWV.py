"""
Finding Disjoint Motifs in a Gene
Unsolved
"""

t = 'GACCACGGTT'
p = 'ACAG'
q = 'CCG'

def InterwovenStrings(t,p,q):
    """ Returns 0 if tw
    substrings = FindWindows(t,p,q)
    if substrings == []:
        return 0



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

print(FindWindows(t,p,q))
        