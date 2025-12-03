# Solicitar al usuario que ingrese una secuencia de números separados por comas y almacenarla en la variable 'valores'
valores = input("Ingrese algunos números separados por comas: ")

# Divide la cadena 'valores' en una lista usando comas como separadores y almacénala en la variable 'list'
list = values.split(",")

# Convierte la 'lista' en una tuple y guárdala en la variable 'tuple'
tuple = tuple(lista)

# Imprimir la lista
print('Lista: ', lista)

# Imprimir la tuple
print('Tuple: ', tuple)
