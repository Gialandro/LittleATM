###Requirments:
#Bueno un cajero automático que solo tenga un usuario y contraseña,
#y un monto fijo (obviamente solo al cerrar el programa y volverlo a abrir).
#Se pedirá usuario y contraseña para poder entrar al menú
#Tiene que mostrar retirar, ingresar, consultar y salir a la pantalla de login
#No puede retirar mas de 5000
#Y no puede depositar mas de 7000
#Y si se puede cada que ingrese a una opción o cabie de login a menu se limpie la pantalla

import getpass
import os

us = '123'#'Admin'
pwd = '123'#'p@$$w0rd'
username = ''
password = ''
menu = 0
capital = 9999.99
ingreso = 0.00
retiro = 7000.00
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
    pass
if username == us and password == pwd:
    while menu <= 0 or menu >= 4:
        menu = int(input('Menu: \n 1. Ingresar \n 2. Retirar \n 3. Consultar \n 4. Salir \n'))
        if menu == 1:
            while ingreso >= 7000.00:
                ingreso = float(input('Cantidad a depositar (Maximo $7000.00): $'))
            pass