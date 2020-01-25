import os
import numpy as np






if __name__ == '__main__':
    Load_path = "../int_train/"
    name_list = os.listdir(Load_path)
    name_list.sort()
    cnt = 0
    data = []
    train = []
    val = []
    #name_list = name_list[-2:]
    for name in name_list:
        read = np.genfromtxt(Load_path+name, delimiter=',')
        np.random.shuffle(read)

        #label = np.zeros(len(read)) + cnt
        #read = np.c_[read, label]
        label = np.zeros(len(read)) + cnt
        read = np.c_[read, label]

        #read_train = read[:int(len(read)*0.8)]
        #read_val = read[int(len(read)*0.8):]

        data.append(read)
        #train.append(read_train)
        #val.append(read_val)
        cnt += 1
        #if cnt == 12:
        #    break
        print(name + " finished !")

    data = np.concatenate(data, axis=0)
    #train = np.concatenate(train, axis=0)
    #val = np.concatenate(val, axis=0)
    
    np.savetxt("../dataset/train.csv", data, delimiter=",", fmt='%d')
    #np.savetxt("../dataset/species_train.csv", train, delimiter=',', fmt='%d')
    #np.savetxt("../dataset/species_validation.csv", val, delimiter=',', fmt='%d')


