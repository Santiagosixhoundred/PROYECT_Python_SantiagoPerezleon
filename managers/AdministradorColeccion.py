import os
from models import libro, pelicula, musica
from utils.archivo_handler import cargar_datos, guardar_datos
class AdministradorColeccion:
    
    def __init__(self, archivo_datos="data/coleccion.json"):
        self.archivo_datos = archivo_datos
        self.coleccion = []
        self.datos = cargar_datos(archivo_datos)
        self.cargar_datos()
    
    def cargar_datos(self):
        try:
            datos = self ()
            self.coleccion = []
            
            for item in datos:
                if item['tipo'] == 'Libro':
                    elemento = libro(
                        item['titulo'], item['genero'], item['año'], item['autor'], item['paginas']
                    )
                elif item['tipo'] == 'Película':
                    elemento = pelicula(
                        item['titulo'], item['genero'], item['año'], item['director'], item['duracion']
                    )
                elif item['tipo'] == 'Música': elemento = musica(
                        item['titulo'], item['genero'], item['año'], item['artista'], item['duracion']
                )
                else:
                    continue  
                
                if 'fecha_agregado' in item:
                    elemento.fecha_agregado = item['fecha_agregado']
                
                self.coleccion.append(elemento)
            
            print(f"Datos cargados: {len(self.coleccion)} elementos")
            
        except Exception as e:
            print(f"Error al cargar datos: {e}")
            print("Iniciando con colección vacía")
    
    def guardar_datos(self):
        try:
            datos = [elemento.to_dict() for elemento in self.coleccion]
            self.archivo_handler.guardar_datos(datos)
            print("Datos guardados exitosamente!")
            return True
        except Exception as e:
            print(f"Error al guardar datos: {e}")
            return False
    
    def agregar_elemento(self):
        print("\n AGREGAR NUEVO ELEMENTO")
        print("1. Libro")
        print("2. Película") 
        print("3. Música")
        
        try:
            tipo = input("Seleccione el tipo (1-3): ").strip()
            
            if tipo == "1":
                elemento = self._crear_libro()
            elif tipo == "2":
                elemento = self._crear_pelicula()
            elif tipo == "3":
                elemento = self._crear_musica()
            else:
                print("Opción no válida")
                return False
            
            if elemento:
                self.coleccion.append(elemento)
                print(f"{elemento.tipo} agregado exitosamente: {elemento.titulo}")
                return True
                
        except ValueError:
            print("Error: Por favor ingrese valores válidos")
        except Exception as e:
            print(f"Error inesperado: {e}")
        return False
    
    def _crear_libro(self):
        titulo = input("Título del libro: ").strip()
        if not titulo:
            print("El título es obligatorio")
            return None
            
        autor = input("Autor: ").strip()
        if not autor:
            print("El autor es obligatorio")
            return None
            
        genero = input("Género: ").strip() or "Sin género"
        año = int(input("Año de publicación: "))
        paginas = int(input("Número de páginas: "))
        
        if paginas <= 0:
            print("El número de páginas debe ser mayor a 0")
            return None
        
        return libro(titulo, genero, año, autor, paginas)
    
    def _crear_pelicula(self):
        titulo = input("Título de la película: ").strip()
        if not titulo:
            print("El título es obligatorio")
            return None
            
        director = input("Director: ").strip()
        if not director:
            print("El director es obligatorio")
            return None
            
        genero = input("Género: ").strip() or "Sin género"
        año = int(input("Año de estreno: "))
        duracion = int(input("Duración (minutos): "))
        if duracion <= 0:
            print(" La duración debe ser mayor a 0")
            return None
        
        return pelicula(titulo, genero, año, director, duracion)
    
    def _crear_musica(self):
        titulo = input("Título de la canción/álbum: ").strip()
        if not titulo:
            print("El título es obligatorio")
            return None
            
        artista = input("Artista: ").strip()
        if not artista:
            print("El artista es obligatorio")
            return None
            
        genero = input("Género: ").strip() or "Sin género"
        año = int(input("Año: "))
        duracion = input("Duración (ej: 3:45): ").strip()
        
        if not duracion:
            print(" La duración es obligatoria")
            return None
        
        return musica(titulo, genero, año, artista, duracion)
    
    def listar_coleccion(self):
        if not self.coleccion:
            print("La colección está vacía")
            return
        
        print(f"\nCOLECCIÓN COMPLETA ({len(self.coleccion)} elementos)")
        print("-" * 80)
        for i, elemento in enumerate(self.coleccion, 1):
            print(f"{i:2d}. {elemento}")
            print(f"    Agregado: {elemento.fecha_agregado}")
            print()
    
    def buscar_elemento(self):
        if not self.coleccion:
            print("La colección está vacía")
            return
        
        termino = input("Ingrese el título a buscar: ").strip().lower()
        if not termino:
            print(" Debe ingresar un término de búsqueda")
            return
        
        resultados = [elem for elem in self.coleccion if termino in elem.titulo.lower()]
        if not resultados:
            print("No se encontraron elementos")
            return
        
        print(f"\n🔍 RESULTADOS DE BÚSQUEDA ({len(resultados)} encontrados)")
        print("-" * 60)
        for i, elemento in enumerate(resultados, 1):
            print(f"{i}. {elemento}")
    
    def filtrar_por_genero(self):
        if not self.coleccion:
            print("La colección está vacía")
            return
        generos = sorted(list(set(elem.genero for elem in self.coleccion)))
        
        print("\nGÉNEROS DISPONIBLES:")
        for i, genero in enumerate(generos, 1):
            cantidad = sum(1 for elem in self.coleccion if elem.genero == genero)
            print(f"{i:2d}. {genero} ({cantidad} elementos)")
        
        try:
            seleccion = int(input("Seleccione un género (número): ")) - 1
            if 0 <= seleccion < len(generos):
                genero_seleccionado = generos[seleccion]
                resultados = [elem for elem in self.coleccion if elem.genero == genero_seleccionado]
                
                print(f"\n ELEMENTOS DE GÉNERO '{genero_seleccionado}' ({len(resultados)} encontrados)")
                print("-" * 60)
                for i, elemento in enumerate(resultados, 1):
                    print(f"{i}. {elemento}")
            else:
                print(" Selección no válida")
        except (ValueError, IndexError):
            print("Por favor ingrese un número válido")
    
    def eliminar_elemento(self): 
        if not self.coleccion:
            print("La colección está vacía")
            return False
        
        self.listar_coleccion()
        
        try:
            indice = int(input("Ingrese el número del elemento a eliminar: ")) - 1
            if 0 <= indice < len(self.coleccion):
                elemento = self.coleccion.pop(indice)
                print(f"Elemento eliminado: {elemento.titulo}")
                return True
            else:
                print("Número no válido")
        except ValueError:
            print(" Por favor ingrese un número válido")
        
        return False
    
    def editar_elemento(self):
        if not self.coleccion:
            print("La colección está vacía")
            return False
        
        self.listar_coleccion()
        
        try:
            indice = int(input("Ingrese el número del elemento a editar: ")) - 1
            if 0 <= indice < len(self.coleccion):
                elemento = self.coleccion[indice]
                return self._editar_elemento_especifico(elemento)
            else:
                print("Número no válido")
        except ValueError:
            print("Por favor ingrese un número válido")
        
        return False
    
    def _editar_elemento_especifico(self, elemento):
        print(f"\nEditando: {elemento}")
        print("Presione Enter para mantener el valor actual")
        
        try:
            nuevo_titulo = input(f"Título [{elemento.titulo}]: ").strip()
            if nuevo_titulo:
                elemento.titulo = nuevo_titulo
            
            nuevo_genero = input(f"Género [{elemento.genero}]: ").strip()
            if nuevo_genero:
                elemento.genero = nuevo_genero
            
            nuevo_año = input(f"Año [{elemento.año}]: ").strip()
            if nuevo_año:
                elemento.año = int(nuevo_año)
            
            if isinstance(elemento, libro):
                self._editar_libro(elemento)
            elif isinstance(elemento, pelicula):
                self._editar_pelicula(elemento)
            elif isinstance(elemento, musica):
                self._editar_musica(elemento)
            
            print("Elemento editado exitosamente")
            return True
            
        except ValueError:
            print("Error en los datos ingresados")
            return False
    
    def _editar_libro(self, libro):
        nuevo_autor = input(f"Autor [{libro.autor}]: ").strip()
        if nuevo_autor:
            libro.autor = nuevo_autor
        nuevas_paginas = input(f"Páginas [{libro.paginas}]: ").strip()
        if nuevas_paginas:
            paginas = int(nuevas_paginas)
            if paginas > 0:
                libro.paginas = paginas
            else:
                print("Las páginas deben ser mayor a 0")
    
    def _editar_pelicula(self, pelicula):
        nuevo_director = input(f"Director [{pelicula.director}]: ").strip()
        if nuevo_director:
            pelicula.director = nuevo_director
        nueva_duracion = input(f"Duración [{pelicula.duracion}]: ").strip()
        if nueva_duracion:
            duracion = int(nueva_duracion)
            if duracion > 0:
                pelicula.duracion = duracion
            else:
                print("La duración debe ser mayor a 0")
    
    def _editar_musica(self, musica):
        nuevo_artista = input(f"Artista [{musica.artista}]: ").strip()
        if nuevo_artista:
            musica.artista = nuevo_artista
        nueva_duracion = input(f"Duración [{musica.duracion}]: ").strip()
        if nueva_duracion:
            musica.duracion = nueva_duracion
    
    def mostrar_estadisticas(self):
        """Muestra estadísticas detalladas de la colección"""
        if not self.coleccion:
            print("📭 La colección está vacía")
            return
        
        libros = [e for e in self.coleccion if isinstance(e, libro)]
        peliculas = [e for e in self.coleccion if isinstance(e, pelicula)]
        musica = [e for e in self.coleccion if isinstance(e, musica)]
        
        generos = {}
        for elemento in self.coleccion:
            generos[elemento.genero] = generos.get(elemento.genero, 0) + 1
        
        print("\nESTADÍSTICAS DE LA COLECCIÓN")
        print("=" * 50)
        print(f"Total de elementos: {len(self.coleccion)}")
        print(f"Libros: {len(libros)}")
        print(f" Películas: {len(peliculas)}")
        print(f" Música: {len(musica)}")
        
        print("\n Por género:")
        for genero, cantidad in sorted(generos.items()):
            porcentaje = (cantidad / len(self.coleccion)) * 100
            print(f"  {genero}: {cantidad} ({porcentaje:.1f}%)")
        
        if libros:
            avg_pages = sum(libro.paginas for libro in libros) / len(libros)
            print(f"\n📚 Estadísticas de libros:")
            print(f"  Promedio de páginas: {avg_pages:.0f}")
            print(f"  Libros largos (>400 pág): {sum(1 for l in libros if l.es_libro_largo())}")
        
        if peliculas:
            avg_duration = sum(pelicula.duracion for pelicula in peliculas) / len(peliculas)
            print(f"\n🎬 Estadísticas de películas:")
            print(f"  Duración promedio: {avg_duration:.0f}")