# Ejemplo conversion tipo de datos

# Convertir de cadena a numero 
numero_cadena = "10"
numero_entero = int(numero_cadena)

print(f"Valor numero en cadena: {numero_cadena} ")
print(f"Valor numero en entero: {numero_entero} ")


# Convertir de cadena a flotante
numero_cadena = "10.5"
numero_flotante = float(numero_cadena)

print(f"Cadena a flotante: {numero_flotante} ")

# Convertir de numero a cadena 
numero_entero = 23
numero_cadena = str(numero_entero)

print(f"Entero a cadena: {numero_cadena} ")

# Convertir a booleano
# Tipo bool es falso en los siguientes casos:
# si el valor es 0, cadena vacia, none es falso
# Regresa True si el valor es diferente de 0, si es diferente de cadena vacia, si es diferente de None
# Y tambien si es diferente de none 
numero_booleano = 0 
numero_booleano = bool(numero_booleano)

print(f"Valor booleano de 0: {numero_booleano} ")

numero_booleano = 5 
numero_booleano = bool(numero_booleano)

print(f"Valor booleano de 5: {numero_booleano} ") # True

cadena = ''
booleano = bool(cadena)
print(f"Valor booleano de cadena vacia: {booleano} ") # False, incluye colecciones vacias

cadena = 'Hola'
booleano = bool(cadena)
print(f"Valor booleano de cadena con valor: {booleano} ") # True

variable = None
booleano = bool(variable)
print(f"Valor booleano de None: {booleano} ") # False