print("Hola, Mundo!")
def mostrar_menu():
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")

tareas = []

while True:
    mostrar_menu()
    opcion = input("Elige una opcion (1-4): ")

    if opcion == "1":
        if not tareas:
            print("\n No tienes tareas pendientes.")
        else:
            print("\n Tus tareas:")
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")

    elif opcion == "2":
        nueva_tarea = input("\nEscribe la nueva tarea: ")
        if nueva_tarea.strip():
            tareas.append(nueva_tarea)
            print(f" Tarea '{nueva_tarea}' agregada.")

    elif opcion == "3":
        if not tareas:
            print("\n No hay tareas para eliminar.")
        else:
            num = int(input("\nNumero de tarea a eliminar: "))
            if 1 <= num <= len(tareas):
                eliminada = tareas.pop(num - 1)
                print(f" Tarea '{eliminada}' eliminada.")
            else:
                print(" Numero invalido.")

    elif opcion == "4":
        print("\n Hasta luego!")
        break
    else:
        print(" Opcion no valida, intenta de nuevo.")
