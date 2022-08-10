listofMacs = []

with open("C :\\ Users \\ Alvendril \\ Desktop \\ Python TXTS \\ Generated_Mac_addresses.txt", "r")as reader:
    for line in reader.readlines():
        listofMacs.append(line)

print(listofMacs)
print("\n"*2)

RemoveDash = []
RemoveLine = []
NewMacs = []

for mac in listofMacs :
    whatWeNeed = mac.replace("-",":")
    RemoveDash.append(whatWeNeed)

for mac in RemoveDash:
    whatWeNeed = mac.replace("\n","")
    RemoveLine.append(whatWeNeed)

for mac in RemoveLine:
    whatWeNeed = mac.lower()
    NewMacs.append(whatWeNeed)

print(NewMacs)

with open("C:\\ Users \\ Alvendril \\ Desktop \\ Python TXTS \\ Standarized_Mac_Addresses.txt", "w")as f:
    for i in NewMacs:
        f.write(i)
        f.write("\n")