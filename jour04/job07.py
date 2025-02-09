import random

# Classe représentant une carte
class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def get_valeur(self):
        """Renvoie la valeur numérique de la carte"""
        if self.valeur in ["Roi", "Dame", "Valet"]:
            return 10
        elif self.valeur == "As":
            return 11  # On gérera le choix entre 1 et 11 plus tard
        else:
            return self.valeur  # Pour les cartes de 2 à 10

    def __str__(self):
        """Affiche la carte sous forme de texte"""
        return f"{self.valeur} de {self.couleur}"

# Classe représentant le paquet de cartes
class Jeu:
    def __init__(self):
        self.paquet = []  # Liste des 52 cartes
        couleurs = ["Cœur", "Carreau", "Trèfle", "Pique"]
        valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Valet", "Dame", "Roi", "As"]

        # Générer toutes les cartes du jeu
        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))

    def melanger(self):
        """Mélange le paquet de cartes"""
        random.shuffle(self.paquet)

    def distribuer(self):
        """Distribue une carte du paquet"""
        if len(self.paquet) > 0:
            return self.paquet.pop()
        else:
            return None  # Plus de cartes

# Classe représentant un joueur (ou le croupier)
class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []  # Liste des cartes du joueur

    def ajouter_carte(self, carte):
        """Ajoute une carte à la main du joueur"""
        self.main.append(carte)

    def calculer_score(self):
        """Calcule le score du joueur en gérant l'As"""
        total = 0
        nb_as = 0

        for carte in self.main:
            valeur = carte.get_valeur()
            if valeur == 11:  # Si c'est un As
                nb_as += 1
            total += valeur

        # Si on dépasse 21, on transforme les As (11 → 1)
        while total > 21 and nb_as > 0:
            total -= 10
            nb_as -= 1

        return total

    def afficher_main(self):
        """Affiche les cartes du joueur"""
        cartes = [str(carte) for carte in self.main]
        return f"{self.nom} a: " + ", ".join(cartes) + f" (Score: {self.calculer_score()})"

def jouer_blackjack():
    """jouer la partie"""
    print("\n--- Bienvenue au Blackjack ! ---\n")

    jeu = Jeu()
    jeu.melanger()

    # Création du joueur et du croupier
    joueur = Joueur("Joueur")
    croupier = Joueur("Croupier")

    # Distribution des cartes initiales
    joueur.ajouter_carte(jeu.distribuer())
    joueur.ajouter_carte(jeu.distribuer())
    croupier.ajouter_carte(jeu.distribuer())

    # Affichage des mains initiales
    print(joueur.afficher_main())
    print(f"{croupier.nom} a: {croupier.main[0]} et une carte cachée\n")

    # Tour du joueur
    while joueur.calculer_score() < 21:
        action = input("Voulez-vous prendre une carte ? (o/n) : ").lower()
        if action == "o":
            joueur.ajouter_carte(jeu.distribuer())
            print(joueur.afficher_main())
        else:
            break

    # Vérification si le joueur dépasse 21
    if joueur.calculer_score() > 21:
        print("\n💥 Vous avez dépassé 21 ! Vous perdez.\n")
        return

    # Tour du croupier
    print("\n--- Tour du Croupier ---")
    croupier.ajouter_carte(jeu.distribuer())
    print(croupier.afficher_main())

    while croupier.calculer_score() < 17:
        croupier.ajouter_carte(jeu.distribuer())
        print(croupier.afficher_main())

    # Victoires
    print("\n--- Résultat ---")
    score_joueur = joueur.calculer_score()
    score_croupier = croupier.calculer_score()

    if score_croupier > 21 or score_joueur > score_croupier:
        print("🎉 Bravo, vous avez gagné !")
    elif score_joueur < score_croupier:
        print("😞 Le croupier gagne !")
    else:
        print("🤝 Égalité !")

jouer_blackjack()