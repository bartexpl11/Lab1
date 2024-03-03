import sys

# a = 56
# print(a)
# print(type(a))
# b = 5.5
# print(b)
# print(type(b))
# zmienna_tesktowa = 'wizualizacja danych'
# print(zmienna_tesktowa)
# print(type(zmienna_tesktowa))
# a = 6
# b = 3
#
# c = a + b
# print(c)
# d = a - b
# print(d)
# e = 4
# f = b // a
# print(f)
# f = a // b
# print(f)
# # g = a ** 2
# g = a ** 2 # dwa ** to potega
# print(g)
# h = pow(a, 2)
# print(h)
# i = 6 ** 1/2  # kolejnosc dzialan , trzeba dac 1/2 w nawias
# j = pow(6, 1/2)
# print(i)
# print(j)
#
# k = 'wizualizacja danych'
# l = ' grupa '
# m = 1
# print(k+l+str(m))
# print('liczba a jest rowna {:d}, liczba b jest rowna {:.2f}'.format(a, b))
# w klamerki wchodza zmienne z format, liczba zmiennych i klamer ma sie rownac

# a = input ('Wprowadz liczbe: ')
# print(a)
# print(type(a))
# #a = int(a)
# print(a*5)
# print(type(a))

# sys.stdout.write('wprowadz liczbe: ')
# b = sys.stdin.readline()
# print(b + ' to wartosc liczby b')
# print(type(b))

# lista = [5, 6.6, 24, 'a', 'b', [2, 3, 4], 'ab']
# print(lista)
# lista.append(67)
# print(lista)
# lista.insert(2, 'c')
# print(lista)
# lista.extend([20, 11, 22])
# print(lista)
# lista.pop()
# print(lista)
# lista.pop(2)
# print(lista)
# lista.remove([2, 3, 4])
# print(lista)
# del lista[1]
# print(lista)
# #del lista
# print(lista)
# lista.reverse()
# print(lista)
# #lista.sort()
# print(lista)

slownik = {'klucz': 'wartosc', 1: 2, 'a':5, 4: 'b'}
print(slownik)
print(slownik[4])
slownik[6] = 45
print(slownik)
slownik.pop(1)
print(slownik)
print(slownik.keys())
print(slownik.values())
del slownik[6]