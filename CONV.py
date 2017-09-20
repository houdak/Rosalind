"""
Comparing Spectra with the Spectral Convolution
Solved August 22, 2017
"""

import FileOperations as f

# Comparing Spectra with the Spectral Convolution
def CompareSpectra():
    """ Given 2 spectra, returns:
    1. the largest mutliplicity of set1(-)set2
    2. abs(x) which maximizes (set1(-)set2)(x) """
    input = f.LoadFile('\\rosalind_conv.txt').splitlines()
    temp_spec = [float(x) for x in input[0].split()]
    test_spec = [float(x) for x in input[1].split()]
    
    # Find all possible differences between spectra
    differences = []
    for i in temp_spec:
        for j in test_spec:
            differences.append(round(i-j,5))
    
    # Find diff that occurs most frequently
    mode = max(set(differences),key=differences.count)
    
    # Count how frequently
    count = 0
    for i in differences:
        if i == mode:
            count += 1
    
    #print(count, mode, sep = '\n')
    f.ExportToFile('rosalind_conv_output.txt','\n'.join([str(count),str(mode)]))
    return

CompareSpectra()