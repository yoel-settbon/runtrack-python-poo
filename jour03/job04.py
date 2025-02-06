class Joueur:
    def __init__(self, nom, numero, position, buts, passes_decisives, cartons_jaune, cartons_rouge):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = buts
        self.passes_decisives = passes_decisives
        self.cartons_jaune = cartons_jaune
        self.cartons_rouge = cartons_rouge
    
    def marquerUnBut(self):
        self.but += 1
    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1
    def recevoirUnCartonJaune(self):
        self.cartons_jaune += 1
    def recevoirUnCartonRouge(self):
        self.cartons_rouge += 1
    def afficherStatistiques(self):
        print(f"{self.nom}\n{self.numero}\n{self.position}\n{self.buts} buts marqués\n{self.passes_decisives} passes décisives\nCartons Jaune : {self.cartons_jaune}\nCartons Rouge : {self.cartons_rouge}")



class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []
    
    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)
    def afficher_statistiques_joueurs(self):
        print(f"Statistiques de l'équipe {self.nom}:")
        for joueur in self.joueurs:
            print(joueur)
    def mettre_a_jour_statistiques(self, joueur_nom, action):
        for joueur in self.joueurs:
            if joueur.nom == joueur_nom:
                if action == "but":
                    joueur.marquer_but()
                elif action == "carton_jaune":
                    joueur.recevoir_carton_jaune()
                elif action == "carton rouge":
                    joueur.recevoir_carton_rouge()
                break

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.buts = 0
        self.cartons_jaunes = 0
        self.carton_rouge = 0

    def marquer_but(self):
        self.buts += 1

    def recevoir_carton_jaune(self):
        self.cartons_jaunes += 1

    def recevoir_carton_rouge(self):
        self.carton_rouge += 1

    def __str__(self):
        return f"{self.nom} - Buts: {self.buts}, Cartons Jaunes: {self.cartons_jaunes}, Carton Rouge: {self.carton_rouge}"


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def afficher_statistiques_joueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.joueurs:
            print(joueur)

    def mettre_a_jour_statistiques(self, joueur_nom, action):
        for joueur in self.joueurs:
            if joueur.nom == joueur_nom:
                if action == "but":
                    joueur.marquer_but()
                elif action == "carton_jaune":
                    joueur.recevoir_carton_jaune()
                elif action == "carton_rouge":
                    joueur.recevoir_carton_rouge()
                break


# Création des joueurs
joueur1 = Joueur("Lucas")
joueur2 = Joueur("Emma")
joueur3 = Joueur("Mia")

# Création des équipes
equipe1 = Equipe("Équipe A")
equipe2 = Equipe("Équipe B")

# Ajout des joueurs aux équipes
equipe1.ajouter_joueur(joueur1)
equipe1.ajouter_joueur(joueur2)

equipe2.ajouter_joueur(joueur3)

# Affichage des statistiques avant le match
equipe1.afficher_statistiques_joueurs()
equipe2.afficher_statistiques_joueurs()

# Simulation du match
# Équipe A marque un but et reçoit un carton jaune
equipe1.mettre_a_jour_statistiques("Lucas", "but")
equipe1.mettre_a_jour_statistiques("Emma", "carton_jaune")

# Équipe B reçoit un carton rouge
equipe2.mettre_a_jour_statistiques("Mia", "carton_rouge")

# Affichage des statistiques après le match
print("\nStatistiques après le match:")
equipe1.afficher_statistiques_joueurs()
equipe2.afficher_statistiques_joueurs()
