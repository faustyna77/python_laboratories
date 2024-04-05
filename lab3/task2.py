'''napisz skrypt wypełniający tablice znakami a nastepnie wyswietl znaki w kolejnosci odwrotnej do wprowadzania dane w
wprowadzic z klawiatury'''


tab=[]
number=int(input("podaj ilość elementów w tablicy jaką chcesz wprowadzić"))

for i in range(0,number):
    x=input("podaj znak")
    tab.append(x)

print("tablica po wprowadzeniu ",tab)
tab.reverse()
print("zawartość tablicy w odwrotnej kolejności",tab)