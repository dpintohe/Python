import sqlite3
from Operativas.Clases_Almacen import *

MiAlmacen = almacen()
MiAlmacen.crear()
while True:
    print("1. Ver Producto")
    print("2. Introducir Producto")
    print("3. Modificar producto")
    print("4. Ver Lista Productos")
    print("5. Necesitar stock")
    print("6. Valor stock")
    opcion = int(input("Introducir opcion: "))
    if opcion == 1:
        Referencia = input("Introduzca la referencia a consultar: ")
        MiAlmacen.ver(Referencia)
    elif opcion == 2:
        Origen = input("Introduzca Origen: ")
        Nombre = input("Introduzca Nombre: ")
        Cantidad = int(input("Introduzca Cantidad: "))
        Precio = float(input("Introduzca Precio: "))
        Posicion = input("Introduzca Posicion: ")
        datos=[Origen, Nombre, Cantidad, Precio, Posicion]
        MiAlmacen.Introducir(datos)
    elif opcion == 3:
        Referencia = input("Introduzca la referencia a modificar: ")
        MiAlmacen.ver(Referencia)
        print("conceptos a modificar")
        print("1. Cantidad")
        print("2. Precio")
        print("3. Posicion")
        Concepto = int(input("Introduzca el concepto a modificar: "))
        MiAlmacen.modificar(Concepto, Referencia)
        MiAlmacen.ver(Referencia)    
    elif opcion == 4:
        MiAlmacen.listar()
    elif opcion == 5:
        minimo = int(input("A partir de que valor hay que pedir stock: "))
        MiAlmacen.stock(minimo)
    elif opcion == 6:
        MiAlmacen.valor()
    else:
        break