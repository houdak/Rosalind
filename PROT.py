"""
Translating RNA into Protein
Solved July 27, 2017
"""

import FileOperations as f

# Dictionary matching RNA codons with amino acid
RNA_dict = { 'UUU': 'F',
             'UUC': 'F',
             'UUA': 'L',
             'UUG': 'L',
             'UCU': 'S',
             'UCC': 'S',
             'UCA': 'S',
             'UCG': 'S',
             'UAU': 'Y',
             'UAC': 'Y',
             'UAA': '', #Stop
             'UAG': '', #Stop
             'UGU': 'C',
             'UGC': 'C',
             'UGA': '', #Stop
             'UGG': 'W',
             'CUU': 'L',
             'CUC': 'L',
             'CUA': 'L',
             'CUG': 'L',
             'CCU': 'P',
             'CCC': 'P',
             'CCA': 'P',
             'CCG': 'P',
             'CAU': 'H',
             'CAC': 'H',
             'CAA': 'Q',
             'CAG': 'Q',
             'CGU': 'R',
             'CGC': 'R',
             'CGA': 'R',
             'CGG': 'R',
             'AUU': 'I',
             'AUC': 'I',
             'AUA': 'I',
             'AUG': 'M',
             'ACU': 'T',
             'ACC': 'T',
             'ACA': 'T',
             'ACG': 'T',
             'AAU': 'N',
             'AAC': 'N',
             'AAA': 'K',
             'AAG': 'K',
             'AGU': 'S',
             'AGC': 'S',
             'AGA': 'R',
             'AGG': 'R',
             'GUU': 'V',
             'GUC': 'V',
             'GUA': 'V',
             'GUG': 'V',
             'GCU': 'A',
             'GCC': 'A',
             'GCA': 'A',
             'GCG': 'A',
             'GAU': 'D',
             'GAC': 'D',
             'GAA': 'E',
             'GAG': 'E',
             'GGU': 'G',
             'GGC': 'G',
             'GGA': 'G',
             'GGG': 'G'}


def RNAtoProtein():
    """ Uses RNA_dict to convert RNA string to protein"""
    s = f.LoadFile('\\rosalind_prot.txt')
    codons = []
    protein = ''
    for i in range(0, len(s), 3):
        codons.append(s[i:i+3]) # separate into codons
    for triplet in codons:
        if triplet in ['UAA', 'UAG', 'UGA']: # stop at stop codons
            break
        else:
            protein += RNA_dict[triplet]
    f.ExportToFile('rosalind_prot_output.txt',protein)
    return
    
RNAtoProtein()