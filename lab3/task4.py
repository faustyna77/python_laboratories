def histogram(file):
    try:
        with open(file,'r') as file:
            text=file.read()
            histogram_dick={}
            for char in text:
                if char in histogram_dick:
                    histogram_dick[char]+=1
                else:
                    histogram_dick[char]=1
            return histogram_dick
    except FileNotFoundError:
        return"plik nie został znaleziony"  
    

print(histogram('dane.txt'))
        