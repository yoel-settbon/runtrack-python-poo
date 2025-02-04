"""Créez la classe Produit avec des attributs nom, prixHT, TVA. Implémentez la
méthode CalculerPrixTTC qui retourne le prix produit avec la TVA. Ajoutez la
méthode afficher qui liste l’ensemble des informations du produit.
Créez plusieurs produits et calculez leurs TVA.

Ajoutez des méthodes permettant de modifier le nom du produit et son prix.
Ainsi que des méthodes permettant de retourner chaque information du
produit.
Modifiez le nom et le prix de chaque produit et affichez en console le nouveau
prix des produits.
La fonction print() ne doit pas être utilisée dans la classe Produit.
Sur vos scripts doit apparaître l’ensemble des méthodes appelées tout au
long des exercices."""


class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    def calculer_prix_TTC(self):
        return self.prixHT * (1 + self.TVA / 100)
    
    def afficher(self):
        return f"Nom : {self.nom}, prix HT : {self.prixHT}, TVA : {self.TVA}, Prix TTC : {self.calculer_prix_TTC()}€"
    
    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom
    
    def modifier_prixHT(self, prixHT):
        self.prixHT = prixHT
    
    
