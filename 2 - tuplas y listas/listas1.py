#!/usr/bin/env python
personas = ('Juan', 'Ana', 'Maria')

lista_personas = []

num = input('Ingrese un numero: ')
num = int(num)
if num > len(personas):
    print('Numero invalido')
else:
    for value in range(num):
        lista_personas.append(personas[value])
print(lista_personas)
