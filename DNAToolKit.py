from Structures import *
from collections import Counter
import sys
from files import*
def readseq(filename):
    seq=''
    with open(filename,"r") as f :
        for line in f:
           if not line[0]== '>':
                seq += line.rstrip()
    return seq

def seqvalidation(dna_seq): 
    """Determine wether the sequance contains only A,C,G,U or Not"""
    tempseq= dna_seq
    for nucl in tempseq:
        if nucl not in Nuclotides:
            return False
    sequ.write(tempseq)
    sequ.close()
    return tempseq

def nuc_count(seq): 
    tempCountdict= {"A":0,"C":0,"G":0,"T":0}
    for nucl in seq:
        tempCountdict[nucl] += 1
    return tempCountdict

def transcription(seq):
  """Transcript the DNA into RNA by changing the "T" to "U"""
  rna= seq.replace("T","U")
  Rnaf.write(rna)
  Rnaf.close()
  return rna


def rev_complementry_string(seq):
    """returns back the reverse of the complementry DNA templete"""
    mapping =str.maketrans('ATCG','TAGC') #changes A to T , C TO G
    return seq.translate(mapping)[::-1] # reverse the output of the mapping

def gc_content(seq):
    """Returns the GC content"""
    return round((seq.count('C')+seq.count('G'))/len(seq)*100,2) #count the G and C then divide by 2 *100 to find the precentage 

def gc_content_sec(seq, k=20):
    """return the gc content for certain length in DNA sequence"""
    res=[]
    for i in range(0, len(seq)- k + 1,k):
        subseq=seq[i:i+k]
        res.append(gc_content(subseq))
    GC=open(("GC content for "+str(k)+" BP.txt"),"w") #creates a file to store the GC content for x BP
    GC.write(str(res))
    GC.close()
    return res

def translate_DNAseq(seq, init_pos=0):
    """takes each 3 codons of DNA and get the crossbonding amino acid"""
    return [DNA_Codons[seq[pos:pos+3]] for pos in range(init_pos, len(seq) - 2 , 3)]
    
def translate_RNAseq(seq, init_pos=0):
    """takes each 3 codons of RNA and get the crossbonding amino acid"""

    return [RNA_Codons[seq[pos:pos+3]] for pos in range(init_pos, len(seq) - 2 , 3)]
   
def codon_usage(seq, aminoacid):
    """counts how many times a codon is present"""  
    tempList =[]
    for i in range(0, len(seq) -2,3):
        if DNA_Codons[seq[i:i+3]]==aminoacid:
            tempList.append(seq[i:i+3])

    frqDict= dict(Counter(tempList))
    totalweight= sum(frqDict.values())
    for seq in frqDict:
        frqDict[seq]=round(frqDict[seq]/totalweight,2)
    return frqDict

def gen_reading_frame(seq):
    """creates possible amino acids ||reading frames|| """
    frames=[]
    frames.append(translate_DNAseq(seq,0))
    frames.append(translate_DNAseq(seq,1))
    frames.append(translate_DNAseq(seq,2))
    frames.append(translate_DNAseq(rev_complementry_string(seq),0))
    frames.append(translate_DNAseq(rev_complementry_string(seq),1))
    frames.append(translate_DNAseq(rev_complementry_string(seq),2))
    return frames

def proteins(cod_seq):
    """extracts the protein sequence from the DNA"""
    current_prot =[]
    proteins =[]
    for cod in cod_seq:
      if cod == "_": #stop codon
        if current_prot:
            for p in current_prot:
                proteins.append(p) #add all acids to the proteins list
            current_prot=[] #set current protein to null
      else:
         if cod == "M": #start codon
            current_prot.append("") #adds an item in the list for each start codon
         for i in range (len(current_prot)):
            current_prot[i] += cod #adds acids for the same protein
    return proteins

def reading_frames_proteins(seq,startPos=0,endPos=0,Ordered=False):
    """Gets the proteins for reading frames"""
    if endPos > startPos:
        rfs= gen_reading_frame(seq[startPos: endPos]) #gets reading frames after reversing the start and end pos
    else:
        rfs= gen_reading_frame(seq) #gets the reading frames
    res=[]
    for rf in rfs:
        prots= proteins(rf) #gets the protein sequence from the reading frame
        for p in prots:
            res.append(p) #add the sequence to res list
    if Ordered:
        return sorted(res, key=len, reverse=True)
    return res


