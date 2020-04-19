import sys
import os

def create_reads(file_name):
    file = open("validation/"+file_name)
    genomes = []
    seq = ""
    data = file.readlines()
    file.close()

    for line in data[1:]:
        if line[0] == '>':
            genomes.append(seq)
            seq = ""
        else:
            seq += line[:-1]
    
    # add the last sequence
    genomes.append(seq)

    reads = []
    for genome in genomes:
        for i in range(0, len(genome),250):
            if i + 250 > len(genome):
                break

            reads.append(genome[i:i+250])


    with open("stride50_val/"+file_name, 'w') as file:
        cnt = 0
        for read in reads:
            file.write(">"+str(cnt)+"\n")
            file.write(read +'\n')
            cnt+=1
        file.close()

if __name__ == "__main__":
    path = "validation/"
    name_list = os.listdir(path)
    for name in name_list:
        create_reads(name)
        print(name + " finished")    

