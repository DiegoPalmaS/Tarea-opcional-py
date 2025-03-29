""" #método 1
#se defina una función
def sumar(lista):
    #se declara una variable para acumular la suma
    suma = 0
    #se recorre la lista de números
    for numero  in lista:
        #se le suma cada número, a la variable suma
        suma = suma + numero 
    #se retorna la suma
    return suma

#método 2
def suma_rapida(lista):
    #declaro una variable con el valor de la suma
    suma2 = sum(lista)
    #retorno la suma
    return suma2

lista_usuario = [1,2,3]
print(suma_rapida(lista_usuario)) """

""" # Función para multiplicar los elementos de una lista
#forma 1 (con for)
def multiplicar(lista):
    #declaro una variable, para guardar el producto (elemento neutro en la multiplicación)
    resultado = 1
    #se crea un for para recorrer toda la lista
    for numero in lista:
        #se guarda el valor de cada multiplicación
        resultado = resultado * numero
    #se retorna el valor de la multiplicación de todos los números
    return resultado

lista_test = [1,2,3,4]
print(multiplicar(lista_test))

#forma 2 (con while)
def multiplicar_con_while(lista):
    #se crea una variable, para guardar el resultado del producto
    resultado = 1
    #se crea una variable, para detener en algún momento el while
    contador = 0
    #se recorre la lista con un while
    while contador<(len(lista)):
        #qué número estoy recorriendo
        numero = lista[contador]
        #se multiplica el número que se está recorriendo, por el resultado acumulado
        resultado = resultado * numero
        #se le agrega al contador +1, para que el ciclo while termina en algún momento
        contador = contador + 1

    return resultado

lista_test = [1,2,3,4]
print(multiplicar_con_while(lista_test))"""

#comprobar si el número es par ó entero
#se define la función
def par_o_entero(numero):
    #se compara el número, para saber si cumple con las condiciones
    if numero%2 == 0 or numero == int(numero): #si el número es par ó entero
        return True #retorna true
    else: #en el caso contrario
        return False #retorna false