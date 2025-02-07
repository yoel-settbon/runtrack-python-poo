class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    def surface(self):
        return f"Surface : {self.__longueur}*{self.__largeur}"
    
    def get_longueur(self):
        return self.__longueur
    def get_largeur(self):
        return self.__largeur
    def set_longueur(self, longueur):
        self.__longueur = longueur
    def set_largeur(self, largeur):
        self.__largeur = largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.__hauteur
    def get_hauteur(self):
        return self.__hauteur
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

rect = Rectangle(10,5)
print("Perimetre : ", rect.perimetre())

para = Parallelepipede(10, 5, 8)
print("Volume : ", para.volume())