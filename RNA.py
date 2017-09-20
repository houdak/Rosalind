"""
Transcribing DNA into RNA
Solved July 26, 2017

Originally used for loop, improved with list comprehension!
"""

import FileOperations as f

def DNAtoRNA():
    """Converts string of DNA to RNA by replacing T's with U's"""
    DNA = f.LoadFile('\\rosalind_rna.txt')
    RNA = ''.join(['U' if x=='T' else x for x in DNA])
    f.ExportToFile('rosalind_rna_output.txt', RNA)
    return
    
DNAtoRNA()