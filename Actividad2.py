#Un alumno desea saber cuál será su calificación final en una materia. Dicha calificación se compone de los siguientes porcentajes: 50% proyecto integrador, 30% nota técnica y 20% nota tareas. 

#entrada
mark1=float(input("Ingrese la nota del proyecto integrador: "))
mark2=float(input("Ingrese la nota técnica: "))
mark3=float(input("Ingrese la nota de tareas: "))

#calcular la nota final
final_mark = (mark1*0.5)+(mark2*0.3)+(mark3*0.2)

#salida
print(f"La nota final es: {final_mark}")





#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.

#entrada
total_purchase=float(input("Ingrese el total de la compra: "))

#calcular total a pagar
final_price = total_purchase*0.85

#salida
print(f"El total a pagar es: {final_price}")








# Realizar un algoritmo que calcule la edad de una persona.


#entrada
birth_year=int(input("Ingrese su año de nacimiento: "))
current_year=int(input("Ingrese el año actual: "))

#calcular la edad
age = current_year-birth_year

#salida
print(f"Su edad es: {age}")