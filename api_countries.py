import requests

def countries(name):
    #guardo la URL
    url=f"https://restcountries.com/v3.1/name/{name}"
    #hago la peticion a la API
    response=requests.get(url)
    #verifico si la respuesta es correcta
    if response.status_code==200:
        #convierto la respuesta a json
        data=response.json()
        #imprimo la capital
        print(f"Capital: {data[0]['capital'][0]}")
        #imprimo la poblacion
        print(f"Poblacion: {data[0]['population']}")
        #imprimo el idioma principal
        print(f"Idioma Principal: {list(data[0]['languages'].values())[0]}")
    else:
        print("Pais no encontrado")

def main():
    #pido el nombre del pais
    name=input("Ingrese el nombre de un país: ")
    #llamo a la funcion countries
    countries(name)

if __name__=="__main__":
    main()

