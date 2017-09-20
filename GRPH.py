"""
Overlap Graphs
Solved July 28, 2017
"""

import FileOperations as f

def OverlapGraph():
    """ Returns adjacency list of labels of DNA in FASTA format"""
    input = f.LoadFile('\\rosalind_grph.txt')
    [Labels,DNA] = f.FASTA(input)
    
    temp_dict = {}
    adj_dict = {}
    for kmer in DNA:
        temp_dict[kmer] = []
    for kmer in temp_dict:
        for i in DNA:
            if (    kmer[-3:] == i[:3]  # if overlap by 3
                and kmer != i         ): # don't include self!
                temp_dict[kmer].append(i)
        # Remove any without matches
        if temp_dict[kmer] != []:
            adj_dict[kmer] = temp_dict[kmer]

    # Replace with labels
    name_dict = {}
    for kmer in adj_dict:
        kmer_ind = DNA.index(kmer)
        val_inds = []
        for value in adj_dict[kmer]:
            val_inds.append(DNA.index(value))
        name_dict[Labels[kmer_ind]] = [Labels[i] for i in val_inds]
    
    # Return in format
    output = []
    for name in name_dict:
        for i in name_dict[name]:
            output.append(' '.join([name,i]))
    f.ExportToFile('rosalind_grph_output.txt','\n'.join(output))
    return

OverlapGraph()