/* 2. Clase Rectángulo con área y perímetro
Objetivo: Usar métodos para realizar cálculos.
 Instrucciones:
 Crea una clase Rectangulo que reciba ancho y alto como parámetros.
 Agrega los métodos:

calcularArea(): retorna el área.
calcularPerimetro(): retorna el perímetro. 
*/
const prompt = require('prompt-sync')(); // Importar prompt-sync

class Rectangulo {
    // Constructor de la clase Rectangulo
    constructor(ancho, alto) {
        this.ancho = ancho;
        this.alto = alto;
    }

    // Método para calcular el área
    calcularArea() {
        // Área = ancho * alto
        const area = this.ancho * this.alto;
        return area;
    }

    // Método para calcular el perímetro
    calcularPerimetro() {
        // Perímetro = 2 * (ancho + alto)
        const perimetro = 2*(this.ancho + this.alto);
        return perimetro;
    }
}

// Solicitar ancho y alto al usuario
const ancho = parseFloat(prompt("Ingrese el ancho del rectángulo: "));
const alto = parseFloat(prompt("Ingrese el alto del rectángulo: "));
// Instancia de la clase Rectangulo
const rectangulo1 = new Rectangulo(ancho, alto);
console.log(rectangulo1); // Mostrar el objeto rectangulo1
console.log("Área: ", rectangulo1.calcularArea().toFixed(1)); // Mostrar el área
console.log("Perímetro: ", rectangulo1.calcularPerimetro().toFixed(1)); // Mostrar el perímetro));