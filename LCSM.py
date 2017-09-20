"""
Finding a Shared Motif
Solved July 31, 2017
"""

import FileOperations as f

def InAll(template,DNA):
    """ Checks if template string is in *all* DNA strings in list"""
    for substr in DNA:
        if template not in substr:
            return False
    return True


def SharedMotif():
    """ Finds the longest motif shared by all DNA strings in list, FASTA format """
    input = f.LoadFile('\\rosalind_lcsm.txt')
    [Labels,DNA] = f.FASTA(input)
    
    t = min(DNA) # shortest string
    k = len(t) # length of shortest string
    
    # From length of shortest sequence to 0
    for j in range(k,0,-1): # Do all at longest length first
        # From 0 to end of first sequence
        for i in range(k-j+1): # Adjust window
            template = t[i:i+j] #i + j be less than the length of t
            if InAll(template,DNA) == True:
                f.ExportToFile('rosalind_lcsm_output.txt',template)
                return

SharedMotif()