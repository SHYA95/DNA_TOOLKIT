import random
import os
from tkinter.filedialog import test
from DNAToolKit import*
from files import*
import tkinter as tk
from tkinter import *

from tkinter import *

ws = Tk()
ws.geometry('700x500')
ws.title('DNA TOOLKIT')
ws['bg']='#967bb6'

f = ("Times bold", 20)

def nextPage():
    ws.destroy()
    import Page_3

def prevPage():
    ws.destroy()
    import Project   

    
Fnamelabel=Label(ws,text="Write the file name :",padx=20,pady=20,bg='#967bb6',font=f)
Fnamelabel.pack(expand=True, fill=BOTH)
FnameEntry =Entry(ws)
FnameEntry.pack(padx=22,pady=22)

def firststep():
   DNAseq= readseq(FnameEntry.get())
   Vseq=seqvalidation(DNAseq)

Button(ws, text="ENTER", font=f,command=firststep).pack(padx=24,pady=24)

Button(ws, text="Previous Page", font=f,command=prevPage).pack(fill=X, expand=TRUE, side=LEFT)

Button(ws,text="Next Page",font=f,command=nextPage).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()

DNAseq= readseq(FnameEntry.get())
Vseq=seqvalidation(DNAseq)
if Vseq is not False:
   print("Which tool would you like to use?\n")
   print("Show Basic info [1]")
   print("Show RNA sequence [2]")
   print("Show DNA Complementery sequence and it's reverse [3]")
   print("Show GC content [4]")
   print("Show amino acids[5]")
   print("Show codon frequency[6]")
   print("Show reading frames[7]")
   print("Show proteins[8]")

   c=int(input("Enter the number of the tool : "))

   if (c==1): #1
    print(f'\nDNA Sequence : {Vseq}\n')  
    print(f'\nSequence length : {len(Vseq)} bp\n')
    Binfo.write(f'Sequence length : {len(Vseq)} bp\n')
    print(f'\nNucleotide count : { nuc_count(Vseq)}\n')
    Binfo.write(f'\nNucleotide count : { nuc_count(Vseq)}\n')

   elif (c==2):#2
    print(f'\nDNA to RNA transcription : {transcription(Vseq)}\n')

   elif(c==3):#3
    print(f"\n DNA template + complementery string + reverse complementery string:\n5' {Vseq} 3'[DNA template]")
    bonds=''.join(['|' for c in range(len(Vseq))])
    print(f"   {bonds}")
    print(f"3' {rev_complementry_string(Vseq)[::-1]} 5' [complement]\n")
    csf.write(Vseq+'\n') #csf start
    csf.write(bonds+'\n')
    csf.write(rev_complementry_string(Vseq)[::-1])
    csf.close()# csf end
    print(f"\n3' {rev_complementry_string(Vseq)[::-1]} 5' [complement]")
    print(f"   {bonds}")
    print(f"5' {rev_complementry_string(Vseq)} 3'[Rev. complement]\n")
    Rcsf.write(rev_complementry_string(Vseq)[::-1]+'\n') #Rscf start
    Rcsf.write(bonds+'\n')
    Rcsf.write(rev_complementry_string(Vseq))
    Rcsf.close() #Rscf end 
          
   elif(c==4):#4
       x=int(input("Do u need whole GC content[1] or content per number of BPs[2]? : "))
       if(x==1):
           print(f'\nGC content : {gc_content(Vseq)}%\n')
           Binfo.write(f'\nGC content : {gc_content(Vseq)}%\n')
       elif(x==2):
        k=int(input(f'number of BPs desired for GC content : '))
        print(f'\nGC content for every {k} bps :{gc_content_sec(Vseq,k)}\n ')
   elif(c==5):#5
    print(f'\nAminoacids : {translate_DNAseq(Vseq)}\n')
   elif(c==6):#6
    print(f'\nCodon frequency: {codon_usage(Vseq,"L")}\n')   
   elif(c==7):#7
     print(f'\nReading_frames: \n')
     framesnum=0
   
     for frames in gen_reading_frame(Vseq):
          fRf.write(str(frames)+'\n\n')
          if framesnum==3:
             print("\nReverse frames : \n") 
          if framesnum==2:
             fRf.write("\n\n----Reverse frames-----\n\n")
          print(frames)      
          framesnum+=1
   elif(c==8):#8
    print(f'All proteins in frames :')

    for prot in reading_frames_proteins(Vseq,0,0,True):
      fP.write(str(prot)+'\n\n')
      print(f'{prot}')
else:
    print("Sequance not valid")

  
