import webbrowser

peliculas = []

def agregar_pelicula():
    nombre = input("Ingrese el nombre de la película: ")
    descripcion = input("Ingrese la descripción de la película: ")
    anio_lanzamiento = input("Ingrese el año de lanzamiento: ")
    genero = input("Ingrese el género de la película: ")
    reparto = input("Ingrese el reparto de la película: ")
    director = input("Ingrese el nombre del director: ")
    enlace = input("Ingrese el enlace de la película: ")

    pelicula = {
        'Nombre': nombre,
        'Descripción': descripcion,
        'Año de lanzamiento': anio_lanzamiento,
        'Género': genero,
        'Reparto': reparto,
        'Director': director,
        'Enlace': enlace
    }

    peliculas.append(pelicula)
    print(f'La película "{nombre}" ha sido agregada correctamente.\n')

def mostrar_peliculas(): #
    if not peliculas:
        print("No hay películas en la lista.")
        return

    for idx, pelicula in enumerate(peliculas, 1):
        print(f'\nPelícula {idx}: {pelicula["Nombre"]}')
        for key, value in pelicula.items():
            print(f'{key}: {value}')
        print('-' * 30)

def remover_pelicula():
    mostrar_peliculas()
    if not peliculas:
        print("No hay películas para remover.")
        return

    try:
        indice = int(input("Ingrese el número de la película que desea remover: "))
        if 1 <= indice <= len(peliculas):
            pelicula_removida = peliculas.pop(indice - 1)
            print(f'La película "{pelicula_removida["Nombre"]}" ha sido removida correctamente.\n')
        else:
            print("Número de película no válido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

def abrir_enlace_pelicula():
    mostrar_peliculas()
    if not peliculas:
        print("No hay películas para abrir.")
        return

    try:
        indice = int(input("Ingrese el número de la película que desea abrir: "))
        if 1 <= indice <= len(peliculas):
            enlace = peliculas[indice - 1].get('Enlace')
            if enlace:
                webbrowser.open(enlace)
                print(f'Abriendo enlace para la película "{peliculas[indice - 1]["Nombre"]}".\n')
            else:
                print("La película seleccionada no tiene un enlace asociado.")
        else:
            print("Número de película no válido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

def menu():
    while True:
        print("\n--- Menú de Películas ---")
        print("1. Agregar Película")
        print("2. Mostrar Películas")
        print("3. Remover Película")
        print("4. Abrir Enlace de Película")
        print("5. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        
        if opcion == '1':
            agregar_pelicula()
        elif opcion == '2':
            mostrar_peliculas()
        elif opcion == '3':
            remover_pelicula()
        elif opcion == '4':
            abrir_enlace_pelicula()
        elif opcion == '5':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    menu()
