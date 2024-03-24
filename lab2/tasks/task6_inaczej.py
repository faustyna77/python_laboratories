from math import pi

def dodawanie(x1, y1):
    x1 = int(input("Podaj pierwszą liczbę: "))
    y1 = int(input("Podaj drugą liczbę: "))
    return x1 + y1

def odejmowanie(x1, y1):
    x1 = int(input("Podaj pierwszą liczbę: "))
    y1 = int(input("Podaj drugą liczbę: "))
    return x1 - y1

def mnozenie(x1, y1):
    x1 = int(input("Podaj pierwszą liczbę: "))
    y1 = int(input("Podaj drugą liczbę: "))
    return x1 * y1

def dzielenie(x1, y1):
    x1 = int(input("Podaj pierwszą liczbę: "))
    y1 = int(input("Podaj drugą liczbę: "))
    return float(x1 / y1)

def obwod(r):
    r = int(input("Podaj promień: "))
    return 2 * pi * r

print("Wybierz jakie działanie chcesz wykonać:")
print("1 - Dodawanie")
print("2 - Odejmowanie")
print("3 - Mnożenie")
print("4 - Dzielenie")
print("5 - Liczenie obwodu koła")
print("6 - Zapis do pliku")

x = int(input("Twój wybór: "))

if x == 1:
    result = dodawanie(1, 1)
elif x == 2:
    result = odejmowanie(1, 1)
elif x == 3:
    result = mnozenie(1, 1)
elif x == 4:
    result = dzielenie(1, 1)
elif x == 5:
    result = obwod(1)

if x in range(1, 6):
    with open("wyniki.txt", "a") as file:
        file.write(str(result) + "\n")

elif x == 6:
    with open("wyniki.txt", "r") as file:
        for line in file:
            print(line.strip())  # Usunięcie białych znaków z końca linii
