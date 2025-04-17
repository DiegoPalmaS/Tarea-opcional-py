/*3. Clase CuentaBancaria con métodos de depósito y retiro
Objetivo: Simular un comportamiento realista.
 Instrucciones:
 Crea una clase CuentaBancaria con:

titular (string)
saldo (number, inicia en 0)

 Agrega métodos:

depositar(cantidad)
retirar(cantidad) //(solo si hay saldo suficiente)
verSaldo()

Simula algunas transacciones.
*/
const prompt = require("prompt-sync")() // Importar prompt-sync

class CuentaBancaria {
    // Constructor de la clase CuentaBancaria
    constructor(titular) {
        this.titular = titular;
        this.saldo = 0; // Inicializa el saldo en 0
    }

    // Método para depositar dinero
    depositar(cantidad) {
        if (cantidad > 0) {
            this.saldo += cantidad; // Aumenta el saldo
            console.log(`Se han depositado $${cantidad}. Nuevo saldo: $${this.saldo}`);
            console.log("----------------------------"); // Separador
        } else {
            console.log("La cantidad a depositar debe ser mayor que 0.");
            console.log("----------------------------"); // Separador
        }
    }

    // Método para retirar dinero
    retirar(cantidad) {
        if (cantidad > 0 && cantidad <= this.saldo) {
            this.saldo -= cantidad; // Disminuye el saldo
            console.log(`Se han retirado $${cantidad}. Nuevo saldo: $${this.saldo}`);
            console.log("----------------------------"); // Separador
        } else if (cantidad > this.saldo) {
            console.log("No hay suficiente saldo para realizar el retiro.");
            console.log("----------------------------"); // Separador
        } else {
            console.log("ingrese un valor válido.");
            console.log("----------------------------"); // Separador
        }
    }

    // Método para ver el saldo actual
    verSaldo() {
        console.log(`${this.titular} tu saldo actual es: $${this.saldo}`);
        console.log("----------------------------"); // Separador
    }
}

// Solicitar el nombre del titular de la cuenta
const titular = prompt("Ingrese el nombre del titular de la cuenta: ");
// Instancia de la clase CuentaBancaria
const cuenta = new CuentaBancaria(titular);



// Bucle para realizar transacciones
let opcion; // Variable para almacenar la opción del usuario
//Siempre que la opción no sea 4, se mostrará el menú de opciones
while (opcion !== 4) {
    //Mostrar el menú de opciones
    console.log("Opciones:");
    console.log("1. Depositar dinero");
    console.log("2. Retirar dinero");
    console.log("3. Ver saldo");
    console.log("4. Salir");
    opcion = parseInt(prompt("Seleccione una opción (1-4): "));//Guardar la opción elegida por el usuario
    console.log("----------------------------"); // Separador
    //Acciones según la opción elegida por el usuario
    switch (opcion) {
        case 1:
            // Solicitar la cantidad a depositar
            const cantidadDeposito = parseFloat(prompt("Ingrese la cantidad a depositar: "));
            cuenta.depositar(cantidadDeposito); // Llama al método depositar
            break;
        case 2:
            // Solicitar la cantidad a retirar
            const cantidadRetiro = parseFloat(prompt("Ingrese la cantidad a retirar: "));
            cuenta.retirar(cantidadRetiro); // Llama al método retirar
            break;
        case 3:
            // Mostrar el saldo actual
            cuenta.verSaldo(); // Llama al método verSaldo
            break;
        case 4:
            console.log("Saliendo del programa...");
            break;
        default:
            console.error("Opción no válida. Intente de nuevo.");
            console.log("----------------------------"); // Separador
    }
}