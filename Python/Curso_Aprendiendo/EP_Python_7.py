# Sistema de generador ID Unico
"""
Con los datos recibidos el sistema debera realizar lo siguiente:
- Del valor recibido de nombre, usar solo los 2 primera letras y convertirlas a mayusculas
- Del valor de apellido, usar las 2 primeras letras y convertirlas a mayusculas
- Del valor de año, tomar los ultimos 2 digitos

Ademas el sistema debera de generar un valor aleatorio de 4 digitos, con la funcion randint
Finalmente, con los datos obtenidos, generar un ID unico uniendo los valores como sigue

Ej. Nombre -> Juan -> JU
    Apellido -> Perez -> PE
    Año -> 1990 -> 90
    Valor aleatorio -> 1234
    ID unico -> JUPE90-1234
"""
from random import randint

print("--- Sistema de generador ID Unico ---")
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
anio = input("Ingresa tu año de nacimiento: ")
nombre_M = nombre
apellido_M = apellido

print("\n--- Generando ID unico ---")
nombre = nombre[:2].upper()
apellido = apellido[:2].upper()
anio = anio[-2:]
valor_aleatorio = randint(1000, 9999)

id_unico = f"{nombre}{apellido}{anio}-{valor_aleatorio}"
print(f"Persona: {nombre_M} {apellido_M} ")
print(f"ID unico generado: {id_unico} ")
