# Programa para tomar pedidos en un restaurante de sushi con opción de descuento y pedidos múltiples

while True:
    # Definir el menú de sushi con números de ítem, nombres y precios en pesos chilenos
    menu = {
        '1': {'name': 'California Roll', 'price': 7000},
        '2': {'name': 'Spicy Tuna Roll', 'price': 7500},
        '3': {'name': 'Salmon Nigiri', 'price': 6000},
        '4': {'name': 'Eel Roll', 'price': 8500},
        '5': {'name': 'Shrimp Tempura Roll', 'price': 8000},
    }

    # Mensaje de bienvenida y mostrar el menú al cliente
    print("\n¡Bienvenido al Restaurante de Sushi!")
    print("Aquí está nuestro menú:")
    for key in menu:
        print(f"{key}. {menu[key]['name']} - ${menu[key]['price']} CLP")

    # Inicializar un diccionario vacío para almacenar el pedido del cliente
    order = {}

    # Bucle para tomar pedidos hasta que el cliente decida terminar
    while True:
        choice = input("Ingrese el número del sushi que desea ordenar (o 'q' para terminar): ")
        if choice.lower() == 'q':
            break  # Salir del bucle de pedidos si el cliente termina
        if choice not in menu:
            print("Opción inválida. Por favor seleccione un número válido del menú.")
            continue  # Pedir nuevamente si la opción es inválida
        try:
            quantity = int(input(f"¿Cuántos {menu[choice]['name']} desea ordenar? "))
            if quantity <= 0:
                print("Por favor ingrese una cantidad positiva.")
                continue  # Pedir nuevamente si la cantidad no es positiva
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número.")
            continue  # Pedir nuevamente si la entrada no es un número
        # Agregar la cantidad al pedido, o actualizar si ya fue ordenado
        if choice in order:
            order[choice] += quantity
        else:
            order[choice] = quantity

    # Solicitar código de descuento
    codigo_descuento = input("Ingrese código de descuento si tiene (o presione Enter para continuar): ")

    # Después de ordenar, mostrar el resumen del pedido y el costo total
    if order:
        print("\nResumen del Pedido:")
        total = 0
        for item_key in order:
            item_name = menu[item_key]['name']
            item_price = menu[item_key]['price']
            quantity = order[item_key]
            item_total = item_price * quantity
            total += item_total
            print(f"{item_name} x {quantity} = ${item_total} CLP")
        # Aplicar descuento si el código es correcto
        if codigo_descuento.lower() == "soyotaku":
            descuento = total * 0.10
            total_con_descuento = total - descuento
            print(f"\nCódigo de descuento aplicado: 10%")
            print(f"Descuento: -${descuento:.0f} CLP")
            print(f"Total con descuento: ${total_con_descuento:.0f} CLP")
        else:
            print("\nNo se aplicó ningún código de descuento.")
            print(f"Total: ${total} CLP")
    else:
        print("No se ordenaron productos. ¡Gracias por su visita!")

    # Preguntar si desea hacer otro pedido
    otro_pedido = input("\n¿Desea hacer otro pedido? (s/n): ")
    if otro_pedido.lower() != 's':
        print("Gracias por su visita. ¡Hasta luego!")
        break
