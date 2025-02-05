# Sistema de empleados 
print("--- Sistema de empleados ---")

nombre_empleado = input("Ingresa el nombre del empleado: ")
edad_empleado = int(input("Ingresa la edad del empleado: "))
salario_empleado = float(input("Ingresa el salario del empleado: "))
es_jefe_departamento = input("Es jefe de departamento (Si/No)? ")

# Vamos a convertir a un tipo booleano la variable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == "si"

# Imprimer los valores del empleado
print("\n--- Datos del empleado ---")
print(f"Nombre: {nombre_empleado} ")
print(f"Edad: {edad_empleado} ")
print(f"Salario: {salario_empleado:.2f} ")
print(f"Jefe de departamento: {es_jefe_departamento} ")