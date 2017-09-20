"""
Finding a Motif in DNA
Solved July 27, 2017
"""

import FileOperations as f

def FindMotif():
    """ Returns all indices where given motif can be found in string"""
    input = f.LoadFile('\\rosalind_subs.txt').splitlines()
    s = input[0]
    t = input[1]
    
    k = len(t)
    motifs = []
    for i in range(len(s)-k):
        if s[i:i+k] == t:
            motifs.append(str(i+1))
    f.ExportToFile('rosalind_subs_output.txt',' '.join(motifs))        
    return

FindMotif()