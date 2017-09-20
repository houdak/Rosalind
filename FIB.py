"""
Rabbits and Recurrance Relations
Solved July 26, 2017
"""

import FileOperations as f

def Rabbits():
    """ Returns total number of rabbit pairs present after n months
    beginning with 1 pair in each generation, every pair of reproduction-age
    rabbits producing a litter of k rabbit pairs"""
    s = f.LoadFile('\\rosalind_fib.txt').split()
    n = int(s[0])
    k = int(s[1])
        
    pairs = [0,1] # start with 1 pair, 0 as buffer for recurrance
    for _ in range(n-1): # for n total months
        pairs.append(pairs[-1] + (pairs[-2]*k)) # add previous bunnies to new litters
    f.ExportToFile('rosalind_fib_output.txt', str(pairs[-1])) #last value =final amount
    return
    
Rabbits()