import numpy as np
import os

def filter_reads(pos, file_name):
    with open(pos+file_name) as f_in:
        with open("filtered_train/"+file_name.split(".")[0]+"_new.fasta", 'w') as f_out:
            for read in f_in.readlines():
                one_hot = []
                flag = 0
                for nucl in read[:-1]:
                    if nucl == 'A':
                        continue
                    elif nucl == 'C':
                        continue
                    elif nucl == 'G':
                        continue
                    elif nucl == 'T':
                        continue
                    else:
                        flag = 1
                        break
                if flag == 0:
                    f_out.write(read)


if __name__ == "__main__":
    load_path = "stride50_train/"
    
    name_list = os.listdir(load_path)
    for name in name_list:
        filter_reads(load_path, name)
       
