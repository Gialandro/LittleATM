###Requirments:
#Bueno un cajero automático que solo tenga un usuario y contraseña,
#y un monto fijo (obviamente solo al cerrar el programa y volverlo a abrir).
#Se pedirá usuario y contraseña para poder entrar al menú
#Tiene que mostrar retirar, ingresar, consultar y salir a la pantalla de login
#No puede retirar mas de 5000
#Y no puede depositar mas de 7000
#Y si se puede cada que ingrese a una opción o cabie de login a menu se limpie la pantalla

import getpass

us = 'Admin'
pwd = 'p@$$w0rd'
username = ''
password = ''
while username != us and pwd != password:
    username = input('Usuario: ')
    password = getpass.getpass('Contraseña: ')