class Commande:
    def __init__(self, numero_commande, plats_commandes=None, statut="en cours"):
        self.__numero_commande = numero_commande
        self.__plats_commandes = plats_commandes if plats_commandes is not None else {}
        self.__statut = statut

    def ajouter_plat(self, nom_plat, prix_plat):
        if nom_plat not in self.__plats_commandes:
            self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "en cours"}
        else:
            print(f"Le plat {nom_plat} est déjà dans la commande.")

    def annuler_commande(self):
        if self.__statut == "en cours":
            self.__statut = "annulée"
            print("La commande a été annulée.")
        else:
            print("Impossible d'annuler une commande qui n'est pas en cours.")

    def __calculer_total(self):
        total = 0
        for plat in self.__plats_commandes.values():
            total += plat["prix"]
        return total

    def afficher_commande(self):
        print(f"Commande numéro: {self.__numero_commande}")
        print("Plats commandés:")
        for plat, details in self.__plats_commandes.items():
            print(f"- {plat}: {details['prix']}€ (Statut: {details['statut']})")
        total = self.__calculer_total()
        print(f"Total à payer: {total}€")

    def calculer_tva(self, taux_tva=20):
        total = self.__calculer_total()
        tva = (total * taux_tva) / 100
        return tva

    def get_statut(self):
        return self.__statut
    def get_numero_commande(self):
        return self.__numero_commande
    def get_plats_commandes(self):
        return self.__plats_commandes
