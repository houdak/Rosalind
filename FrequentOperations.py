"""Frequent Operations used in Rosalind Problems"""

from math import factorial

# Used in: IPRB, LIA, PPER, ASPC, EVAL, INDC, WFMD
def nCr(n,r):
    """n choose r"""
    return factorial(n) // factorial(r) // factorial(n-r)
    

# Used in ORF, CORR
def RemoveDuplicates(Items):
    ItemsNoDuplicates = []
    for num in Items:
        if num not in ItemsNoDuplicates:
            ItemsNoDuplicates.append(num)    
    return ItemsNoDuplicates
 
       
# Used in RNA, ORF, SPLC
def DNAtoRNA(DNA):
    """Converts string of DNA to RNA by replacing T's with U's"""
    RNA = ''.join(['U' if x=='T' else x for x in DNA])
    return RNA
 
       
# Used in REVC, ORF, REVP, CORR, DBRU
def ReverseComplement(s):
    """Returns the reverse complement of a string of DNA"""
    reverse = s[::-1]
    complement = ''
    for nuc in reverse:
        if nuc == 'A':
            complement += 'T'
        elif nuc == 'C':
            complement += 'G'
        elif nuc == 'G':
            complement += 'C'
        elif nuc == 'T':
            complement += 'A'
    return complement
          

# Used in PROT, ORF, SPLC
# Dictionary matching RNA codons with amino acid
RNA_dict = { 'UUU': 'F',
             'UUC': 'F',
             'UUA': 'L',
             'UUG': 'L',
             'UCU': 'S',
             'UCC': 'S',
             'UCA': 'S',
             'UCG': 'S',
             'UAU': 'Y',
             'UAC': 'Y',
             'UAA': '', #Stop
             'UAG': '', #Stop
             'UGU': 'C',
             'UGC': 'C',
             'UGA': '', #Stop
             'UGG': 'W',
             'CUU': 'L',
             'CUC': 'L',
             'CUA': 'L',
             'CUG': 'L',
             'CCU': 'P',
             'CCC': 'P',
             'CCA': 'P',
             'CCG': 'P',
             'CAU': 'H',
             'CAC': 'H',
             'CAA': 'Q',
             'CAG': 'Q',
             'CGU': 'R',
             'CGC': 'R',
             'CGA': 'R',
             'CGG': 'R',
             'AUU': 'I',
             'AUC': 'I',
             'AUA': 'I',
             'AUG': 'M',
             'ACU': 'T',
             'ACC': 'T',
             'ACA': 'T',
             'ACG': 'T',
             'AAU': 'N',
             'AAC': 'N',
             'AAA': 'K',
             'AAG': 'K',
             'AGU': 'S',
             'AGC': 'S',
             'AGA': 'R',
             'AGG': 'R',
             'GUU': 'V',
             'GUC': 'V',
             'GUA': 'V',
             'GUG': 'V',
             'GCU': 'A',
             'GCC': 'A',
             'GCA': 'A',
             'GCG': 'A',
             'GAU': 'D',
             'GAC': 'D',
             'GAA': 'E',
             'GAG': 'E',
             'GGU': 'G',
             'GGC': 'G',
             'GGA': 'G',
             'GGG': 'G'}

def RNAtoProtein(s):
    """ Uses RNA_dict to convert RNA string to protein"""
    codons = []
    protein = ''
    for i in range(0, len(s), 3):
        codons.append(s[i:i+3]) # separate into codons
    for triplet in codons:
        if triplet in ['UAA', 'UAG', 'UGA']: # stop at stop codons
            break
        else:
            protein += RNA_dict[triplet]
    return protein


# Used in HAMM, CORR, PDST
def HammingDistance(p,q):
    """Returns the Hamming Distance between 2 strings"""
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist += 1
    return dist  


