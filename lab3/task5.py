def fill_array():
    # Tworzenie pustej tablicy 5x5
    array = np.zeros((5, 5), dtype=int)
    
    # Wypełnianie pierwszego wiersza wartościami 2, 3, 4, 5, 6
    array[0] = np.arange(2, 7)
    
    # Wypełnianie pozostałych wierszy kwadratami liczb z poprzedniego wiersza
    for i in range(1, 5):
        array[i] = array[i-1] ** 2
    
    return array

# Wywołanie funkcji i wyświetlenie wyniku
result_array = fill_array()
print("Tablica dwuwymiarowa wypełniona kwadratami liczb z poprzedniego wiersza:")
print(result_array)