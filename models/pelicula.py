from models.elemento import Elemento
class Pelicula(Elemento):
    
    def __init__(self, titulo, genero, año, director, duracion):
        super().__init__(titulo, genero, año)
        self.director = director
        self.duracion = duracion
        self.tipo = "Película"
    
    def __str__(self):
        return f"{self.titulo} - Dir: {self.director} ({self.año}) - {self.genero} - {self.duracion} min"
    
    def __repr__(self):
        return (f"Pelicula(titulo='{self.titulo}', director='{self.director}', "f"genero='{self.genero}', año={self.año}, duracion={self.duracion})")
    def to_dict(self):
        data = super().to_dict() 
        data.update({
            'tipo': self.tipo,
            'director': self.director,
            'duracion': self.duracion
        })
        return data
    
    def es_pelicula_larga(self):
        return self.duracion > 150
    
    def get_duracion_formateada(self):
        horas = self.duracion // 60
        minutos = self.duracion % 60
        if horas > 0:
            return f"{horas}h {minutos}min"
        else:
            return f"{minutos}min"
    
    def es_clasica(self):
        return self.año < 1980
    
    def get_info_completa(self):
        return {
            'titulo': self.titulo,
            'director': self.director,
            'año': self.año,
            'genero': self.genero,
            'duracion': self.duracion,
            'duracion_formateada': self.get_duracion_formateada(),
            'es_larga': self.es_pelicula_larga(),
            'es_clasica': self.es_clasica(),
            'fecha_agregado': self.fecha_agregado
        }