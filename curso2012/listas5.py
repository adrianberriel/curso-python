#!/usr/bin/env python
productos = ['Sony Vaio VPsdasd','Sony Vaio VPX','Sony Vaio VPC',
        'Dell Inspiron i15R','Dell Inspiron i15R HDS2']
stock = [10,30,5,11,8]
reponer = [5,10,2,2,4]

reporte = []
num = input('Ingrese nivel de stock: ')
num = int(num)
for key,value in enumerate(stock):
    if value < num:
        aux = (productos[key], stock[key], reponer[key])
        reporte.append(aux)
for value in reporte:
    print(value)
