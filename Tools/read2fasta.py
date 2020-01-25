file = open("Picornavirales_val.fasta")
data = file.readlines()

file = open("Picornavirales.fasta", 'w')
print(len(data))
for i in range(len(data)):
    file.write(">"+str(i)+"\n")
    file.write(data[i])
