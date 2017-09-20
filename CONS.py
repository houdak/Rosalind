"""
Consensus and Profile
Solved July 27, 2017
"""

import FileOperations as f

def ConsensusandProfile():
    """ Returns conensus string and profile matrix for a collection of
    FASTA format DNA strings"""
    input = f.LoadFile('\\rosalind_cons.txt')
    [Labels, DNA] = f.FASTA(input)
    
    k = len(DNA[0])

    # Initialize profile
    profile = {'A': [], 'C': [], 'G': [], 'T': []}
    for _ in range(k):
        profile['A'].append(0)
        profile['C'].append(0)
        profile['G'].append(0) 
        profile['T'].append(0)
    # Fill in profile
    for line in DNA:
        i = -1
        for nuc in line:
            i += 1
            profile[nuc][i] += 1
    # Find consensus
    consensus = ''
    for i in range(k):
        nuc_l = [profile['A'][i],
                 profile['C'][i],
                 profile['G'][i],
                 profile['T'][i]]
        for key in profile:
            if max(nuc_l) == profile[key][i]:
                consensus += key
                break
    # Report results in proper format
    output = [consensus,
              'A: %s' %(' '.join(map(str,profile['A']))),
              'C: %s' %(' '.join(map(str,profile['C']))),
              'G: %s' %(' '.join(map(str,profile['G']))),
              'T: %s' %(' '.join(map(str,profile['T'])))]
              
    
    f.ExportToFile('rosalind_cons_output.txt','\n'.join(output))
    return

ConsensusandProfile()