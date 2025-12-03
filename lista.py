# Pedir números al usuario
valores = input("Ingrese algunos números separados por comas: ")

# Convertir la cadena en lista de enteros
lista = [int(x) for x in valores.split(",")]

# Calcular datos
mayor = max(lista)
menor = min(lista)
promedio = sum(lista) / len(lista)

# Mostrar resultados
print("Lista de números:", lista)
print("Número mayor:", mayor)
print("Número menor:", menor)
print("Promedio:", promedio)
