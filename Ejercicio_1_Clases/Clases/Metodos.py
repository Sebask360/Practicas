class Pajaro:
    
    alas = True
    
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie
        
    def piar(self):
        print(f"pio, mi  color es {self.color}")
    
    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        
    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pajaro escolor {self.color}")
        
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"El pajaro puso {cantidad} huevos")
        cls.alas = True
        print(Pajaro.alas)
        
    @staticmethod
    def mirar():
        print(f"El pajaro mira")
piolin = Pajaro('amarillo', 'canario')
piolin.pintar_negro()

piolin.alas = False
print(piolin.alas)

Pajaro.poner_huevos(5)

piolin.poner_huevos(4)