"""
Matching a Spectrum to a Protein
Solved August 22, 2017
"""

import FileOperations as f
from FrequentOperations import CompareSpectra

# Monoisotopic mass table of 20 amino acids
mass_dict = {'A': 71.03711,
             'C': 103.00919,
             'D': 115.02694,
             'E': 129.04259,
             'F': 147.06841,
             'G': 57.02146,
             'H': 137.05891,
             'I': 113.08406,
             'K': 128.09496,
             'L': 113.08406,
             'M': 131.04049,
             'N': 114.04293,
             'P': 97.05276,
             'Q': 128.05858,
             'R': 156.10111,
             'S': 87.03203,
             'T': 101.04768,
             'V': 99.06841,
             'W': 186.07931,
             'Y': 163.06333}

# Matching a Spectrum to a Protein
def GetMasses(protein):
    """ Returns all possible substring
    masses of a protein string"""
    masses = []
    mass = 0
    for aa in protein:
        mass += mass_dict[aa]
        masses.append(mass)
    
    mass = 0
    for aa in list(reversed(protein))[:-1]:
        mass += mass_dict[aa]
        masses.append(mass)
    return masses

def MatchSpectrum():
    """ Given:
    1) A positive integer n
    2) n protein strings
    3) A multiset corresponding to the complete spectrum of some
    unknown protein string...
    ... Returns the maximum multiplicity, and the string where this occurs """
    input = f.LoadFile('\\rosalind_prsm.txt').splitlines()
    n = int(input[0])
    proteins = input[1:n+1]
    spectrum = [float(x) for x in input[n+2:]]
    
    # Find the masses for each protein
    masses = []
    for p in proteins:
        masses.append(GetMasses(p))
    
    # Find mode for each
    modes = []
    for m in masses:
        modes.append(CompareSpectra(m,spectrum))
    
    # Return protein w max modes, and that max
    max_mode = max(modes)
    max_index = modes.index(max_mode)
    max_protein = proteins[max_index]
    
    f.ExportToFile('rosalind_prsm_output.txt','\n'.join([str(max_index),max_protein]))
    return

MatchSpectrum()