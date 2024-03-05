lista = []
def agregar(item):
  lista.append(item)
def remover(item):
  if item in lista:
    lista.remove(item)
def visualizar():
  print(lista)
while True:
  print("Opciones:")
  print("1. Añadir item")
  print("2. Remover item")
  print("3. Visualizar lista")
  print("4. Salir")
  opcion = int(input("Introduzca una opción: "))
  if opcion == 1:
    item = input("Introduzca el item a añadir: ")
    agregar(item)
  elif opcion == 2:
    item = input("Introduzca el item a eliminar: ")
    remover(item)
  elif opcion == 3:
    visualizar()
  elif opcion == 4:
    print("¡Hasta luego!")
    break
  else:
    print("Opción no válida")
