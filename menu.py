import requests
from tabulate import tabulate

base_url = "https://api-rest-python-six.vercel.app"

def print_menu():
    print("MENU:")
    print("1. Ver lista de animales")
    print("2. Crear un nuevo animal")
    print("3. Actualizar un animal")
    print("4. Eliminar un animal")
    print("5. Salir")

def get_animals():
    response = requests.get(f'{base_url}/get/animals')
    if response.status_code == 200:
        animals = response.json()
        if animals:
            headers = animals[0].keys()
            rows = [animal.values() for animal in animals]
            print(tabulate(rows, headers=headers, tablefmt='grid'))
        else:
            print("No se encontraron animales")
    else:
        print("Error al obtener la lista de animales")


def create_animal():
    nombre = input("Ingrese el nombre del animal: ")
    cientifico = input("Ingrese el nombre científico del animal: ")
    region = input("Ingrese la región del animal: ")
    latitud = input("Ingrese la latitud del animal: ")
    longitud = input("Ingrese la longitud del animal: ")
    img = input("Ingrese la URL de la imagen del animal: ")

    data = {
        "nombre": nombre,
        "cientifico": cientifico,
        "region": region,
        "latitud": latitud,
        "longitud": longitud,
        "img": img
    }

    response = requests.post(f'{base_url}/post/animals', json=data)
    if response.status_code == 200:
        print("Animal creado exitosamente")
    else:
        print("Error al crear el animal")

def update_animal():
    animal_id = input("Ingrese el ID del animal a actualizar: ")
    nombre = input("Ingrese el nuevo nombre del animal: ")
    cientifico = input("Ingrese el nuevo nombre científico del animal: ")
    region = input("Ingrese la nueva región del animal: ")
    latitud = input("Ingrese la nueva latitud del animal: ")
    longitud = input("Ingrese la nueva longitud del animal: ")
    img = input("Ingrese la nueva URL de la imagen del animal: ")

    data = {
        "nombre": nombre,
        "cientifico": cientifico,
        "region": region,
        "latitud": latitud,
        "longitud": longitud,
        "img": img
    }

    response = requests.put(f'{base_url}/update/animals/{animal_id}', json=data)
    if response.status_code == 200:
        print("Animal actualizado exitosamente")
    else:
        print("Error al actualizar el animal")

def delete_animal():
    animal_id = input("Ingrese el ID del animal a eliminar: ")

    response = requests.delete(f'{base_url}/delete/animals/{animal_id}')
    if response.status_code == 200:
        print("Animal eliminado exitosamente")
    else:
        print("Error al eliminar el animal")

def main():
    while True:
        print_menu()
        choice = input("Ingrese su opción: ")
        if choice == '1':
            get_animals()
        elif choice == '2':
            create_animal()
        elif choice == '3':
            update_animal()
        elif choice == '4':
            delete_animal()
        elif choice == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
