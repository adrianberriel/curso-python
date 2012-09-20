#!/usr/bin/env python
productos = ['Producto 1',['Stock:10', 'Precio Unitario:5'],
            'Producto 2',['Stock:10', 'Precio Unitario:5'],
            'Producto 3',['Stock:10', 'Precio Unitario:5']]

for value in productos:
    if isinstance(value, list):
        for value2 in value:
            print('\t' + value2)
    else:
        print(value + ':')
