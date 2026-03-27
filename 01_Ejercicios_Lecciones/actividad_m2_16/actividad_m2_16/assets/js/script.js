// Aseguramos que el DOM esté completamente cargado antes de ejecutar los scripts
$(document).ready(function() {

    /* =========================================
       FASE 2: Manipulación del DOM
       ========================================= */
    
    // 1. Cambiar el color de texto de los elementos de la lista
    // Seleccionamos todos los 'li' dentro de '#lista-nodos' y modificamos su CSS
    $('#lista-nodos li').css({
        'color': '#004085', 
        'font-weight': 'bold'
    });

    // 2. Agregar dinámicamente un cuarto elemento
    // Usamos .append() para inyectar HTML al final de la lista
    $('#lista-nodos').append('<li class="list-group-item text-success">Sistema de Detección de Intrusos - IDS (192.168.1.50) [Añadido dinámicamente]</li>');


    /* =========================================
       FASE 3: Eventos en jQuery
       ========================================= */
    
    // Capturamos el evento click del botón
    $('#btn-toggle').click(function() {
        
        // .slideToggle() alterna entre ocultar y mostrar con una animación
        $('#lista-nodos').slideToggle('fast', function() {
            
            // Esta función interna (callback) se ejecuta cuando termina la animación.
            // Verificamos si la lista quedó oculta usando el seudoselector :hidden
            if ($('#lista-nodos').is(':hidden')) {
                // Si está oculta, cambiamos el texto y el color del botón
                $('#btn-toggle').text('Mostrar lista');
                $('#btn-toggle').removeClass('btn-danger').addClass('btn-success');
            } else {
                // Si está visible, restauramos el texto y el color original
                $('#btn-toggle').text('Ocultar lista');
                $('#btn-toggle').removeClass('btn-success').addClass('btn-danger');
            }
        });
    });


    /* =========================================
       FASE 4: Uso de Plugins
       ========================================= */
    
    // El Tooltip de Bootstrap es un plugin que no viene activado por defecto.
    // Requiere esta línea exacta de jQuery para buscar los elementos con 'data-toggle="tooltip"' y activarlos.
    $('[data-toggle="tooltip"]').tooltip();

});