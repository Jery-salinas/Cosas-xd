# Receta de cocina
"""
Crear un programa para solicitar algunos valores importantes para una receta de cocina
Lo valores que debe introducir el usuario son:
- Nombre de la receta
- Ingredientes
- Tiempo de preparacion (en minutos)
- Dificultad (Facil, Media, Dificil)
Mandar a imprimir la receta 
"""
nombre_receta = input("Ingresa el nombre de la receta: ")
ingredientes = input("Ingresa los ingredientes de la receta: ")
tiempo_preparacion = int(input("Ingresa el tiempo de preparacion (en minutos): "))
dificultad = input("Ingresa la dificultad de la receta (Facil, Media, Dificil): ")
print("----------------------------------")
print(f"Receta: {nombre_receta} ")
print(f"Ingredientes: {ingredientes} ")
print(f"Tiempo de preparacion: {tiempo_preparacion} minutos ")
print(f"Dificultad: {dificultad} ")
