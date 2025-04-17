# Pide al usuario un número n y usa un bucle while para generar una lista de los números del 1 al n.

#entrada
n = int(input("Ingrese un número: ")) #nombre_de_la_variable = input("mensaje que se le muestra al usuario")


#crear la lista de números
#creo una lista vacía
lista=[]
#creo una variable i que va a ir desde 1 hasta n
i=1
#mientras i sea menor o igual a n
while i<=n:
    #agrego i a la lista
    lista.append(i)
    #incremento i en 1 
    i+=1 #i=i+1


# salida
print(lista)

#Crea un programa que use un bucle for para sumar todos los números de una lista proporcionada por el usuario.

#entrada
lista_usuario = input("Ingrese una lista de números, separados por comas: ") #"1,2,3"

#convertir el string del input a una lista de números
lista_usuario = lista_usuario.split(",") #separo los elementos por coma
#lista_usuario = ["1","2","3"]

lista = [] #creo una lista vacía
for elemento in lista_usuario: #para cada elemento en la lista
    elemento = int(elemento) #convierto el elemento a un número entero
    lista.append(elemento) #agrego el elemento a la lista


#sumar la lista
suma = 0 #creo una variable para guarar el resultado de la suma
for elemento in lista: #para cada elemento en la lista
    suma = suma + elemento #le sumo el valor del elemento a la variable suma


#salida
print(f"La suma de los elementos es: {suma}") #muestro la sumas

#Solicita una lista de números al usuario y usa un bucle for para agregar solo los números pares a una nueva lista.

#entrada
lista_usuario = input("Ingrese una lista de números, separados por coma: ")
#lista_usuario es así --> "1,2,3,4"

#transformar el string del usuario en una lista
lista_usuario = lista_usuario.split(",")
#lista_usuario es así --> ["1","2","3","4"]

#crear una lista vacía
lista = []

#agregar los números a la lista vacía
for elemento in lista_usuario: #para cada elemento en la lista del usuario
    elemento = int(elemento) #tranformar el elemento de str a int
    if elemento%2 == 0: #si el elemto es par
        lista.append(elemento) #agregar el número a la lista

#salida
print(f"los números pares de tu lista son: {lista}")

#Escribe un programa que permita al usuario ingresar números (notas) hasta que escriba la palabra "fin". El programa debe calcular el promedio de las notas ingresadas. Usa un bucle while para obtener las notas y una condicional para determinar si el promedio indica que el usuario aprobó o reprobó.


#creo una lista vacía, para agregar las notas que ingrese el usuario
lista=[]
#se crea un bucle while True, para obtener las notas
while True:
    #se le pide al usuario ingresar una nota
    elemento = input("ingrese una nota, escriba 'fin' para finalizar: ")
    #si el usuario ingresa la palabra fin
    if elemento == "fin":
        #se termina el while
        break
    #transformar el la nota ingresada por el usuario de str a float
    elemento = float(elemento)
    #se agrega la nota a la lista
    lista.append(elemento)

#sumar los elementos de la lista
suma = 0 #creo una variable para guardar la suma
for i in lista:
    suma+=i # es lo mismo que: suma = suma + i

#calcular el promedio
promedio = suma/len(lista)
#redondear el promedio a 1 solo decimal
promedio = round(promedio,1)

#comprobar si la persona pasa o no de curso
if promedio >= 4.0:
    print(f"Aprueba, con un promedio de: {promedio}")
else:
    print(f"No aprueba, con un promedio de: {promedio}")