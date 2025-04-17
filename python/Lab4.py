# def main():
#ingresa una lista de números, retorna la suma de estos.
def addmultiplenumbers(list):
    #se decrara una variable para acumular la suma
    suma = 0
    #se recorre la lista de números, para sumarlos
    for numero in list: #para cada número en la lista
        #se suma el número a la variable suma
        suma += numero #es lo mismo --> suma = suma + numero
    #se retorna la suma
    return suma
#ingresa una lista de números, retorna el producto de estos.
def multiplymultiplenumbers(list):
    #se decrara una variable para acumular el producto
    producto = 1
    #se recorre la lista de números, para multiplicarlos
    for numero in list:
        #se multiplica el número con la variable producto
        producto *= numero
    #se retorna el producto
    return producto
#ingresa un solo número, retorna True si es par o entero, False si no lo es.
def isiteven(number):
    if number%2 == 0 or number == int(number):
        return True
    else:
        return False
#ingresa un solo número, retorna True si es entero, False si no lo es.
def isitaninteger(number):
    if number == int(number):
        return True
    else:
        return False

# if __name__=="__main__":
#     main()