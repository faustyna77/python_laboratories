






def add(x,y):
    return x+y



def odejmowanie(x,y):
    return(x-y)


def mnozenie(x,y):
    return x*y


def dzielenie(x,y):
    return float(x/y)


x=int(input("wybierz co chcesz zrobić 1-dodawanie 2-odejmowanie 3-mnozenie 4-dzielenie "))
if(x==1):
    x1=int(input("podaj 1 liczbe"))
    x2=int(input("podaj druga liczbe"))
    print(add(x1,x2))
elif(x==2):
    x1=int(input("podaj 1 liczbe"))
    x2=int(input("podaj druga liczbe"))
    print(odejmowanie(x1,x2))
elif(x==3):
    x1=int(input("podaj 1 liczbe"))
    x2=int(input("podaj druga liczbe"))
    print(mnozenie(x1,x2))
elif(x==4):
    x1=float(input("podaj 1 liczbe"))
    x2=float(input("podaj druga liczbe"))
    print((dzielenie(x1,x2)))



'''

print(str(add(2,3))+"\n")
print(odejmowanie(9,8))
print(mnozenie(7,7))
print(dzielenie(7,3))
'''