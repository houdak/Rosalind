"""
Assessing Assembly Quality with N50 and N75
Solved August 28, 2017
"""

import FileOperations as f

def Contigs():
    """ Returns N50 and N75 for a collection of DNA strings """
    DNA = f.LoadFile('\\rosalind_asmq.txt').splitlines()
    
    DNA = sorted(DNA, key=len)
    total_length = sum(len(x) for x in DNA)
    
    count = 0
    for i in DNA:
        count += len(i)
        if count > total_length / 2:
            N50 = len(i)
            break
    
    count = 0
    for i in DNA:
        count += len(i)
        if count > total_length*0.25:
            N75 = len(i)
            break
    
    output = [str(N50),str(N75)]
    f.ExportToFile('rosalind_asmq_output.txt',' '.join(output))
    return

Contigs()