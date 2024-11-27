# Alcaldia-mapas

Instalación y Configuración
Prerrequisitos

Asegúrate de tener instalados los siguientes programas en tu sistema:

    Python 3.6+
    pip
    Node.js y npm
    Git

Pasos de Instalación

    Clonar el repositorio:

    git clone https://github.com/alexjut/Alcaldia-mapas.git
    cd Alcaldia-mapas

    Crear y activar un entorno virtual:

    python3 -m venv myenv
    source myenv/bin/activate

    Instalar las dependencias de Python:

    pip install Flask requests

    Instalar sass para compilar SCSS a CSS:

    sudo npm install -g sass

    Compilar el archivo SCSS a CSS:

    sass static/css/styles.scss static/css/styles.css

Configuración

    Configurar la clave API:
        Reemplaza 'your_api_key' en app.py con tu clave API proporcionada por IDECA.

    Configurar los iconos personalizados:
        Reemplaza 'https://example.com/path/to/icon.png' en index.html con la URL de tu icono personalizado.

Ejecución

    Ejecutar la aplicación Flask:

    python app.py

    Abrir en el navegador:
        Ve a http://127.0.0.1:5000/ en tu navegador para ver la aplicación en funcionamiento.

Funcionalidades

    Geocodificación Directa: Convierte una dirección en coordenadas geográficas.
    Geocodificación Inversa: Convierte coordenadas geográficas en una dirección.
    Cálculo de Rutas: Calcula rutas entre dos puntos utilizando diferentes medios de transporte.
    Búsqueda por CHIP: Busca información utilizando el código CHIP.
    Búsqueda de Lugares: Busca lugares por palabra clave o ubicación.
