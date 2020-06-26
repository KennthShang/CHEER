import numpy as np
import os 

p_list = ["I", "M", "T", "N", "K", "S", "R", "L", "P", "H", "Q", "V", "A", "D", "E", "G", "S", "F", "Y", "W", "C", "O"]


int_to_vocab = {ii: word for ii, word in enumerate(p_list)}
vocab_to_int = {word: ii for ii, word in int_to_vocab.items()}


def encode(file_name):
    file = open("protein_train/"+file_name) 
    data = file.readlines() 
    feature = []
    for read in data:
        read = read[:-1]
        int_read = []
        for i in range(len(read)):
            int_read.append(vocab_to_int[read[i]])
        
        
        if len(int_read) < 492:
            print("less than 250bp: Padding")

        while len(int_read) < 492:
            padding = np.zeros((6,1)) + 22
            int_read = int_read.reshape(6, -1)
            int_read = np.concatenate((int_read, padding), axis = 1)
            int_read = int_read.reshape(1, -1)
        
        if len(int_read) != 492:
            print("error length")
        
        feature.append(int_read)
    name = file_name.split(".")[0]
    np.savetxt("int_train/"+name+".csv", feature, delimiter=",", fmt='%d')


if __name__ == "__main__":
    Load_path = "protein_train/"
    name_list = os.listdir(Load_path)
    for name in name_list:
        encode(name)
        #print(name + " finished")