#  Used in LEXF, KMER                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
def Lex(sym,r):
    """ Given a collection of symbols and a +integer n, returns
    all strings of length n that can be formed from the alphabet,
    ordered lexicographically"""    
    n = len(sym)
    lex_list = []
    
    # for first round
    for _ in range((n**r)//n): # should match 1/n of total in list
        for i in sym:
            lex_list.append(i)
    lex_list = sorted(lex_list)
    
    # First go through whole list correct number of times (j)
    m = (n**r)//n
    k = 0
    for j in range(1,r):      
        i = -1 # index resets each go-through
        m = m // n # Smaller number of each sym in a row each round
        k += 1 # More cycles each time to get through list
        
        for __ in range(n**k):
            for s in sym:
                for _ in range(m):
                    i += 1
                    lex_list[i] += s
    return lex_list

# Used in REAR, SORT
def CountBreakagePoints(p):
    """ Counts Breakage Points in a permutation,
    including those at the beginning and end of the sequence """
    p = [0] + p + [11]
    
    count = 0
    dir = None
    for i in range(1,len(p)):
        if dir == None:
            if p[i] == p[i-1] + 1:
                dir = 'ascend'
            elif p[i] == p[i-1] - 1:
                dir = 'descend'
            else:
                count += 1
        elif dir == 'ascend':
            if p[i] != p[i-1] + 1:
                dir = None
                count += 1
        elif dir == 'descend':
            if p[i] != p[i-1] - 1:
                dir = None
                count += 1
    return count

# Used in REAR, SORT
def TransformIndex(p,q):
    """Makes q easier to work with by changing index to match p
     as if p = [1,2,3,4,5,6,7,8,9,10]"""
    
    index = 10
    for i in p:                
        index += 1
        q = [index if x==i else x for x in q]
    q = [x-10 for x in q]
    return q

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

# Used in DBRU, GASM
def DeBruijn(Graph):
    """ Returns adjacency list """    
    # Add all prefixes to adj_dict
    adj_dict = {}
    for kmer in Graph:
        adj_dict[kmer[:-1]] = []
      
    for i in adj_dict:
        for j in Graph:
            if i == j[:-1]: # Look for strings with that prefix
                adj_dict[i].append(j[1:]) #If so, add suffix

    return adj_dict


# Used in CONV, PRSM
def CompareSpectra(temp_spec, test_spec):
    """ Given 2 spectra, returns:
    the largest mutliplicity of set1(-)set2 """
    
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
    
    return mode
    

# Used in LONG, GASM
def Overlap(p,q):
    """ Returns amount of overlap between 2 strings """
    # p = front str
    # q = back str
    if p == q:
        return 0
    else:    
        k = len(max([p,q], key = len))    
        for i in range(1,k):
            if p[i:] == q[:len(p[i:])]:
                return len(p[i:])
    return 0


# Used in LONG, GASM
def Combine(p,q):
    """ Combines two strings with overlap """
    k = len(max([p,q], key = len))    
    for i in range(1,k):
        if p[i:] == q[:len(p[i:])]:
            return (p + q[len(p[i:]):])
    return p + q 
    

# Used ing DBRU, GASM    
def DeBruijnRC(S):
    """ Returns adjacency list, based on
    given DNA strings and their reverse complements"""
    
    # Make list of S U Src
    SuRC = []    
    for i in S:
        SuRC.append(ReverseComplement(i))
    SuRC.extend(S)
    SuRC = RemoveDuplicates(SuRC)
    
    # Add all prefixes to adj_dict
    adj_dict = {}
    for kmer in SuRC:
        adj_dict[kmer[:-1]] = []
      
    for i in adj_dict:
        for j in SuRC:
            if i == j[:-1]: # Look for strings with that prefix
                adj_dict[i].append(j[1:]) #If so, add suffix
    
    # Return in format
    output = []
    for i in adj_dict:
        for j in adj_dict[i]:
            output.append(('(%s, %s)' %(i,j)))
           
    return adj_dict