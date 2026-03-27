// 1. Seleccionar todos los botones de compra de DOM
const botonesCompra = document.querySelectorAll('article button');

// 2. Definir la lógica del evento
function agregarAlCarrito(evento) {
    //evento.target identifica el elemento exacto que recibió el clic
    const botonPresionado = evento.target;
    
    // Subir un nivel en el DOM para capturar la tarjeta (article) completa
    const tarjetaServicio = botonPresionado.parentElement;

    // Extraer el texto del título (h4) dentro de esa tarjeta específica
    const nombreServicio = tarjetaServicio.querySelector('h4').innerText;

    // Alerta visual para el usuario (Front-End)
    alert(`Servicio Soc añadido al carrito de compra: \n${nombreServicio}`);

    // Registro técnico para depuración (Consola del navegador)
    console.log(`[LOG SEGURIDAD]: Intento de compra registrado para ->${nombreServicio}`);
}

// 3. Asignar el 'escuchador de eventos' (Event Listener) a cada botón
botonesCompra.forEach(boton => {
    boton.addEventListener('click', agregarAlCarrito);
});