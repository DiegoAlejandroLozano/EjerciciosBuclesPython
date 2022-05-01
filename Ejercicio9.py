'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
'''

CONTRASEÑA = "LuNaKatIA"

while True:
    password = input("Ingrese la contraseña: ")

    if password == CONTRASEÑA:
        print("Contraseña correcta !!!")
        break
    else:
        print("Contraseña incorrecta :(")