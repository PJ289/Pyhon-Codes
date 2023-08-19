# Programa de encriptación y desencriptación de archivos mediante AES-256

# Requiere instalar pyAesCrypt (pip install pyAesCrypt)

# Developed by PJ289

import getpass
import pyAesCrypt

opcion = ""

while opcion.lower() != "salir" or opcion.lower() != "s":
    opcion = input("¿Que desea hacer? (Encriptar / Desencriptar / Salir): ")

    # Encriptación
    if opcion.lower() == "encriptar" or opcion.lower() == "e":
        entrada = input("Nombre del archivo a encriptar (incluye extensión): ")
        contrasena = getpass.getpass("Contraseña para el archivo cifrado (usa una larga y segura): ")

        # Pregunta si se desea mantener el mismo nombre del archivo original
        mantener_nombre = input("¿Desea mantener el mismo nombre de archivo? (si/no): ")
        if mantener_nombre.lower() == "no" or mantener_nombre.lower() == "n":
            nombre_salida = input("Ingrese el nuevo nombre de archivo (sin extensión): ")
        else:
            nombre_salida = entrada.rsplit(".", 1)[0]  # Obtiene el nombre sin la extensión
            print("Usando nombre original...")

        # Pregunta si se desea mantener la misma extensión del archivo original
        mantener_extension = input("¿Desea mantener la misma extensión de archivo? (si/no): ")
        if mantener_extension.lower() == "no" or mantener_extension.lower() == "n":
            extension = input("Ingrese la nueva extensión de archivo (sin punto) o deje en blanco para usar la misma del archivo de origen: ")
            if extension:
                extension = "." + extension
        else:
            extension = "." + entrada.rsplit(".", 1)[-1]  # Obtiene la extensión completa

        salida = nombre_salida + extension
        print("Encriptación en curso...")
        try:
            pyAesCrypt.encryptFile(entrada, salida + ".aes", contrasena)
            print("¡Archivo encriptado! ","("+entrada+".aes)")
        except Exception as e:
            print("Ocurrió un error al encriptar el archivo:", e)

    # Desencriptación
    elif opcion.lower() == "desencriptar" or opcion.lower() == "d":
        entrada = input("Nombre del archivo a desencriptar (incluye extensión): ")
        contrasena = getpass.getpass("Contraseña del archivo cifrado: ")
        if entrada.endswith(".aes"):
            salida = entrada[:-4]  # Quita los últimos 4 caracteres (".aes")
            try:
                pyAesCrypt.decryptFile(entrada,salida,contrasena)
                print("¡Archivo desencriptado! ","("+salida+")")
            except Exception as e:
                print("Ocurrió un error al desencriptar el archivo:", e)
        else:
            print("El archivo seleccionado no tiene extensión .aes, ¿seguro que está encriptado?")
            respuesta = input("¿Desea continuar? (si/no): ")
            if respuesta.lower() == "si" or respuesta == "s":
                salida = entrada
                print("Desencriptación en curso...")
                try:
                    pyAesCrypt.decryptFile(entrada,salida,contrasena)
                    print("¡Archivo desencriptado! ","("+salida+")")
                except Exception as e:
                    print("Ocurrió un error al desencriptar el archivo:", e)
            else:
                print("Omitiendo...")

