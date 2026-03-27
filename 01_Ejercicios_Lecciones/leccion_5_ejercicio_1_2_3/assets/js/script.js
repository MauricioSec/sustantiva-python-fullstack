// Capturamos el botón del DOM mediante su ID
const botonArriba = document.getElementById('btnArriba');

// Validamos que el elemento exista en la página para evitar errores de ejecución
if (botonArriba !== null) {
    // Agregamos un 'escuchador' de eventos para el clic
    botonArriba.addEventListener('click', function() {
        // Ejercicio 2: Ejecutamos el método scrollTo del objeto window
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
} else {
    // Depuración en consola en caso de fallo estructural
    console.log("Error de DOM: No se encontró el botón con ID 'btnArriba'.");
}