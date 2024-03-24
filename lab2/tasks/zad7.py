import math 

def solution(a, b, c):
    delta = b * b - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"Rozwiązania to: x1 = {x1}, x2 = {x2}"
    elif delta < 0:
        return "Brak miejsc zerowych"
    else:  # delta == 0
        x = -b / (2 * a)
        return f"Rozwiązanie to: x = {x}"

def zapis(wynik):
    with open("solut.txt", "a") as file:
        file.write(wynik + "\n")

# Wywołanie funkcji solution i zapis wyników do pliku
wynik = solution(1, 2, 3)
zapis(wynik)
