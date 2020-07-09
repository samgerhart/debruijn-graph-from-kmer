# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:18:26 2019

@author: Samuel Gerhart
"""

#Note: I had to manually add in commas to final input
#I didn't have enough time manipulate the strings with code

f = open("De_Bruijn_Graph_from_kmer.txt", "r") #test
#f = open("rosalind_ba3e.txt", "r") #real deal
#dna = f.readline()

kmers = []
for line in f:
    k_mer = line[0:len(line) - 1]
    kmers.append(k_mer)
f.close()

fw  = open("outputlab.txt", "w")
#kmers = ['GAGG', 'CAGG', 'GGGG', 'GGGA', 'CAGG', 'AGGG', 'GGAG']
#kmers = ['ATG', 'GGG', 'GGT', 'GTA', 'GTG', 'TAT', 'TGG']
#dna = 'AAGATTCTCTAC'


#makes a debruijn graph using dict
def deBruijn(d, k):
    if d == '' or k == 0:
        return ''
    #kmers = dToKmers(d, k)
    deBruijnGraph = {}
    for kmer in kmers:
        #print(kmer)
        if kmer[0:k-1] in deBruijnGraph.keys():
            deBruijnGraph[kmer[0:k-1]].append(kmer[1:k])
            
        else:
            deBruijnGraph[kmer[0:k-1]] = [kmer[1:k]]
    return dictToString(deBruijnGraph)       

#writes dict to file
def dictToString(D):
    for x in sorted (D.keys()):
        y = D[x]
        y = sorted(y)     
        output = [x, '->'] + y + ['\n']  
        realoutput = ' '.join(output)
        fw.write(realoutput)

print(deBruijn(kmers, len(kmers[0])))

fw.close()