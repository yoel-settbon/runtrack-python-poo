class Voiture:
    def __init__(self, marque, modele, annee, km, en_marche = False):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__km = km
        self.__en_marche = en_marche
        self.__reservoir = 50
    
    def get_marque(self):
        return self.__marque
    def get_modele(self):
        return self.__modele
    def get_annee(self):
        return self.__annee
    def get_km(self):
        return self.__km
    def get_en_marche(self):
        return self.__en_marche
    def get_reservoir(self):
        return self.__reservoir
    
    def set_marque(self, marque):
        self.__marque = marque
    def set_modele(self, modele):
        self.__modele = modele
    def set_annee(self, annee):
        self.__annee = annee
    def set_km(self, km):
        self.__km = km
    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche
    def set_reservoir(self, reservoir):
        self.__reservoir = reservoir
    
    def __verifier_plein(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print("La voiture a démarré.")
        else:
            print("Le réservoir est trop bas pour démarrer.")
    
    def demarrer_voiture(self):
        if self.__verifier_plein() > 5:
            print("La voiture a démarré.")
        else:
            print("Le réservoir est trop bas pour démarrer.")
    def arreter_voiture(self):
        self.__en_marche = False
        print("La voiture est arrêtée.")

ma_voiture = Voiture("Toyota", "Corolla", 2020, 15000)
ma_voiture.demarrer_voiture()