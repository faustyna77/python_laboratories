''' Stworzony na poprzednich zajęciach kalkulator edytuj tak aby wykorzystywał on funkcję do obliczania wybranych przez użytkownika działań 
(funkcje przyjmują po 2 parametry i zwracają wynik obliczeń)'''
from math import pi
def dodawanie(x1,y1):
    x1=int(input("podaj 1 liczbe "))
    y1=int(input("podaj 2 liczbe "))
    return x1+y1


def odejmowanie(x1,y1):
    x1=int(input("podaj 1 liczbe "))
    y1=int(input("podaj 2 liczbe "))
    return x1-y1

def mnozenie(x1,y1):
    x1=int(input("podaj 1 liczbe "))
    y1=int(input("podaj 2 liczbe "))
    return x1*y1
def dzielenie(x1,y1):
    x1=int(input("podaj 1 liczbe "))
    y1=int(input("podaj 2 liczbe "))
    return float(x1/y1)

def obwod(r):
    r=int(input("podaj promień "))
    return 2*pi*r


print("wybierz jakie działanie chcesz wykonać 1-dodawanie 2-odejmowanie 3 -mnozenie 4 -dzielenie 5 liczenie obwodu koła ")

x=int(input("Twój wybór : "))


if(x==1):
    print(dodawanie(1,1))
elif(x==2):
    print(odejmowanie(1,1))
elif(x==3):
    print(mnozenie(1,1))
elif(x==4):
    print(dzielenie(1,1))
elif(x==5):
    print(obwod(1))



