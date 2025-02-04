class Livre:
    def __init__(self, titre: str, auteur: str, pages):
        self._titre = titre
        self._auteur = auteur
        self.set_pages(pages)
        self._disponible = True

    def get_titre(self):
        return self._titre
    def get_auteur(self):
        return self._auteur
    def get_pages(self):
        return self._pages
    
    def set_titre(self, titre):
        self._titre = titre
    def set_auteur(self, auteur):
        self._auteur = auteur
    def set_pages(self, pages):
        if type(pages) == int and pages > 0:
            self._pages = pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")
            self._pages = 0
    
    def verification(self):
        return self._disponible
    def emprunter(self):
        if self.verification():
            self._disponible = False
            print(f"Le livre '{self.get_titre()}' a été emprunté.")
        else:
            print(f"Le livre '{self.get_titre()}' n'est pas disponible.")
    def rendre(self):
        if not self.verification():
            self._disponible = True
            print(f"Le livre '{self.get_titre()}' a été rendu.")
        else:
            print(f"Le livre '{self.get_titre()}' n'a pas été emprunté.")

livre = Livre("MAUS", "Art Spiegleman", 328)
print(livre.get_titre())
print(livre.get_auteur())

livre.set_pages(10)
print(livre.get_pages())