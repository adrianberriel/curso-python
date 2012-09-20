#!/usr/bin/env python
productos = {
        'INF-001':['Producto1', 55.90],
        'INF-002':['Producto2', 14.90],
        'INF-003':['Producto3', 25.50],
        'INF-004':['Producto1', 18]
        }
facturacion = {
        '001':{'INF-001':2, 'INF-003':1, 'INF-010':1},
        '001':{'INF-002':3, 'INF-004':1},
        None:None,
        '003':{'INF-002':1}, 
        '004':{'INF-009':2}
        }
errores = {}
total_facturado = 0

for value in facturacion.items():
    if value[0] is not None:
        print('Factura %s' % value[0])
        total_factura = 0
        err_linea = []
        lineas = value[1].items()
        print('\t Productos')
        err = False
#Proceso lineas
        for linea in lineas:
            codigo_producto = linea[0]
            cantidad_producto = linea[1]
            total_linea = 0

            producto = productos.get(codigo_producto)
            if producto is not None:
                total_linea = cantidad_producto * producto[1]
                print('\t\t %s, Cantidad %s, Precio unitario %.2f, \
                        Subtotal %.2f', % (producto[0], cantidad_producto,
                            producto[1], total_linea))
                total_factura += total_linea
            else:
                err = True
                err_linea.append(codigo_producto)

        print('\t Total facturado %f' % total_factura)
        total_facturado += total_factura

        if err:
            errores[value[0]] = err_linea

print('Total facturado: ' + total_facturado)


