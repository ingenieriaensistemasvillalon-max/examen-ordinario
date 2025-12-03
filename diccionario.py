# Diccionario inicial de inventario
inventario = {
    "mouse": 10,
    "teclado": 6,
    "monitor": 3
}

# Pedir datos al usuario
producto = input("¿Qué producto quieres retirar? (mouse / teclado / monitor): ")
cantidad = int(input("¿Cuántas unidades quieres retirar?: "))

# Verificar si el producto existe
if producto in inventario:

    # Verificar si hay suficiente stock
    if cantidad <= inventario[producto]:
        inventario[producto] -= cantidad
        print("\nRetiro realizado correctamente.")
    else:
        print("\nERROR: No hay suficientes unidades disponibles.")

else:
    print("\nERROR: El producto no existe en el inventario.")

# Mostrar inventario actualizado
print("\n--- Inventario actualizado ---")
for item, stock in inventario.items():
    print(f"{item}: {stock}")
