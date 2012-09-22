#!/usr/bin/env python
MOs = [
        ['UY', 'MOVISTAR', '094777888', 'mensaje xxx'],
        ['UY', 'CLARO', '094777888', 'mensaje yyy'],
        ['AR', 'MOVISTAR', '094312888', 'mensaje zzz'],
        ['UY', 'MOVISTAR', '094432888', 'mensaje aaa'],
        ['UY', 'MOVISTAR', '094312888', 'mensaje yyy'],
        ['UY', 'MOVISTAR', '094312888', 'mensaje bbb']
        ]
mensajes = []
eliminar = []
for key,value in enumerate(MOs):
    if value[0]=='UY' and value[1]=='MOVISTAR':
        mensajes.append(value[2] + ' : ' + value[3])
    else:
        eliminar.append(key)

MOs2 = []
for key,value in enumerate(MOs):
    if key not in eliminar:
        MOs2.append(value)
MOs = MOs2
del(MOs2)
print(MOs)
