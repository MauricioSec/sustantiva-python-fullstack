// 1. Estructura de Datos (Arreglo de Objetos)
const servicios = [
    { id: 1, titulo: "Análisis de Vulnerabilidades (OWASP)", descripcion: "Escaneo automatizado y reporte detallado de fallos de seguridad en aplicaciones web.", precio: 150000, imagen: "assets/img/1-vulnerabilidades.jpg" },
    { id: 2, titulo: "Pentesting de Infraestructura", descripcion: "Prueba de intrusión manual para detectar brechas críticas en redes corporativas.", precio: 350000, imagen: "assets/img/2-pentesting-infraestructura.jpg" },
    { id: 3, titulo: "Pasarela Webpay Segura", descripcion: "Integración de pagos con Transbank bajo estrictos estándares de seguridad y validación backend.", precio: 200000, imagen: "assets/img/3-pasarela-webpay.jpg" },
    { id: 4, titulo: "Auditoría de Cumplimiento", descripcion: "Evaluación de normativas ISO 27001 y Ley de Protección de Datos Personales.", precio: 280000, imagen: "assets/img/4-auditoria-normativa.jpg" },
    { id: 5, titulo: "Respuesta ante Incidentes", descripcion: "Análisis forense digital, contención de brechas y recuperación de sistemas comprometidos.", precio: 450000, imagen: "assets/img/5-respuesta-incidentes.jpg" },
    { id: 6, titulo: "Monitoreo SOC 24/7", descripcion: "Vigilancia continua de la red, detección de anomalías y alertas en tiempo real.", precio: 600000, imagen: "assets/img/6-monitoreo.soc.jpg" }
];

// 2. Variables de Estado
let cantidadEnCarrito = 0;

// 3. Controlador de Arranque (Enrutador Básico)
document.addEventListener('DOMContentLoaded', () => {
    const contenedorCatalogo = document.getElementById('contenedor-servicios');
    const contenedorDetalle = document.getElementById('detalle-servicio');

    // Si existe el contenedor del catálogo, estamos en index.html
    if (contenedorCatalogo) {
        renderizarServicios(contenedorCatalogo);
    } 
    // Si existe el contenedor de detalle, estamos en detalle.html
    else if (contenedorDetalle) {
        renderizarVistaDetalle(contenedorDetalle);
    }
});

// 4. Función para Renderizar el Catálogo (index.html)
function renderizarServicios(contenedor) {
    contenedor.innerHTML = '';
    servicios.forEach(servicio => {
        const precioFormateado = servicio.precio.toLocaleString('es-CL');
        const tarjetaHTML = `
            <div class="col-md-6 col-lg-4">
                <article class="card h-100 bg-secondary text-light border-dark shadow-sm">
                    <img src="${servicio.imagen}" class="card-img-top" alt="Ilustración de ${servicio.titulo}" style="object-fit: cover; height: 200px;">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title text-success">${servicio.titulo}</h5>
                        <p class="card-text text-light opacity-75">${servicio.descripcion}</p>
                        <h6 class="mt-auto mb-3">Valor: $${precioFormateado} CLP</h6>
                        <div class="d-grid gap-2">
                            <a href="detalle.html?id=${servicio.id}" class="btn btn-outline-light btn-sm">Ver detalles</a>
                            <button class="btn btn-success btn-sm btn-agregar" data-id="${servicio.id}">
                                <i class="bi bi-cart-plus"></i> Añadir al Carrito
                            </button>
                        </div>
                    </div>
                </article>
            </div>
        `;
        contenedor.innerHTML += tarjetaHTML;
    });
    asignarEventosBotones();
}

// 5. Función para Renderizar la Vista Individual (detalle.html)
function renderizarVistaDetalle(contenedor) {
    // Extraer el ID de la URL
    const parametrosURL = new URLSearchParams(window.location.search);
    const idCapturado = parseInt(parametrosURL.get('id'));

    // Buscar el servicio en el arreglo
    const servicio = servicios.find(s => s.id === idCapturado);

    // Manejo de error si el ID no existe
    if (!servicio) {
        contenedor.innerHTML = `
            <div class="alert alert-danger text-center mt-5">
                <h4>Error de sistema</h4>
                <p>El servicio solicitado no existe o fue removido.</p>
                <a href="index.html" class="btn btn-dark mt-3">Volver al inicio</a>
            </div>`;
        return;
    }

    const precioFormateado = servicio.precio.toLocaleString('es-CL');

    // Construcción del HTML para la vista de detalle
    contenedor.innerHTML = `
        <div class="row align-items-center bg-secondary p-4 rounded shadow-sm border border-dark">
            <div class="col-md-6 mb-4 mb-md-0">
                <img src="${servicio.imagen}" class="img-fluid rounded border border-success" alt="${servicio.titulo}">
            </div>
            <div class="col-md-6">
                <h2 class="text-success mb-3">${servicio.titulo}</h2>
                <h4 class="mb-4">Valor de inversión: $${precioFormateado} CLP</h4>
                <p class="lead mb-4">${servicio.descripcion}</p>
                
                <div class="d-grid gap-3">
                    <button class="btn btn-success btn-lg btn-agregar" data-id="${servicio.id}">
                        <i class="bi bi-cart-plus"></i> Procesar Contratación
                    </button>
                </div>
                
                <hr class="border-secondary my-4">
                <p class="text-muted small"><i class="bi bi-shield-check text-success"></i> Todos los servicios incluyen NDA (Acuerdo de Confidencialidad) por defecto.</p>
            </div>
        </div>
    `;
    asignarEventosBotones();
}

// 6. Función para manejar el evento del Carrito (Compartida)
function asignarEventosBotones() {
    const botonesAgregar = document.querySelectorAll('.btn-agregar');
    const badgeContador = document.getElementById('contador-carrito');
    
    botonesAgregar.forEach(boton => {
        boton.addEventListener('click', (evento) => {
            cantidadEnCarrito++;
            if(badgeContador) badgeContador.innerText = cantidadEnCarrito;
            
            const btn = evento.currentTarget;
            const textoOriginal = btn.innerHTML;
            btn.innerHTML = '<i class="bi bi-check-lg"></i> ¡Procesado!';
            btn.classList.replace('btn-success', 'btn-primary');
            
            setTimeout(() => {
                btn.innerHTML = textoOriginal;
                btn.classList.replace('btn-primary', 'btn-success');
            }, 1000);
        });
    });
}