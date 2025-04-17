import requests

def main():
    #se crea un bucle para preguntar la acción a realizar por el usuario
    while True:
        #se imprime el menú de opciones
        print("¿Qué acción deseas realizar?\n1. Enviar un mensaje\n2. Ver los mensajes anteriores\n3. Salir")
        print("----------------------------------------------")
        answer = input("Ingrese el valor de una acción (1, 2 ó 3): ")
        #si el usuario ingresa a opción 1
        if answer == "1":
            text = input("Ingrese el mensaje: ") #se le pide que ingrese un mensaje
            post_message(text) #se postea el mensaje
            print("¡Mensaje enviado con éxito!") #se le muestra un mensaje, confirmando que el mensaje se ha enviado
        #si el usuario ingresa a opción 2
        elif answer == "2":
            print(f"Estos son los mensajes anteriores:") #se muestran los mensaje anteriores
            get_message()
        elif answer == "3":
            print("¡Vueve pronto!")
            break
        else: #si no ingresa una opción válida, se envía el siguiente mensaje:
            print(" ---------------------------")
            print("| Ingrese una opción válida |")
            print(" ---------------------------")

#se define la función para enviar un mensaje
def post_message(text):
    #se guarda el valor de la url
    url = "https://3bda700d-ebe7-421a-bbc1-20cb9289f0cc-00-c4yvkdzp1nlg.janeway.replit.dev/send_cheep"
    #se guarda el mensaje como objeto
    myobj = {"message": f"{text}"}
    #se postea el mensaje
    message = requests.post(url, json = myobj)

def get_message():
    #se guarda el valor de la url
    url = "https://3bda700d-ebe7-421a-bbc1-20cb9289f0cc-00-c4yvkdzp1nlg.janeway.replit.dev/get_cheeps"
    #se busca la URL utilizando la API
    response = requests.get(url)
    #se transforma el resultado a json
    messages = response.json()
    #se imprime cada mensaje
    for element in messages:
        print(element)
    print("----------------------------")

if __name__ =="__main__":
    main()