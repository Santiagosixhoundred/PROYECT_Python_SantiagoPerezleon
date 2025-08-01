import os
from models import libro, pelicula, musica
from utils import archivo_handler

class AdministradorColeccion:
    """Clase principal para administrar la colección de elementos"""
    
    def __init__(self, archivo_datos="data/coleccion.json"):
        self.archivo_datos = archivo_datos
        self.coleccion = [] 
        os.makedirs("data", exist_ok=True)
        
        self.cargar_datos()
        
    def cargar_datos(self):
        try:
            datos = archivo_handler.cargar_datos(self.archivo_datos)
            self.coleccion = datos if datos else []
            print(f"Datos cargados correctamente. {len(self.coleccion)} elementos en la colección.")
        except Exception as e:
            print(f"Error al cargar datos: {e}")
            self.coleccion = []
    
    def guardar_datos(self):
        try:
            return archivo_handler.guardar_datos(self.coleccion, self.archivo_datos)
        except Exception as e:
            print(f"Error al guardar datos: {e}")
            return False
    
    def agregar_elemento(self):
        print("\n=== AGREGAR ELEMENTO ===")
        print("1. Libro")
        print("2. Película") 
        print("3. Música")
        print("Elemento agregado con exito")
        
        try:
            tipo = input("Selecciona el tipo de elemento (1-3): ").strip()
            
            if tipo == "1":
                self._agregar_libro()
            elif tipo == "2":
                self._agregar_pelicula()
            elif tipo == "3":
                self._agregar_musica()
            else:
                print("Opción inválida")
        except Exception as e:
            print(f"Error al agregar elemento: {e}")
    
    def _agregar_libro(self):
        titulo = input("Título del libro: ").strip()
        autor = input("Autor: ").strip()
        genero = input("Género: ").strip()
        ano = input("Año de publicación: ").strip()
        paginas = input("Número de páginas: ").strip()
        
        try:
            nuevo_libro = {
                "tipo": "libro",
                "titulo": titulo,
                "autor": autor,
                "genero": genero,
                "ano": int(ano) if ano.isdigit() else 0,
                "paginas": int(paginas) if paginas.isdigit() else 0
            }
            
            self.coleccion.append(nuevo_libro)
            print("Libro agregado exitosamente!")
            
        except ValueError:
            print("Error: Año y páginas deben ser números")
        except Exception as e:
            print(f"Error al agregar libro: {e}")
    
    def _agregar_pelicula(self):
        titulo = input("Título de la película: ").strip()
        director = input("Director: ").strip()
        genero = input("Género: ").strip()
        ano = input("Año: ").strip()
        duracion = input("Duración (minutos): ").strip()
        
        try:
            nueva_pelicula = {
                "tipo": "pelicula",
                "titulo": titulo,
                "director": director,
                "genero": genero,
                "ano": int(ano) if ano.isdigit() else 0,
                "duracion": int(duracion) if duracion.isdigit() else 0
            }
            
            self.coleccion.append(nueva_pelicula)
            print("Película agregada exitosamente!")
            
        except ValueError:
            print("Error: Año y duración deben ser números")
        except Exception as e:
            print(f"Error al agregar película: {e}")
    
    def _agregar_musica(self):
        titulo = input("Título de la canción/álbum: ").strip()
        artista = input("Artista: ").strip()
        genero = input("Género: ").strip()
        ano = input("Año: ").strip()
        duracion = input("Duración (minutos): ").strip()
        
        try:
            nueva_musica = {
                "tipo": "musica",
                "titulo": titulo,
                "artista": artista,
                "genero": genero,
                "ano": int(ano) if ano.isdigit() else 0,
                "duracion": float(duracion) if duracion.replace('.','').isdigit() else 0.0
            }
            
            self.coleccion.append(nueva_musica)
            print("Música agregada exitosamente!")
            
        except ValueError:
            print("Error: Año y duración deben ser números")
        except Exception as e:
            print(f"Error al agregar música: {e}")
    
    def listar_coleccion(self):
        if not self.coleccion:
            print("La colección está vacía")
            return
        
        print(f"\n=== COLECCIÓN ({len(self.coleccion)} elementos) ===")
        for i, elemento in enumerate(self.coleccion, 1):
            print(f"\n{i}. {elemento['titulo']}")
            print(f"   Tipo: {elemento['tipo'].capitalize()}")
            print(f"   Género: {elemento.get('genero', 'N/A')}")
            print(f"   Año: {elemento.get('ano', 'N/A')}")
            
            if elemento['tipo'] == 'libro':
                print(f"   Autor: {elemento.get('autor', 'N/A')}")
                print(f"   Páginas: {elemento.get('paginas', 'N/A')}")
            elif elemento['tipo'] == 'pelicula':
                print(f"   Director: {elemento.get('director', 'N/A')}")
                print(f"   Duración: {elemento.get('duracion', 'N/A')} min")
            elif elemento['tipo'] == 'musica':
                print(f"   Artista: {elemento.get('artista', 'N/A')}")
                print(f"   Duración: {elemento.get('duracion', 'N/A')} min")
    
    def buscar_elemento(self):
        """Busca elementos por título"""
        if not self.coleccion:
            print("La colección está vacía")
            return
        
        termino = input("Ingresa el título a buscar: ").strip().lower()
        resultados = [elem for elem in self.coleccion if termino in elem['titulo'].lower()]
        
        if resultados:
            print(f"\n=== RESULTADOS ({len(resultados)} encontrados) ===")
            for resultado in resultados:
                print(f"- {resultado['titulo']} ({resultado['tipo'].capitalize()})")
        else:
            print("No se encontraron elementos con ese título")
    
    def filtrar_por_genero(self):
        if not self.coleccion:
            print("La colección está vacía")
            return
        
        genero = input("Ingresa el género a filtrar: ").strip().lower()
        resultados = [elem for elem in self.coleccion if genero in elem.get('genero', '').lower()]
        
        if resultados:
            print(f"\n=== ELEMENTOS DEL GÉNERO '{genero.upper()}' ({len(resultados)} encontrados) ===")
            for resultado in resultados:
                print(f"- {resultado['titulo']} ({resultado['tipo'].capitalize()})")
        else:
            print(f"No se encontraron elementos del género '{genero}'")
    
    def editar_elemento(self):
        if not self.coleccion:
            print("La colección está vacía")
            return
        
        self.listar_coleccion()
        try:
            indice = int(input("Selecciona el número del elemento a editar: ")) - 1
            if 0 <= indice < len(self.coleccion):
                elemento = self.coleccion[indice]
                print(f"Editando: {elemento['titulo']}")
                
                nuevo_titulo = input(f"Nuevo título (actual: {elemento['titulo']}): ").strip()
                if nuevo_titulo:
                    elemento['titulo'] = nuevo_titulo
                    print("Elemento editado exitosamente!")
            else:
                print("Número inválido")
        except ValueError:
            print("Debes ingresar un número válido")
    
    def eliminar_elemento(self):
        if not self.coleccion:
            print("La colección está vacía")
            return
        
        self.listar_coleccion()
        try:
            indice = int(input("Selecciona el número del elemento a eliminar: ")) - 1
            if 0 <= indice < len(self.coleccion):
                elemento_eliminado = self.coleccion.pop(indice)
                print(f"Elemento '{elemento_eliminado['titulo']}' eliminado exitosamente!")
            else:
                print("Número inválido")
        except ValueError:
            print("Debes ingresar un número válido")
    
    def mostrar_estadisticas(self):
        if not self.coleccion:
            print("La colección está vacía")
            return
        
        total = len(self.coleccion)
        libros = len([elem for elem in self.coleccion if elem['tipo'] == 'libro'])
        peliculas = len([elem for elem in self.coleccion if elem['tipo'] == 'pelicula'])
        musica = len([elem for elem in self.coleccion if elem['tipo'] == 'musica'])
        
        print(f"\n=== ESTADÍSTICAS DE LA COLECCIÓN ===")
        print(f"Total de elementos: {total}")
        print(f"Libros: {libros}")
        print(f"Películas: {peliculas}")
        print(f"Música: {musica}")