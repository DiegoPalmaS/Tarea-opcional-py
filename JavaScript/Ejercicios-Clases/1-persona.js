/* 1. Crea una clase Persona
Objetivo: Abstraer una persona con sus propiedades básicas.
Instrucciones:
Crea una clase llamada Persona con las siguientes propiedades:

    nombre (string)
    edad (number)

Agrega un método llamado saludar() que devuelva un string como: "Hola, me llamo Juan y tengo 30 años."
Instancia al menos una persona y llama al método saludar(). */

class Persona {
    // Constructor de la clase Persona
    constructor(nombre, edad) {
        this.nombre = nombre;
        this.edad = edad;
    }
    // Método para saludar
    saludar() {
        return `Hola, me llamo ${this.nombre} y tengo ${this.edad} años.`;
    }
}

// Solicitar nombre y edad al usuario
const nombre = prompt("Ingrese el nombre de la persona: ");
const edad = parseInt(prompt("Ingrese la edad de la persona: "));

// Instancia de la clase Persona
const persona1 = new Persona(nombre, edad);

// Mostrar el objeto persona1
console.log(persona1); // Mostrar el objeto persona1

// Llamar al método saludar y mostrar el resultado
console.log(persona1.saludar()); // "Hola, me llamo Juan y tengo 30 años."
