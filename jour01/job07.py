"""Créez une classe Personnage représentant un personnage de jeu. Le plateau
de jeu est représenté par une matrice. Le joueur est défini par ses attributs x
et y, représentant les index du tableau.
Créez le constructeur de cette classe en initialisant la position (x et y).
Créez les méthodes : gauche, droite, bas et haut permettant respectivement
de faire avancer à gauche et à droite, en haut ou en bas.
Implémentez une méthode “position” renvoyant les coordonnées sous forme
d’un tuple."""


class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)

plateau = [[0]*5 for _ in range(5)]  # Plateau de jeu de 5x5, rempli de 0 (pour l'exemple)

personnage = Personnage(2, 2)

print("Position initiale :", personnage.position())

personnage.gauche()
print("Après avoir bougé à gauche :", personnage.position())

personnage.droite()
print("Après avoir bougé à droite :", personnage.position())

personnage.haut()
print("Après avoir bougé en haut :", personnage.position())

personnage.bas()
print("Après avoir bougé en bas :", personnage.position())