from models.elemento import Elemento
class Libro(Elemento):
    
    def __init__(self, titulo, genero, año, autor, paginas):
        super().__init__(titulo, genero, año)
        self.autor = autor
        self.paginas = paginas
        self.tipo = "Libro"
    
    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.año}) - {self.genero} - {self.paginas} páginas"
    
    def __repr__(self):
        return (f"Libro(titulo='{self.titulo}', autor='{self.autor}', "
                f"genero='{self.genero}', año={self.año}, paginas={self.paginas})")
    
    def to_dict(self):
        data = super().to_dict()  
        data.update({
            'tipo': self.tipo,
            'autor': self.autor,
            'paginas': self.paginas
        })
        return data
    
    def es_libro_largo(self):
        return self.paginas > 400
    
    def get_info_completa(self):
        
        return {
            'titulo': self.titulo,
            'autor': self.autor,
            'año': self.año,
            'genero': self.genero,
            'paginas': self.paginas,
            'es_largo': self.es_libro_largo(),
            'fecha_agregado': self.fecha_agregado
        }