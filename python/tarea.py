#Escribe un programa que pida al usuario un número en metros y lo convierta a centímetros.

#entrada
numero_en_metros = input("Ingrese un número en metros: ")

#convertir los metros a numero
numero_en_metros = int(numero_en_metros)

#Conversión de metros a centímetros
numero_en_centimetros = numero_en_metros * 100

#salida
print(numero_en_centimetros) 

#Crea un programa que pida el nombre del usuario y su edad. Luego, calcula cuántos años tendrá en 10 años.

#entrada
nombre = input("cómo te llamas? ")
edad = int(input("qué edad tienes? "))

#calcular la edad que tendrá en 10 años
edad = edad + 10

#salida
print(f"Hola {nombre}, en 10 años tendrás {edad} años.") 

#area  un rectangulo

#pedir al usuario base y altura de un rectangulo
base = float(input("ingrese la base"))
altura = float(input("ingrese la altura"))

#calcular el area
area = base * altura

#mostrar el resultado
print(f"El área del rectángulo es: {area}")

#Pide al usuario dos números y muestra la suma, resta, multiplicación y división de esos números.

#entradas
numero_1 = float(input("Ingrese un número: "))
numero_2 = float(input("Ingrese otro número: "))

#calcular suma
suma = numero_1 + numero_2

#calcular resta
resta = numero_1 - numero_2

#multiplicacion
multiplicacion = numero_1 * numero_2

#division
division = numero_1 / numero_2

#salida

print(f"suma: {suma}")
print(f"resta: {resta}")
print(f"multiplicacion: {multiplicacion}")
print(f"division: {division}")
print(" ")
print(f"suma: {suma}\nresta: {resta}\nmultiplicacion: {multiplicacion}\ndivision: {division}") 

#Pide al usuario el precio de un producto y calcula el precio final con un IVA del 19%.

#entrada
precio_producto = int(input("ingrese el precio del producto: "))

#calcular el iva
preciofinal=precio_producto*1.19

#salida
print(f"El precio final con IVA es: ${preciofinal}")

#Solicita tres números al usuario y muestra su promedio.
#entrada
numero_1=float(input("número 1: "))
numero_2=float(input("número 2: "))
numero_3=float(input("número 3: "))

#calcular el promedio
promedio = (numero_1+numero_2+numero_3)/3

#salida
print(f"El promedio es: {promedio}")

#Pide al usuario una cantidad de horas, minutos y segundos, y calcula el tiempo total en segundos.

#variables
horas=int(input("hora: "))
minutos=int(input("minutos: "))
segundos=int(input("segundos: "))

#cálculo
total_segundos = (horas*3600)+(minutos*60)+segundos

#print
print(f"total de segundos: {total_segundos}")