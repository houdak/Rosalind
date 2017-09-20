"""
Inferring mRNA from Protein
Solved July 31, 2017
"""

import FileOperations as f

# Value in dict represents number of possible codons
mRNA_dict = {'F': 2,
             'L': 6,
             'S': 6,
             'Y': 2,
             'X': 3, # X == stop
             'C': 2,
             'W': 1,
             'P': 4,
             'H': 2,
             'Q': 2,
             'R': 6,
             'I': 3,
             'M': 1,
             'T': 4,
             'N': 2,
             'K': 2,
             'V': 4,
             'A': 4,
             'D': 2,
             'E': 2,
             'G': 4}


def ProteinTomRNA():
    """ Returns total number of different RNA strings from which the
    protein could have been translated, modulo 1000000"""
    protein = f.LoadFile('\\rosalind_mrna.txt')
    protein += 'X' # add stop codon to end
    combo = 1
    for aa in protein:
        if aa in mRNA_dict:
            combo = combo*mRNA_dict[aa]
    f.ExportToFile('rosalind_mrna_output.txt', str(combo % 1000000))
    return

ProteinTomRNA()