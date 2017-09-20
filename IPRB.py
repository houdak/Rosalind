"""
Mendel's First Law
Solved July 26, 2017
"""

import FileOperations as f
from FrequentOperations import nCr

def MendelFirstLaw():
    """Calculates the probability that 2 randomly selected mating
    organisms will produce indiv possessing a dominant allele"""
    input = f.LoadFile('\\rosalind_iprb.txt').split()
    k = int(input[0]) # num of homo dominant indivs
    m = int(input[1]) # num of heterozygous indivs
    n = int(input[2]) # num of homo recessive indivs
    
    total_outcomes = nCr(k+m+n,2)
    o100 = nCr(k,2) + (k*m) + (k*n) # total outcomes with 100 pcent probability of dom offspring (k with itself and others)
    o75  = nCr(m,2) # outcomes w 75 pcent probability (m with itself)
    o50  = m*n # m with n = 50 pcent prob
    #o0   = nCr(n,2) n with itself won't product dom offspring, don't need to calculate
    probability = (o100 + 0.75*o75 + 0.5*o50) / total_outcomes
    f.ExportToFile('rosalind_iprb_output.txt',str(probability))
    return 

MendelFirstLaw()