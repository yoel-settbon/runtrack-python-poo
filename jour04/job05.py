from job04 import Forme, Rectangle

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
    
    def aire(self):
        return 3.14 * self.radius **2

rectangle = Rectangle(5, 10)
print("L'aire du rectangle est : ", rectangle.aire())

cercle1 = Cercle(8)
print("L'aire du cercle est : ", cercle1.aire())