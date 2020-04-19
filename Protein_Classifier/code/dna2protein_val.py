import os
table = {

        'ATA':'I',   'ATC':'I',   'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'O', 'TAG':'O',
        'TGC':'C', 'TGT':'C', 'TGA':'O', 'TGG':'W'
    }

def func1(dna):
    protein=[]
    codon=[]
    var1=0
    var2=3
    for i in range(len(dna)//3):
            codon.append("".join(dna[var1:var2]))
            var1+=3
            var2+=3
    for i in range(len(codon)):
        if len(codon[i])==3:
            protein.append(table[codon[i]])
    return "".join(protein)

def dna2protein(file_name):
    with open("filtered_val/"+file_name) as file_in:
        with open("protein_val/"+file_name, 'w') as file_out:
            reads = file_in.readlines()
            for read in reads:
                dna=read[:-1]
                dna1=dna[1:]
                dna2=dna[2:]
                rdna=dna[::-1]
                dna3=rdna[1:]
                dna4=rdna[2:]


                ldna1=func1(dna)[:-1]
                ldna2=func1(dna1)[:-1]
                ldna3=func1(dna2)
                ldna4=func1(rdna)[:-1]
                ldna5=func1(dna3)[:-1]
                ldna6=func1(dna4)

                protein = ldna1+ldna2+ldna3+ldna4+ldna5+ldna6
                file_out.write(protein+"\n")
        
if __name__ == "__main__":
    path = "filtered_val/"
    name_list = os.listdir(path)
    for name in name_list:
        dna2protein(name)
        print(name + " finished") 
