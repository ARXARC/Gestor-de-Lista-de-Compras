lista = []
print("Opciones:\n","1. Añadir item\n","2. Remover item\n","3. Visualizar lista\n","4. Salir\n")
while True:
    opcion = input("Introduzca una opción: ")
    if opcion == "1":
        item = input("Introduzca el item a añadir: ")
        lista.append(item)
        print(f"Añadido {item} a la lista de compras.")
    elif opcion == "2":
        item = input("Introduzca el item a eliminar: ")
        if item in lista:
            lista.remove(item)
            print(f"Eliminado {item} de la lista de compras.")
        else:
            print(f"{item} no existe ese item")
    elif opcion == "3":
        print("Lista de compras:")
        for i, item in enumerate(lista, start=1):
            print(f"{i}. {item}")
    elif opcion == "4":
        print("Adios")
        break
    else:
        print("Opción no válida.")
