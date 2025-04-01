import requests

def pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200: #si se encuentra al pokemon
        data = response.json() #convierte la respuesta a json
        print(f"Nombre: {data['name']}") # Imprime el nombre del pokemon
        #mostrar los tipos del pokemon
        types = [] # Lista para almacenar los tipos
        for type in data['types']: #recorre todos los tipos
            types.append(type['type']['name']) # Agrega cada tipo a la lista
        print("tipo: "+ ", ".join(types)) # Imprime todos los tipos separados por comas
        #mostrar los ataques del pokemon
        attacks = [] # Lista para almacenar los ataques
        for attack in data['abilities']: #recorre todas las habilidades
            attacks.append(attack['ability']['name']) # Agrega cada habilidad a la lista
        print("Ataques: "+ ", ".join(attacks)) # Imprime todos los ataques separados por comas
    else: #si no se encuentra el pokemon
        print("Pokemon no encontrado")

def main():
    poke_name = input("Introduce el nombre del pokemon: ")
    pokemon(poke_name)



if __name__ == "__main__":
    main()