import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts !")

    def est_vivant(self):
        return self.vie > 0

class Jeu:
    def __init__(self):
        self.niveau = None

    def choisirNiveau(self):
        niveaux = {1: 50, 2: 70, 3: 100}
        while True:
            try:
                choix = int(input("Choisissez un niveau de difficulté (1: Facile, 2: Moyen, 3: Difficile) : "))
                if choix in niveaux:
                    self.niveau = niveaux[choix]
                    break
                else:
                    print("Veuillez entrer un choix valide (1, 2 ou 3).")
            except ValueError:
                print("Veuillez entrer un nombre valide.")

    def verifierGagnant(self, joueur, ennemi):
        if not joueur.est_vivant():
            print(f"{joueur.nom} est mort ! {ennemi.nom} a gagné !")
            return ennemi.nom
        elif not ennemi.est_vivant():
            print(f"{ennemi.nom} est mort ! {joueur.nom} a gagné !")
            return joueur.nom
        return None

    def lancerJeu(self):
        self.choisirNiveau()
        joueur = Personnage("Joueur", self.niveau)
        ennemi = Personnage("Ennemi", self.niveau)

        print(f"Début du combat ! {joueur.nom} ({joueur.vie} PV) vs {ennemi.nom} ({ennemi.vie} PV)")

        while joueur.est_vivant() and ennemi.est_vivant():
            joueur.attaquer(ennemi)
            if not ennemi.est_vivant():
                break
            ennemi.attaquer(joueur)
            print(f"{joueur.nom} : {joueur.vie} PV | {ennemi.nom} : {ennemi.vie} PV")

        gagnant = self.verifierGagnant(joueur, ennemi)
        print(f"Le combat est terminé. {gagnant} remporte la victoire !")

# Lancement du jeu
jeu = Jeu()
jeu.lancerJeu()
