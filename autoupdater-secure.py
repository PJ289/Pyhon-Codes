version = "1.0.0" # La versión debe estar siempre en la primera línea

# Sistema de actualización automática de un programa
# Requieres de tener un servidor web
# Developed by PJ289

# ======== Sistema de actualización automatica ======== #
cambios = """Cambios: 
- ¡Añade aquí los cambios de tu actualizaciones!
- Estos cambios aparecerán al actualizarse el programa.'"""

import requests
import base64

url_ultima_version = "https://tu-servidor-web.com/tu-programa.py" # Reemplaza con la dirección web a tu archivo
nombre_archivo = "tu-programa.py" # Reemplaza con el nombre de tu programa con la extensión .py
usuario = "usuario"  # Reemplaza con el nombre de usuario
contrasena = "contraseña"  # Reemplaza con la contraseña

# Codificar en Base64 el usuario y contraseña para usar en la autenticación
credenciales = base64.b64encode(f"{usuario}:{contrasena}".encode()).decode()
headers = {"Authorization": f"Basic {credenciales}"}

# Obtener el contenido del archivo del servidor
print("Comprobando actualizaciones...")
try:
    response = requests.get(url_ultima_version, headers=headers)
    response.raise_for_status()  # Lanza una excepción para errores HTTP
    contenido_archivo_servidor = response.text.strip()

    # Extraer el contenido de la variable de versión del archivo del servidor
    lineas_archivo_servidor = contenido_archivo_servidor.split("\n")
    primera_linea_servidor = lineas_archivo_servidor[0].strip()
    contenido_version_servidor = primera_linea_servidor.split("=")[-1].strip()

    # Leer el contenido de la versión actual
    with open(nombre_archivo, "r", encoding="utf-8") as archivo_actual:
        primera_linea_local = archivo_actual.readline().strip()

    # Extraer el contenido de la variable de versión de la primera línea local
    contenido_version_local = primera_linea_local.split("=")[-1].strip()

    # Comparar el contenido de las versiones
    if contenido_version_servidor != contenido_version_local:
        # Descargar la última versión del archivo Python  (siempre considera la última la verisón del servidor)
        response = requests.get(url_ultima_version)
        with open(nombre_archivo, "wb") as archivo:
            archivo.write(response.content)
        print("\033[46mDescarga de la última versión completada.\033[0m")
        print()
        print(cambios)
        print()

        # Reiniciar la aplicación
        import subprocess
        print("\033[43mReiniciando...\033[0m")
        subprocess.call(["python", "tu-programa.py"]) # Reemplaza con el nombre de tu programa con la extensión .py para que se reinice al actualizarse

        #Finaliza el programa para evitar que se ejecute el codigo de abajo y se repita el programa dos veces innecesariamente
        import sys
        sys.exit()


    else:
        print("\033[46m¡Tienes la última versión!\033[0m")
except requests.exceptions.ConnectionError:

    print("\033[41mError al conectar con el servidor. Comprueba tu conexión o inténtalo más tarde.\033[0m")

except Exception as e:
    print("\033[1,41mOcurrió un error:\033[0m","\033[31m", str(e),"\033[0m")