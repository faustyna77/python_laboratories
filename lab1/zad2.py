#3️⃣ Napisz krótki skrypt (wystarczy jedna linia kodu) który obliczy sumę liczb całkowitych wprowadzonych przez użytkownika i wynik wyświetli jako liczba zmiennoprzecinkowa.

x=int(input("podaj ile liczb chcesz wprowdzić "))
i=0
sum=0
while(i<x):
    i+=1
    n=int(input("podaj liczbe "))
    sum+=n


print("suma liczb podanych przez Ciebie wynosi ",sum)
