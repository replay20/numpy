import numpy as np
def zad1():
    wielKrot=np.arange(3,46,3)
    print(wielKrot)

#zad1()

def zad2():
    listaFloat = np.array([2,3,4,5,6,9,8,7],dtype=float)
    print(listaFloat)
    listaInt = np.array(listaFloat,dtype='int64')
    print(listaInt)

#zad2()

def zad3(n):
    if n>0 and isinstance(n,int):
        return np.arange(1,n*n+1).reshape(n,n)
    else:
        return "Podano zla wartosc"


#print(zad3(5))

def zad4(liczba,ilosc):
    return np.logspace(0,ilosc-1, ilosc, base=liczba)

#print(zad4(2,4))