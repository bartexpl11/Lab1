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

lista = [5, 6.6, 24, 'a', 'b', [2, 3, 4], 'ab']
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

# slownik = {'klucz': 'wartosc', 1: 2, 'a':5, 4: 'b'}
# print(slownik)
# print(slownik[4])
# slownik[6] = 45
# print(slownik)
# slownik.pop(1)
# print(slownik)
# print(slownik.keys())
# print(slownik.values())
# del slownik[6]

# a = 5
# b = 5
# if a > b:
#     print('a greater than b')
# elif a < b:
#     print('a less than b')
# else: # lub elif a == b
#     print('a is equal to b')

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if (a > b) & (c > d):
#     print(a, c)
# else:
#     print(b, d)

# for i in range (1, 8, 2):
#     print(i)
# else:
#     print('jesli petla dojdzie do konca petli')
#
# for i in lista:
#     print(i)

# for i in range(0, 5):
#     for j in range(0, 5):
#         result = i + j
#         print(result)
#     print(' ')

# licznik = 0
# while licznik < len(lista):
#     print(lista[licznik])
#     licznik += 1
# else:
#     print('gdy dojdzie do konca petli')

# licznik = 0
# while licznik != 10:
#     if licznik == 7:
#         print(licznik)
#         break
#     else:
#         licznik += 1
# else:
#     print('licznik')

list = [11,22,33,44,55,66,77]
sys.stdout.write('wprowadz liczbe: ')
a = sys.stdin.readline()
a = int(a)
i=0
while i<len(list):
    if a-list[i]==0:
        print(i, list[i])
        break
    else:
        i+=1