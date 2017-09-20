"""
Complementing a Strand of DNA
Solved July 26, 2017
"""

import FileOperations as f

def ReverseComplement():
    """Returns the reverse complement of a string of DNA"""
    s = f.LoadFile('\\rosalind_revc.txt')
    reverse = s[::-1]
    complement = ''
    for nuc in reverse:
        if nuc == 'A':
            complement += 'T'
        elif nuc == 'C':
            complement += 'G'
        elif nuc == 'G':
            complement += 'C'
        elif nuc == 'T':
            complement += 'A'
    f.ExportToFile('rosalind_revc_output.txt', complement)
    return

ReverseComplement()