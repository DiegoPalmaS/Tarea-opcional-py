import requests

def main():
    print("Hello learners!")

#se define función para encontra la trivia con el número solicitado
def trivia_fetch(number):
    #se transforma el número a string
    number=str(number)
    #se crea la URL
    url = "http://numbersapi.com/"+number+"?json"
    #se busca la URL utilizando la API
    response = requests.get(url)
    #se transforma el resultado a json
    trivia = response.json()
    return trivia

if __name__=="__main__":
    main()
