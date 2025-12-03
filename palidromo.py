# practica1.py

# 1. Captura de datos con input()
nombre = input("Ingresa tu nombre: ")
edad = int(input("¿Cuantos años tienes?"))
estudias = input("¿Si estudias? (True/False): ")


# 2. Conversión de tipos
nombre = int(nombre)
edad = int(edad)
estudias = estudias == "True"  # Convierte a booleano

# 3. Mostrar los datos capturados
print("\n--- Datos Capturados ---")
print("Nombre completo:", nombre)
print("Edad:", edad)
print("¿Que carrera estudia?:", estudias)
