import random

tablica_liczb=[]

for i in range(0,5):
    x=random.randint(-5,5)
    tablica_liczb.append(x)


f=open('data.txt','w')
f.write(str(tablica_liczb))
f.close()

f=open('data.txt','r')
for line in f:
    print(line)
f.close()