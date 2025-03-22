## Parte 1
# Proyecto: Interacción con JavaScript y Express

Este proyecto es un ejercicio básico que muestra el uso de JavaScript en una página web con una caja de texto, una ventana emergente y un botón para cambiar colores.

## Funcionalidad

- Al presionar `Enter` después de escribir en el input, se muestra un modal con el texto ingresado.
- Dentro del modal hay un botón que cambia el color del input de forma alternada:
  - Fondo blanco / texto negro
  - Fondo negro / texto blanco
  - Fondo celeste / texto rojo

## Requisitos

- Tener instalado [Node.js](https://nodejs.org/)

## Instalación

1. Cloná este repositorio.
2. Abrí una terminal en la carpeta del proyecto.
3. Instalá la dependencia:
   ```bash
   npm install
   ```

## Cómo ejecutar el proyecto

1. En la terminal, posicionado en la carpeta /servidor_express, ejecutá:
   ```bash
   node server.js
   ```

2. Abrí tu navegador y visitá:
   ```
   http://localhost:3000
   ```


## Tecnologías utilizadas

- HTML5
- CSS3
- JavaScript
- Node.js + Express

---

## Parte 2 
# Python + Flask

Esta segunda parte del proyecto implementa la misma funcionalidad, pero usando **Python con Flask** como servicio web.

## Funcionalidad

- Al presionar `Enter` después de escribir en el input, se muestra un modal con el texto ingresado.
- Dentro del modal hay un botón que cambia el color del input de forma alternada:
  - Fondo blanco / texto negro
  - Fondo negro / texto blanco
  - Fondo celeste / texto rojo

## Requisitos

- Tener instalado [Python](https://www.python.org/)
- Instalar Flask en un entorno virtual

## Instalación

1. Crear un entorno virtual (solo la primera vez):
   ```bash
   python -m venv .venv
   ```

2. Activar el entorno virtual:
     ```bash
     .venv\Scripts\activate
     ```

3. Instalar Flask:
   ```bash
   pip install flask
   ```

## Cómo ejecutar el proyecto

1. Asegurate de estar en la raíz del proyecto (donde está `app.py`).
2. Ejecutá el servidor Flask:
   ```bash
   python app.py
   ```

3. Abrí tu navegador y visitá:
   ```
   http://localhost:5000
   ```

---

## Autora

#### Ailin Ayelen Miño
#### Materia: Seminario de Actualización II
#### Instituto Politécnico Formosa
#### Carrera: Técnicatura Superior en Desarrollo de Software Multiplataforma