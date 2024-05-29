
'''def first_function(funk_second,args):
    return funk_second(funk_second(args))



def another_function(x):
    return x**2


print(first_function(another_function,5))
'''

#funkcje anonimowe lambda


#nieanonimowa

'''def add(x,y):
    return x+y

print(add(1,2))'''
#z zastosowaniem lambda 
#print((lambda x:x+6)(1))
'''

d=((lambda x,y:2*x+y)(1,2))
print(d)


k=((lambda x,y,z:x*y*z)(1,1,3))
print(k)

'''

'''
list=[]

def append_funck(x):
    list.append(x)


append_funck(1)
append_funck(2)
print(list)

'''

'''

def add_ten(x):
    return x+10


listes=[1,2,3,4,5]


result=list(map(add_ten,listes))
print(result)

'''
'''
listes=[1,2,3,4,5]
result3=list(map((lambda x:x+10),(listes)))


print(result3)
'''


'''

listes=[1,2,3,4,5,6]


def czy_parzysta(x):
    if(x%2==0):
        return x
    
print(list(filter(czy_parzysta,listes)))

'''

#task 2 Napisz funkcję z wykorzystaniem wyrażenia lambda która dla przyjętego argumentu x wyznaczy listę kwadratów kolejnych liczb naturalnych od 1 do x
'''
lista=[]
def funkc1():
    x=int(input("podaj x argumentów"))
    for i in range(0,x+1):
        lista.append(i)
    print(lista)
    lista4=list(map((lambda x:x**2),lista))
    return lista4





print(funkc1())

'''
#task3 Z podanej poniżej listy odfiltruj elementy które są większe od 4 wykorzystując funkcję filter.

#[1, 2, 3, 5, 8, 3, 0, 7]

'''

list_next=[1,2,3,5,8,3,0,7]

lista_filtered=list(filter((lambda x:x>4),list_next))


print("lista po filtracji : ",lista_filtered)

'''
'''
'''
'''list_next=[1,2,3,5,8,3,0,7]

list2=[]

def funk5(lista):
    c=len(list_next)
    for i in range(0,c+1):
        if(i>4):
            list2.append(i)
funk5(list_next)      
print(list2)
    
#print(list(filter(funk5(list_next),list_next)))
'''


#task7
'''
def generate_spam():
    word = 'spam'
    for i in range(1, len(word) + 1):
        yield word[:i]

# Tworzenie listy z wygenerowanych elementów
spam_list = list(generate_spam())

# Wyświetlenie listy
print(spam_list)

'''
#task6
'''
def Newton(n,k):
    if k==0 or n==k:
        return 1
    else:
        return Newton(n-1, k-1) + Newton(n-1, k)
    


print(Newton(5,2))

'''


def decor(func):
    def wrap():
        print("==================")
        func()
        print("==================")
    return wrap

def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()

@decor
def print_text2():
    print("Spam")

print_text2()