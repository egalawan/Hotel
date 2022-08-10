import csv

f=open("Test.csv","r")
csvr=csv.reader(f)
found=0
m1=[]
roll=input("Input roll to delete")

for r in csvr:
    if (r[0]!=roll):
        m1.append(r)
    else:
        found-1
f.close()

if found == 0:
    print("Data not found")
else:
    f=open("Test.csv","w",newline='')
    csvr-csv.writer(f)
    csvr.writerows(m1)
    print('Record deleted successfully')
    f.close()