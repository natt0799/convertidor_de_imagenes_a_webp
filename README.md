# 🖼️ Proyecto: Convertidor de Imágenes a WebP

Este proyecto fue desarrollado como una herramienta de automatización en Python para convertir imágenes de distintos formatos a `.webp`, un formato moderno, ligero y eficiente para la web. También incorpora manejo de errores y clasificación automática de imágenes no válidas o dañadas.

---

## 💡 Propósito del proyecto

El objetivo fue crear una utilidad que:

- Automatice la conversión de formatos comunes de imagen.
- Detecte errores en imágenes corruptas o no soportadas.
- Organice automáticamente los resultados (convertidas vs. fallidas).
- Mejore la comprensión del manejo de archivos, procesamiento de imágenes y control de errores con Python.

---

## ⚙️ Funcionalidades principales

✅ Soporte para múltiples formatos de entrada: `.jpg`, `.png`, `.tiff`, `.bmp`, etc.  
✅ Salida optimizada en formato `.webp`  
✅ Manejo especial para archivos `.tiff` con librería externa (`tifffile`)  
✅ Clasificación automática de errores en carpetas separadas  
✅ Verificación de imágenes antes de procesarlas  
✅ Creación automática de carpetas necesarias

---

## 🧰 Herramientas y tecnologías utilizadas

- Python 3.x
- Librerías:
  - `Pillow` (PIL) – para manipulación de imágenes
  - `tifffile` – para soporte mejorado de archivos TIFF
- Visual Studio Code
- Entorno Linux WSL (Ubuntu 24.04)

---

## 🗂 Estructura del proyecto

convertidor_imagenes/
├── convertir_imagenes_1.py # Script principal
├── imagenes_convertidas/ # Imágenes procesadas correctamente
├── imagenes_erroneas/ # Imágenes que fallaron en el procesamiento
├── requirements.txt # Librerías necesarias
├── .gitignore # Exclusión de archivos/carpetas
└── README.md # Documentación del proyecto

📈 Aprendizajes clave
✔ Buenas prácticas en manejo de errores con try/except
✔ Uso de condiciones para validar tipos de archivo
✔ Implementación de control de calidad antes de guardar archivos
✔ Manipulación de archivos y carpetas desde código
✔ Uso de librerías externas para formatos específicos

🔐 Licencia
Este proyecto se distribuye bajo la licencia MIT.

🙋 Sobre mí
Me apasiona automatizar tareas con Python y desarrollar soluciones útiles. Este proyecto es parte de mi portafolio como desarrollador backend, donde aplico herramientas de procesamiento y manejo de datos para resolver problemas reales.

📫 Puedes ver más proyectos en mi perfil de GitHub (https://github.com/natt0799)
