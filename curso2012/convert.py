#!/usr/bin/env python

def convert(num, base):
    """Convierte hexadecimales, octales y binarios a decimales"""
    base = base.upper()
    if base == 'HEX':
        formatook = True
        for x in num:
            if x > 'F':
                formatook = False
                print('Formato incorrecto')
        if formatook:
            hexa2dec(num)
    elif base == 'OCT':
        formatook = True
        for x in num:
            if x > '7':
                formatook = False
                print('Formato incorrecto')
        if formatook:
            oct2dec(num)
    elif base == 'BIN':
        formatook = True
        for x in num:
            if x > '1':
                formatook = False
                print('Formato incorrecto')
        if formatook:
            bin2dec(num)
    else:
        print('Base incorrecta')


def hexa2dec(num):
    largo = len(num)
    hexdict = {
            '0' : 0,
            '1' : 1,
            '2' : 2,
            '3' : 3,
            '4' : 4,
            '5' : 5,
            '6' : 6,
            '7' : 7,
            '8' : 8,
            '9' : 9,
            'A' : 10,
            'B' : 11,
            'C' : 12,
            'D' : 13,
            'E' : 14,
            'F' : 15}
    print(sum([hexdict.get(value)*(16**(largo-key-1)) for key,value in
        enumerate(num)]))


def oct2dec(num):
    largo = len(num)
    print(sum([int(value)*(8**(largo-key-1)) for key,value in
        enumerate(num)]))


def bin2dec(num):
    largo = len(num)
    print(sum([int(value)*(2**(largo-key-1)) for key,value in
        enumerate(num)]))
