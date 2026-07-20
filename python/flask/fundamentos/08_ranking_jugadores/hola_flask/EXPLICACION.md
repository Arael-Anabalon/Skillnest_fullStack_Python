# Ranking de Jugadores (Flask App)

Aplicación web simple en Flask para gestionar y visualizar un ranking de usuarios.

## Importancia para el Aprendizaje

Este proyecto sirvió para dominar conceptos clave de desarrollo web:
* **Rutas dinámicas:** Captura de parámetros numéricos y de texto directamente desde la URL.
* **Manejo de errores:** Diagnóstico de errores 404 por rutas no declaradas.
* **Inyección de datos:** Envío de variables desde Python hacia plantillas HTML.
* **Estructura Flask:** Uso obligatorio de la carpeta `templates` sin depender de nombres fijos como `index.html`.

## Explicación de Rutas

### Ruta Raíz (`/`)
* **Función:** Es la página de inicio que carga al entrar a la IP del servidor.
* **Acción:** Muestra el ranking completo con los 5 jugadores por defecto.

### Ruta con Número (`/ranking/<int:cantidad>`)
* **Función:** Filtra la lista de posiciones dinámicamente según el número indicado en la URL.
* **Acción:** Si el número está entre 1 y 5, muestra solo esa cantidad de jugadores usando la variable `loop.index` para enumerar las posiciones automáticamente. Si está fuera de rango, activa un error 404.

### Ruta con Color (`/ranking/<int:cantidad>/<color>`)
* **Función:** Recibe un parámetro de texto dinámico al final de la URL para personalizar la interfaz.
* **Acción:** Captura la palabra escrita (por ejemplo, `blue` o `red`) y la inyecta en la plantilla HTML para cambiar dinámicamente el color de fondo de la página.
