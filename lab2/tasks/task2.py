#Napisz funkcję lotto, która do zwracanej listy wpisze 6 losowych i nie powtarzających się liczb z zakresu od 1 do 49.
import random
list=[]
def lotto():
    while(len(list)<6):

        x=random.randint(1,49)
        
        if x not in list:
            list.append(x)
    print(list)


print(lotto())
    