'''Do kalkulatora dopisz funkcję, która umożliwi użytkownikowi zapis działań oraz 
wyniku dla obliczenia pola/obwodu okręgu do pliku tekstowego.'''



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


print("wybierz jakie działanie chcesz wykonać 1-dodawanie 2-odejmowanie 3 -mnozenie 4 -dzielenie 5 liczenie obwodu koła 6-zapis do pliku ")

x=int(input("Twój wybór : "))


if(x==1):
    result1=dodawanie(1,1)
    file=open("wyniki.txt","a")
    file.writelines(str(result1))
    file.close()
elif(x==2):
    result2=odejmowanie(1,1)
    file=open("wyniki.txt","a")
    file.writelines(str(result2))
    file.close()
elif(x==3):
    result3=(mnozenie(1,1))
    file=open("wyniki.txt","a")
    file.writelines(str(result3))
    file.close()
   
elif(x==4):
    result4=(dzielenie(1,1))
    file=open("wyniki.txt","a")
    file.writelines(str(result4))
    file.close()
    
elif(x==5):
    result5=(obwod(1))
    file=open("wyniki.txt","a")
    file.writelines(str(result5))
    file.close()

    
    
elif(x==6):
    file=open("wyniki.txt","r")
    for line in file:
        print(line)
    file.close()



    



