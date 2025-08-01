from datetime import datetime
class Elemento:
    "Clase base para todos los elementos de la colección"
    
    def __init__(self, titulo, genero, año):
        self.titulo = titulo
        self.genero = genero
        self.año = año
        self.fecha_agregado = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def __str__(self):
        return f"{self.titulo} ({self.año}) - {self.genero}"
    
    def __repr__(self):
        return f"Elemento(titulo='{self.titulo}', genero='{self.genero}', año={self.año})"
    
    def to_dict(self):
        
        return {
            'titulo': self.titulo,
            'genero': self.genero,
            'año': self.año,
            'fecha_agregado': self.fecha_agregado
        }