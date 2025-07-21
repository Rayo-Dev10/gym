# Horario Gimnasio

Este repositorio contiene el horario del gimnasio del IES CINOC para el grupo B-2025. La información del horario se mantiene en un archivo JSON separado y se utiliza un pequeño script para generar la página web.

- **index.html**: página resultante con la tabla del horario.
- **index.template.html**: plantilla utilizada para construir la página.
- **styles.css**: hoja de estilos utilizada por la página.
- **data.json**: datos del horario en formato JSON.
- **render.py**: script que combina la plantilla con los datos para crear `index.html`.

Para actualizar el horario modifica `data.json` y ejecuta:

```bash
python3 render.py
```

El script leerá el JSON y generará un `index.html` listo para ser servido.
