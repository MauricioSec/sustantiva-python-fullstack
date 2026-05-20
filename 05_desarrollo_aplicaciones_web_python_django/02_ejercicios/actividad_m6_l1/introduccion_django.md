# Actividad N° 1 - Introducción a Django y su Ecosistema

## 1. ¿Qué es Django?

**¿Qué tipo de framework es Django?**
Django es un framework web de alto nivel, de código abierto y escrito íntegramente en Python. Sigue un patrón de diseño arquitectónico conocido como MTV (Model-Template-View) y está orientado a facilitar el desarrollo rápido mediante el principio de "baterías incluidas", proveyendo herramientas listas para usar en lugar de requerir que el desarrollador ensamble todo desde cero.

**¿Qué tipo de aplicaciones permite construir?**
Está diseñado para construir aplicaciones web complejas, robustas, escalables y altamente dependientes de bases de datos. Es ideal para gestores de contenido (CMS), redes sociales, plataformas de comercio electrónico, sistemas de gestión interna, aplicaciones científicas y APIs RESTful.

**Ventajas de usar Django sobre trabajar con Python puro:**
1. **Infraestructura integrada:** Provee un ORM (Mapeador Objeto-Relacional), un sistema de enrutamiento, autenticación de usuarios y un panel de administración nativo, evitando programar utilidades repetitivas desde cero.
2. **Seguridad robusta por defecto:** Implementa protecciones automáticas contra vulnerabilidades comunes como inyección SQL, Cross-Site Scripting (XSS), Clickjacking y falsificación de peticiones en sitios cruzados (CSRF).
3. **Manejo eficiente del protocolo HTTP:** Abstrae la complejidad de analizar peticiones y construir respuestas HTTP seguras y estructuradas, lo cual en Python puro requeriría manejar sockets o la interfaz WSGI manualmente.

## 2. Entornos virtuales en Python

**¿Qué es un entorno virtual en Python y para qué sirve?**
Es un árbol de directorios aislado y autocontenido donde se instala un intérprete de Python y un conjunto de librerías y scripts específicos. Sirve para encapsular las dependencias de un proyecto, garantizando que este no interfiera con las librerías globales del sistema operativo ni con otros proyectos de Python en la misma máquina.

**Ventajas de crear un entorno virtual para un proyecto Django:**
- Permite usar versiones específicas de Django (por ejemplo, Django 4.2 en un proyecto y Django 5.0 en otro) sin que existan conflictos de versiones.
- Mantiene limpio el sistema operativo.
- Facilita la replicación del entorno en producción o para otros desarrolladores mediante un archivo `requirements.txt`.

**Explicación del comando:**
*(Nota técnica: El comando correcto es `python -m venv env`, asumiendo un error tipográfico en el documento original que dice `veny`).*
El comando ejecuta a Python e invoca (`-m`) el módulo integrado llamado `venv` (virtual environment) para que ejecute su función principal: crear un nuevo entorno virtual. El segundo término `env` es simplemente el nombre que el usuario decide darle a la carpeta que se creará para alojar dicho entorno.

## 3. Estructura y diseño de Django

**¿Qué es el patrón MVC y cómo se aplica en Django (MTV)?**
MVC (Model-View-Controller) es un patrón de arquitectura de software que separa los datos de una aplicación, la interfaz de usuario y la lógica de control en tres componentes distintos. Django utiliza una variante estricta de este patrón llamada MTV (Model-Template-View). En Django, el controlador está implícito en el propio framework (el enrutador y el sistema central), mientras que la lógica de negocio que típicamente iría en el Controlador de MVC se programa en la Vista (View) de MTV, y la presentación visual se delega al Template.

**Tabla comparativa:**

| Concepto tradicional (MVC) | Nombre en Django (MTV) | Función principal |
| :--- | :--- | :--- |
| **Model** | Model (`models.py`) | Define la estructura de los datos, reglas de validación y la comunicación con la base de datos (mediante el ORM). |
| **View** | Template (`.html`) | Define la presentación visual y la interfaz de usuario. Estructura cómo se muestran los datos en el navegador usando HTML y etiquetas dinámicas. |
| **Controller** | View (`views.py`) | Contiene la lógica de negocio. Recibe la petición HTTP, consulta el Modelo, pasa los datos al Template y retorna una respuesta HTTP. |

**¿Qué es el enrutador de Django y qué papel cumple?**
El enrutador (configurado en `urls.py`) es el mecanismo de despacho inicial de Django. Su papel es analizar la dirección URL solicitada por el usuario (ej. `/productos/2/`), buscar una coincidencia exacta en sus patrones de rutas definidos y direccionar esa solicitud a la Vista (View) específica encargada de procesar dicha petición.

## 4. Principios del desarrollo con Django

**Principio DRY ("Don't Repeat Yourself") y su aplicación:**
DRY dicta que cada pieza de lógica o conocimiento debe tener una única representación autoritativa y sin ambigüedades dentro del sistema. Si se modifica algo, debe hacerse en un solo lugar. Django lo aplica mediante:
- **Herencia de plantillas (Templates):** Permite crear un archivo base con el diseño principal (header, footer) que otras páginas pueden extender, evitando copiar HTML.
- **ORM:** Evita escribir consultas SQL repetitivas.
- **Abstracción de vistas:** Mediante vistas genéricas basadas en clases (CBVs) para operaciones CRUD comunes.

**Estructura flexible y minimalista (Bajo acoplamiento):**
Aunque Django incluye muchas herramientas nativas, está diseñado bajo el principio de "bajo acoplamiento". Esto significa que sus capas (Modelos, Vistas, Templates) son independientes. Puedes cambiar el motor de bases de datos o usar un sistema de plantillas distinto sin reescribir toda la aplicación. Además, fomenta dividir un proyecto grande en múltiples aplicaciones ("apps") pequeñas, modulares y reutilizables.

**Templates en Django y su rol en la renderización:**
Los Templates son archivos de texto (comúnmente HTML) que separan el diseño de la aplicación de su código Python. Su rol es recibir un contexto (variables y datos enviados por la Vista) e inyectar esos datos dinámicos dentro de la estructura estática del documento utilizando el Lenguaje de Plantillas de Django (DTL). Esto permite compilar un documento final renderizado antes de enviarlo como respuesta al navegador del usuario.