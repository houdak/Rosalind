"""
Mortal Fibonacchi Rabbits
Solved July 28, 2017
"""

import FileOperations as f

def MortalRabbits():
    """ Calculates total number of pairs of rabbits remaining after n-th month
    if all rabbits live for m months, and product 1 pair each month after
    maturity (1 month after birth"""
    input = f.LoadFile('\\rosalind_fibd.txt').split()
    n = int(input[0])
    m = int(input[1])
    
    pairs = [1,1]
    for _ in range(m):
        pairs.insert(0,0)
    for _ in range(n-1):
        pairs.append(sum(pairs[-m:-1])) # formula for calculation
    f.ExportToFile('rosalind_fibd_output.txt',str(pairs[-1]))
    return

MortalRabbits()