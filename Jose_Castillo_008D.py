import os
import csv
import time
import random

limpiar = 'cls'
os.system('cls')
def pedidos():
    with open ('pedido.csv', 'w', newline='') as archivo_csv:
        lector_csv = archivo_csv.writable
        lector_csv = archivo_csv.write 
        [ 
            ['Nro.pe', 'Cliente', 'Dirección','Sector', 'Saco 5kg', 'Saco 10kg', 'Saco20kg']
        ]
        
def menu():
        print('''
        Bienvenido al menu de venta de comida para gatos!
        
        1. Registrar pedido
        2. Listar todos los pedidos
        3. Imprimir hoja de ruta
        4. Salir del programa ''')
menu()

def opciones():
    acceso=1
    while acceso==1:
        try:
            opc=int(input('Ingrese una opción del 1 al 4: '))
        except ValueError:
            print('El valor ingresado es incorrecto, favor intente nuevamente')
        break
    if opc==1:
        Nombre=(input('Ingrese su nombre: '))
        Dirección=(input('Ingrese su dirección: '))
        Sector=(input('Ingrese su sector: '))
        Saco5kg=int(input('Ingrese cantidad de sacos de 5kg: '))
        Saco10kg=int(input('Ingrese cantidad de sacos de 10kg: '))
        Saco20kg=int(input('Ingrese cantidad de sacos de 20kg: '))
    elif opc==2:
        print(f'''
            Cliente: {Nombre}
            Dirección: {Dirección}
            Sector: {Sector}
            Saco 5kg: {Saco5kg}
            Saco 10kg: {Saco10kg}
            Saco 20kg: {Saco20kg}
            ''')
    elif opc==3:
        print(f'Seleccione su hoja de ruta:')
    elif opc==4:
        print('¡Gracias por preferir nuetro local!')
opciones()