#!/usr/bin/env python
personas = ['Juan', 'Ana', 'Maria']
nombre = input('Ingrese nombre: ')
if nombre in personas:
    personas.remove(nombre)
    print(personas)
else:
    print('No existe ' + nombre)
