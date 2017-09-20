"""
Computing GC Content
Solved July 26, 2017
"""

import FileOperations as f

def GC():
    """Computes GC content of set of DNA strings.
    Returns name and content of string with highest GC-content"""
    input = f.LoadFile('\\rosalind_gc.txt')
    [Labels,DNA] = f.FASTA(input)
    
    # Calculate GC content
    gc_content = []
    for seq in DNA:
        count = 0
        for nuc in seq:
            if nuc in 'GC':
                count += 1
        gc_content.append(count/len(seq)*100)
    # Find & report max GC + label
    maxgc = max(gc_content)
    maxgc_index = gc_content.index(maxgc)
    label = Labels[maxgc_index]
    f.ExportToFile('rosalind_gc_output.txt','\n'.join([label,str(maxgc)]))
    return

GC()