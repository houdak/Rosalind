"""
Inferring Genotype from a Pedigree
Solved May 26, 2019
"""
import FileOperations as f
import re #used for regex expressions


# Standard probability calculations for genotypes (AA,Aa,aa), basically just from punnett squares
prob_dict ={
            '(AA,AA)': '1.0,0.0,0.0',
            '(AA,Aa)': '0.5,0.5,0.0',    
            '(AA,aa)': '0.0,1.0,0.0',
            '(Aa,AA)': '0.5,0.5,0.0',  
            '(Aa,Aa)': '0.25,0.5,0.25',
            '(Aa,aa)': '0.0,0.5,0.5',
            '(aa,AA)': '0.0,1.0,0.0',
            '(aa,Aa)': '0.0,0.5,0.5',
            '(aa,aa)': '0.0,0.0,1.0'
            }


# Conversion of genotype to a value
geno_dict = {
             'AA': '(1.0,0.0,0.0)',
             'Aa': '(0.0,1.0,0.0)',
             'aa': '(0.0,0.0,1.0)'
            }


def ReduceTree(tree):
    """ Function to convert symbolic genotypes to numerals"""
    # first solve all genotypes
    for key in prob_dict:
        tree = re.sub(key,prob_dict[key],tree)
    # next get any remaining genotypes
    for key in geno_dict:
        tree = re.sub(key,geno_dict[key],tree)
    return str(tree)


def SolveProbabilities(tree):
    """ Find pairings on the tree that are at the same level, and then
    solve them through multiplication. The calculations are based on constants from prob_dict"""
    #now use numerical tree to solve remaining branches
    # step one: find pairings that look like (#,#,#),(#,#,#)
    pairing_str = str(re.search('\(\d+\.\d+,\d+\.\d+,\d+\.\d+\),\(\d+\.\d+,\d+\.\d+,\d+\.\d+\)', tree).group(0))
    # step two: convert them to numbers
    pairing = pairing_str.replace('(','')
    pairing = pairing.replace(')','')
    pairing = pairing.split(',')
    pairing = [float(x) for x in pairing]
    # step three: calculate result by multiplying numbers
    AA =  pairing[0]*pairing[3] + 0.5*pairing[0]*pairing[4] + 0.5*pairing[1]*pairing[3] \
        + 0.25*pairing[1]*pairing[4]

    Aa =  0.5*pairing[0]*pairing[4] + pairing[0]*pairing[5] + 0.5*pairing[1]*pairing[3] \
        + 0.5*pairing[1]*pairing[4] + 0.5*pairing[1]*pairing[5] + 1*pairing[2]*pairing[3] \
        + 0.5*pairing[2]*pairing[4]

    aa =  0.25*pairing[1]*pairing[4] + 0.5*pairing[1]*pairing[5] + 0.5*pairing[2]*pairing[4] \
        + pairing[2]*pairing[5]
    
    result = [AA,Aa,aa]
    # step four: return result in string format
    result_formatted =  ''.join([str(result[0]),',',str(result[1]),',',str(result[2])])
    # step five: stick back into the string
    pairing_str = re.escape(pairing_str)
    result_formatted = re.escape(result_formatted)
    tree = re.sub(pairing_str,result_formatted,tree)
    return tree.replace('\\','')


def CountParantheses(tree):
    """ Count the number of parantheses to see if the tree is completely solved.
        Can't have more than one - otherwise means there are more pairings to solve."""
    n = 0
    for char in tree:
        if char == '(':
            n += 1
            if n > 1:
                return True
    return False
 
 
def GenotypeFromPedigree(newick):
    """ Combine all previous functions, and convert to exportable format"""
    input = f.LoadFile('\\rosalind_mend.txt')

    tree = ReduceTree(input)
    while CountParantheses(tree):
        tree = SolveProbabilities(tree)
    result = tree.replace('(','')
    result = result.replace(')','')
    result = result.replace(';','')
    result = result.split(',')
    f.ExportToFile('rosalind_mend_output.txt',' '.join(result))
    return
    

GenotypeFromPedigree()
