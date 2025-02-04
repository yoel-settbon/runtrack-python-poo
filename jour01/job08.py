"""Créez la classe “Cercle” recevant en argument son rayon, également initialisé
dans le constructeur.
Ajoutez les méthodes suivantes :
- changerRayon qui permet de modifier le rayon.
- afficherInfos qui permet d’afficher toutes les informations du cercle.
- circonférence qui permet de retourner la circonférence.
- aire qui permet de retourner l’aire du cercle.
- diametre qui permet de retourner le diamètre du cercle.

Créez deux cercles avec comme rayon 4 et 7. Pour chaque cercle, affichez ses
informations, affichez sa circonférence, son diamètre et son aire."""


import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    
    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon
    
    def afficherInfos(self):
        print(f"Circonférence : {self.circonference():.2f}")
        print(f"Aire : {self.aire():.2f}")
        print(f"Cercle de rayon : {self.rayon}")
        print(f"Diamètre : {self.diametre()}")
    
    def circonference(self):
        return 2 * math.pi * self.rayon
    
    def aire(self):
        return math.pi * self.rayon ** 2
    
    def diametre(self):
        return 2 * self.rayon

# Création des cercles
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# Affichage des informations pour chaque cercle
print("Informations du premier cercle:")
cercle1.afficherInfos()
print("\nInformations du deuxième cercle:")
cercle2.afficherInfos()

