# Ejercicio con funciones 
from funcion import mostrar_lista, eliminar_posicion
print("Lista actual:", mostrar_lista())

posicion = int(input("Digite la posición que desea eliminar (0-4): "))

print("Lista actualizada:", eliminar_posicion(posicion))