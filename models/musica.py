from models.elemento import Elemento
class Musica(Elemento):
    
    def __init__(self, titulo, genero, año, artista, duracion):
        super().__init__(titulo, genero, año)
        self.artista = artista
        self.duracion = duracion
        self.tipo = "Música"
    
    def __str__(self):
        return f"🎵 {self.titulo} - {self.artista} ({self.año}) - {self.genero} - {self.duracion}"
    
    def __repr__(self):
        return (f"Musica(titulo='{self.titulo}', artista='{self.artista}', "f"genero='{self.genero}', año={self.año}, duracion='{self.duracion}')")
    
    def to_dict(self):
        data = super().to_dict()  
        data.update({
            'tipo': self.tipo,
            'artista': self.artista,
            'duracion': self.duracion
        })
        return data
    
    def get_duracion_en_segundos(self):
        try:
            partes = self.duracion.split(':')
            if len(partes) == 2:  # MM:SS
                minutos, segundos = map(int, partes)
                return minutos * 60 + segundos
            elif len(partes) == 3:  # HH:MM:SS
                horas, minutos, segundos = map(int, partes)
                return horas * 3600 + minutos * 60 + segundos
            else:
                return 0
        except (ValueError, AttributeError):
            return 0
    
    def es_cancion_larga(self):
        return self.get_duracion_en_segundos() > 360
    
    def es_album(self):
        return self.get_duracion_en_segundos() > 1200
    
    def es_musica_clasica(self):
        return self.año < 1970
    
    def get_info_completa(self):
        
        return {
            'titulo': self.titulo,
            'artista': self.artista,
            'año': self.año,
            'genero': self.genero,
            'duracion': self.duracion,
            'duracion_segundos': self.get_duracion_en_segundos(),
            'es_larga': self.es_cancion_larga(),
            'es_album': self.es_album(),
            'es_clasica': self.es_musica_clasica(),
            'fecha_agregado': self.fecha_agregado
        }