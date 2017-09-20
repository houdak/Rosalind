"""
Finding a Protein Motif
Solved July 31, 2017
"""

import FileOperations as f
import urllib.request

def NglyMotif():
    """Finds locations of N-glycosylation motiif in proteins,
    given uniprot IDs.
    Motif = N + (anything but P) + (S or T) + anything but P"""
    input = f.LoadFile('\\rosalind_mprt.txt').splitlines()
    output = []
    for id in input:
        url = 'http://www.uniprot.org/uniprot/' + str(id) + '.fasta'
        fasta = urllib.request.urlopen(url).read().decode("utf-8")
        [labels,protein] = f.FASTA(fasta)
    
        # Get locations of motif
        locs = []
        for i in range(len(protein)-4): #4 = len(motif)
            m = protein[i:i+4]
            if (    m[0] == 'N'
                and m[2] in 'ST'
                and 'P' not in m):
                locs.append(str(i+1))
        
        if locs != []:
            output.append(id)
            output.append(' '.join(str(x) for x in locs))
    
    f.ExportToFile('rosalind_mprt_output.txt','\n'.join(output))
    return

NglyMotif()