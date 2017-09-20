"""
Inferring Protein from Spectrum
Solved August 19, 2017
"""

import FileOperations as f

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

# Gives amino acid for mass, instead of other way around
inv_massdict = {round(mass,4): protein for protein, mass in mass_dict.items()}

def Spectrum():
    """ Given prefix spectrum of protein, returns protein string"""
    L = f.LoadFile('\\rosalind_spec.txt').splitlines()
    L = list(reversed(sorted([float(x) for x in L])))

    protein = []
    for i in range(len(L)-1):
        aa = round(L[i]-L[i+1],4)
        protein.insert(0,inv_massdict[aa])
    
    f.ExportToFile('rosalind_spec_output.txt',''.join(protein))
    return

Spectrum()