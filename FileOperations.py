import sys
import os

os.getcwd()

def LoadFile(filename):
    """Loads file from 'Datasets' folder"""
    wd = os.getcwd()
    pathway = wd +'\\Datasets\\' + filename
    with open(pathway) as file:
        data = file.read()
    return data


def ExportToFile(filename,data):
    """Exports results to 'Output' folder"""
    wd = os.getcwd()
    pathway = wd +'\\Output\\' + filename
    with open(pathway,'w') as file:
        file.write(data)
    return
  
      
def FASTA(input):
    """ Converts FASTA input to individual DNA string, or
    list of strings depending on content.
    Stores DNA and labels in separate lists"""
    input = input.splitlines()
    DNA = ['' for _ in range(len(input))] #longer than necessary
    Labels = [] #also stores labels
    index = -1
    # Add line by line
    for line in input:
        if '>' in line:
            index += 1
            Labels.append(line[1:])
        else:
            DNA[index] += line
    # Remove extra portions of DNA
    if index == 0:
        return Labels[0],DNA[0] #returns two strings
    else:
        return Labels,DNA[:index+1]