# Sistema generador Emails
"""
Se solicita crear una nueva version del sistema de generador de emails
Para generar un email, se debera de solicitar los siguientes datos:
- Nombre 
- Apellido
- Nombre Empresa
- Dominio de la empresa
"""
print("--- Sistema generador Emails ---")

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
nombre_empresa = input("Ingresa el nombre de la empresa: ")
dominio_empresa = input("Ingresa el dominio de la empresa: ")

# Normalizar los valores recibidos
nombre = nombre.strip().lower().replace(" ", "")
apellido = apellido.strip().lower().replace(" ", "")
nombre_empresa = nombre_empresa.strip().lower().replace(" ", "")
dominio_empresa = dominio_empresa.strip().lower().replace(" ", "")

# Generar el email
email = f"{nombre}_{apellido}@{nombre_empresa}.{dominio_empresa}"
print(f"Email generado: {email} ")