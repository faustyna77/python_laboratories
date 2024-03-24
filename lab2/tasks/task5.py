'''Napisz funkcję, która sumuje liczby z listy podanej jako parametr i podaj ją 
(tą funkcję) jako parametr do innej funkcji,
 która odczyta liczby znajdujące się w pliku każda w nowej linii.'''
'''
list=[1,2,3]


def funck1(list):
    i=0
    sum=0
    for i in list:
        sum+=int(i)
        sum+=i
    return sum
    '''
'''
list2=[1,1,5]
print(funck1(list2))
def readFile(funck1):
    file=open("liczby.txt","w")
    file.write(str(funck1(list2)))
    file.close()
    file=open("liczby.txt","r")
    for line in file:
        file.readline()
    file.close()
readFile(funck1)

'''
'''
def odczyt(funckcja):
    with open("liczby.txt","r") as file:
        for line in file:
            numbers=line.split()
            result=funck1(numbers)
            return result

    

print(odczyt(funck1))
'''
def sumuj(list):
    sum = 0
    for num in list:
        sum += int(num)
    return sum

def odczyt(funck1):
    with open("liczby.txt", "r") as file:
        for line in file:
            numbers = line.split()
            result = funck1(numbers)
            print("Suma liczb z pliku:", result)

odczyt(sumuj)
