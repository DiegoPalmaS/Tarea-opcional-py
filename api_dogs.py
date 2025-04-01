import requests

def names():
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url)
    if response.status_code == 200: #si se encuentra la lista de perros
        data = response.json() #convierte la respuesta a json
        dogs_list = data['message'] #obtiene los perros de la respuesta
        print("Razas de perros disponibles:")
        for breed in dogs_list.keys(): #recorre todas las razas
            print(breed) # Imprime el nombre de la raza
    else: #si no se encuentra la lista de perros
        print("No se encontraron razas de perros")

def main():
    names() #llama a la funcion names para mostrar las razas de perros

if __name__ == "__main__":
    main() #llama a la funcion main para ejecutar el programa
