import getpass
import os
import time
import sys

us = 'Admin'
pwd = 'p@$$w0rd'
username = ''
password = ''
menu = ''
capital = 9999.99
ingreso = 7000.00
retiro = 5000.00
while username != us or pwd != password:
    os.system('cls || clear')
    if username != '' and username != us:
        print('Usuario incorrecto, intente nuevamente.')
    if password != '' and password != pwd:
        print('Contraseña incorrecta, intente nuevamente.')
    if username == '' and password == '':
        print('***Bienvenido*** \n Ingrese sus datos para acceder...')
    username = input('Usuario: ')
    password = getpass.getpass('Contraseña: ')
if username == us and password == pwd:
    while True:
        os.system('cls || clear')
        menu = ''
        menu = input('Menu: \n 1. Ingresar \n 2. Retirar \n 3. Consultar \n 4. Salir \n')
        if menu == '1':
            while ingreso >= 7000.00:
                ingreso = float(input('Cantidad a depositar (Maximo $7,000.00): $'))
                if ingreso < 7000.00:
                    capital += ingreso
                    print('Capital actual: ${0}'.format(capital))
                    time.sleep(1)
            ingreso = 7000.00
        elif menu == '2':
            while retiro >= 5000.00:
                retiro = float(input('Cantidad a retirar (Maximo $5,000.00): $'))
                if retiro < 5000.00 and retiro < capital:
                    capital -= retiro
                    print('Capital actual: ${0}'.format(capital))
                    time.sleep(1)
            retiro = 5000.00
        elif menu == '3':
            print('Su saldo actual es de: ${0}'.format(capital))
            time.sleep(1)
        elif menu == '4':
            print('Saliendo...')
            time.sleep(1)
            sys.exit()