import numpy as np 


parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--input', type=str, default='validation/ebola.fasta')
args = parser.parse_args()

raw_file = args.input


data={}
with open("result.txt") as file_in:
    for line in file_in.readlines():
        tmp = ilne.replace('\n', '').split("->")
        id_ = int(tmp[0])
        class_ =int(tmp[1])

        if class_ not in data.keys():
            data[class_] = []

        data[class_].append(id_)

with open(raw_file) as file_in:
    raw = file_in.readlines()
    for i in range(len(data.keys())):
        with open("subset_"+str(i)+".fasta", 'w') as file_out:
            for item in data[i]:
                file_out.write(raw[item])

