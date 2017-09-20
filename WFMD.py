"""
The Wright-Fisher Model of Genetic Drift
Solved August 25, 2017
"""

import FileOperations as f
from FrequentOperations import nCr

def Drift():
    """ Predicts probability that in a population of N diploid
    individuals initially possessing m copies of a dominant allele,
    we will observe after g generations at least k copies
    of a recessive allele (assuming Wright-Fisher model) """
    input = f.LoadFile('\\rosalind_wfmd.txt').split()
    N = int(input[0]) * 2
    m = int(input[1]) # initial num of copies of dom allele in pop (i)
    g = int(input[2]) # after g generations...
    k = int(input[3]) # prob that at least k copies of recessive (j)
    
    # Calculate probability of number of dominant alleles
    # Start with generation 0
    curr_gen = [0 for i in range(N+1)] # initialize as 0
    #-we know there is a 100% prob that there are m alleles
    #-everything else is 0
    curr_gen[m] = 1
    
    # iterate over generations
    for gen in range(g):
        next_gen = [0 for i in range(N+1)] #initialize as 0
        
        for i in range(N+1): #starting point
            for j in range(N+1): #ending point
                # temp-term = markov transition probability
                temp_term = nCr(N,i) * (j/N)**i * (1-(j/N))**(N-i)
                # add to previous p (pA + pB = Ptotal)
                next_gen[i] += temp_term * curr_gen[j]
        
        curr_gen = next_gen # update as current generation
    
    prob = str(sum(curr_gen[:-k])) #sum = 'at least k'
    f.ExportToFile('rosalind_wfmd_output.txt',prob)
    return

Drift()