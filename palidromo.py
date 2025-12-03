# def es_palindromo(texto):
    # Eliminar espacios y convertir a minúsculas
    limpio = texto.replace(" ", "").lower()

    # Comparar con el texto invertido
    return limpio == limpio[::-1]


# Pedir texto al usuario
entrada = input("Ingresa un texto: ")

# Llamar a la función y mostrar resultado
if es_palindromo(entrada):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
