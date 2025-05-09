from PIL import Image
import os
import shutil  # Para mover archivos
import tifffile  # Nueva librería para manejar TIFF
from PIL import ImageFile

# Habilitar que PIL maneje más formatos
ImageFile.LOAD_TRUNCATED_IMAGES = True

# Directorios
input_folder = "/mnt/d/Documentos/Drive/imagenes_originales"  # Carpeta de imágenes originales
output_folder = "imagenes_convertidas"  # Carpeta donde se guardarán las imágenes convertidas
error_folder = "imagenes_erroneas"  # Carpeta para imágenes que no se pudieron convertir
new_format = "webp"  # Formato de salida

# Crear las carpetas de salida si no existen
for folder in [output_folder, error_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Extensiones de imagen permitidas
valid_extensions = (".jpg", ".jpeg", ".png", ".tiff", ".tif", ".bmp")

# Función para intentar abrir la imagen de manera más flexible
def try_open_image(file_path):
    try:
        with Image.open(file_path) as img:
            img.verify()  # Verificar si el archivo es una imagen válida
        return True
    except (IOError, SyntaxError):
        return False

# Procesar imágenes
for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)

    # Verificar que sea un archivo de imagen válido
    if filename.lower().endswith(valid_extensions):
        try:
            # Verificar que la imagen se puede abrir correctamente
            if try_open_image(input_path):
                with Image.open(input_path) as img:
                    # Si es un archivo TIFF y no se puede abrir con PIL, usar tifffile
                    if filename.lower().endswith(('.tiff', '.tif')):
                        try:
                            with tifffile.TiffFile(input_path) as tif:
                                img = Image.fromarray(tif.asarray())
                        except Exception as e:
                            print(f"❌ No se pudo abrir la imagen TIFF {filename}: {e}")
                            shutil.move(input_path, os.path.join(error_folder, filename))  # Mover a la carpeta de errores
                            continue

                    # Obtener nombre base sin extensión
                    base_name = os.path.splitext(filename)[0]
                    output_path = os.path.join(output_folder, f"{base_name}.{new_format}")

                    # Convertir y guardar en formato WebP
                    img.convert("RGB").save(output_path, new_format.upper(), quality=80)
                    print(f"✅ {filename} convertido a {output_path}")
            else:
                print(f"❌ No se pudo abrir {filename}: El archivo podría estar dañado o tener un formato no compatible.")
                shutil.move(input_path, os.path.join(error_folder, filename))  # Mover a la carpeta de errores
        except Exception as e:
            print(f"❌ No se pudo convertir {filename}: {e}")
            shutil.move(input_path, os.path.join(error_folder, filename))  # Mover a la carpeta de errores

print("✨ Conversión completada.")