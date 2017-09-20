"""
Introduction to Set Operations
Solved August 22, 2017
"""
import FileOperations as f
from FrequentOperations import RemoveDuplicates

def Sets():
    """ Returns 6 sets:
    1. A U B
    2. A intersection B
    3. A - B
    4. B - A
    5. Ac
    6. Bc """
    input = f.LoadFile('\\rosalind_seto.txt').splitlines()
    n = int(input[0])
    A = input[1].replace('{','').replace('}','').split(', ')
    B = input[2].replace('{','').replace('}','').split(', ')
    
    # Make Union set
    AB_union = RemoveDuplicates(A + B) # either A or B (or both)
    AB_intersect = [i for i in A if i in B] #both A & B
    AB_diff = [i for i in A if i not in B] # A not B
    BA_diff = [i for i in B if i not in A] # B not A
    
    U = [str(i) for i in range(1,n+1)] # for set complements
    A_comp = [i for i in U if i not in A] # U not A
    B_comp = [i for i in U if i not in B] # U not B
    
    # Return in format
    Sets = [AB_union, AB_intersect, AB_diff, BA_diff, A_comp, B_comp]
    output = []
    for set in Sets:
        output.append('{%s}\n' %', '.join(set))
    f.ExportToFile('rosalind_seto_output.txt',''.join(output))
    return

Sets()