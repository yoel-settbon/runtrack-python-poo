class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
    
    def informationsVehicule(self):
        return f"Marque: {self.marque}\nModèle: {self.modele}\nAnnée: {self.annee}\nPrix: {self.prix}€"

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4
    
    def informationsVehicule(self):
        return super().informationsVehicule() + f"\nNombre de portes: {self.portes}"

# Instanciation d'un objet Voiture
voiture1 = Voiture("Toyota", "Corolla", 2022, 25000)
info_voiture = voiture1.informationsVehicule()
print(info_voiture)