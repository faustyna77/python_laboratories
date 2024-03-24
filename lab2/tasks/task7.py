'''Napisz funkcję wyznaczającą rozwiązania równania kwadratowego. Funkcja przyjmuje 
3 parametry a, b, c i rozwiązania zapisuje do pliku result.txt'''
import math 

def solution(a,b,c):
    delta=b*b-4*a*c
    if(delta>0):
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        return (str(x1),str(x2))
    elif(delta<0):
        answer=("brak miejsc zerowych")
        return ((answer))

    else:
        x=-b/(2*a)
        return str(x)
    
def zapis(wynik):
    with open("solut.txt", "a") as file:
        file.write(wynik)
   
      


    
wynik=solution(1,2,3)
zapis(str(wynik))

