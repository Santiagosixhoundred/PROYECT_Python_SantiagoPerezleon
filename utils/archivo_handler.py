import json
import os
def cargar_datos(ruta_archivo):

    try:
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
                return datos if isinstance(datos, list) else []
        else:
            return []
    except (json.JSONDecodeError, FileNotFoundError, Exception) as e:
        print(f"Error al cargar datos: {e}")
        return []

def guardar_datos(datos, ruta_archivo):

    try:
        directorio = os.path.dirname(ruta_archivo)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)
        
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al guardar datos: {e}")
        return False

def verificar_archivo_existe(ruta_archivo):
    return os.path.exists(ruta_archivo)