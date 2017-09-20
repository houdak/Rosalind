"""
Error Correction in Reads
Solved August 27, 2017
"""

import FileOperations as f
from FrequentOperations import ReverseComplement
from FrequentOperations import HammingDistance
from FrequentOperations import RemoveDuplicates

# Error Correction in Reads
def Freq(read, DNA):
    """Returns frequency of a read in a set of strings
    Counts ReverseComplement as read"""
    rev_read = ReverseComplement(read)
    count = 0
    for i in DNA:
        if i == read:
            count += 1
        elif i == rev_read:
            count += 1
    return count

def MinimumDistance(read,correct_DNA):
    """ Returns correct string the error read matches with best"""
    for i in correct_DNA:
        if HammingDistance(read,i) == 1:
            return i

def ErrorCorrection():
    """ Given list of DNA (FASTA) with correct reads occuring at least twice,
    returns incorrect reads and the corrected version."""
    input = f.LoadFile('\\rosalind_corr.txt')
    [Labels,DNA] = f.FASTA(input)    
    
    correct_DNA = []
    # Read is correct if it appears at least twice,
    #-possibly as reverse complement
    for i in DNA:
        if Freq(i,DNA) > 1:
            correct_DNA.append(i)
    
    # Add all reverse complements to correct_DNA
    new_correct = []
    for i in correct_DNA:
        new_correct.append(i)
        new_correct.append(ReverseComplement(i))
    correct_DNA = RemoveDuplicates(new_correct)
    
    # Compare each read against the correct ones
    output = []
    for read in DNA:
        # If its in correct_Dna, ignore
        if read not in correct_DNA:
            # Find which string it matches best
            match = MinimumDistance(read,correct_DNA)
            # print in format
            output.append('%s->%s' %(read,match))
    f.ExportToFile('rosalind_corr_output.txt','\n'.join(output))
    return

ErrorCorrection()