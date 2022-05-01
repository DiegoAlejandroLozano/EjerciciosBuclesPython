'''
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
'''

#Opción 1

'''
frase = input("Ingrese una frase: ")
letra = input("Ingrese la letra: ")

contador = 0

for i in range(0, len(frase)):
    if letra == frase[i]:
        contador = contador + 1

print("La letra %s aparece %d veces en la frase" % (letra, contador))

frase.count()
'''

#Opción 2

frase = input("Ingrese una frase: ")
letra = input("Ingrese la letra: ")

print("La letra '%s' aparece %d veces en la frase" % (letra, frase.count(letra)))