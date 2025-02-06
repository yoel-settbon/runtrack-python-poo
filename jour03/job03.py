# Classe Tache représentant une tâche
class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def marquerCommeFinie(self):
        "change le statut de la tâche"
        self.statut = "terminée"
    def get_titre(self):
        """donne le titre de la tâche"""
        return self.titre
    def get_description(self):
        """donne la description"""
        return self.description
    def get_statut(self):
        """donne le statut de la tâche"""
        return self.statut
    def afficher(self):
        """affichage de la tâche"""
        print(f"Tâche : {self.titre}\nDescription : {self.description}\nStatut : {self.statut}\n")

class ListeDeTaches:
    def __init__(self):
        self.__taches = []

    def ajouterTache(self, tache):
        """ajoute une tâche à la liste"""
        self.__taches.append(tache)
    def supprimerTache(self, titre):
        """supprime une tâche de la liste"""
        for tache in self.__taches:
            if tache.get_titre() == titre:
                self.__taches.remove(tache)
                print(f"Tâche '{titre}' supprimée.")
                return
        print(f"Tâche '{titre}' non trouvée.")
    def marquerCommeFinie(self, titre):
        """marque une tâche comme terminée"""
        for tache in self.__taches:
            if tache.get_titre() == titre:
                tache.marquerCommeFinie()
                print(f"Tâche '{titre}' marquée comme terminée.")
                return
        print(f"Tâche '{titre}' non trouvée.")
    def afficherListe(self):
        """affiche toutes les tâches"""
        if not self.__taches:
            print("Aucune tâche dans la liste.")
        else:
            print("Liste des tâches :")
            for tache in self.__taches:
                tache.afficher()
    def filterListe(self, statut):
        """filtre les tâches par statut"""
        filtres = [tache for tache in self.__taches if tache.get_statut() == statut]
        if not filtres:
            print(f"Aucune tâche avec le statut '{statut}'.")
        else:
            print(f"Tâches avec le statut '{statut}' :")
            for tache in filtres:
                tache.afficher()

# Test du code
if __name__ == "__main__":
    # Création des tâches
    tache1 = Tache("Acheter du lait", "Aller au supermarché pour acheter du lait")
    tache2 = Tache("Répondre aux emails", "Répondre aux emails professionnels")
    tache3 = Tache("Faire du sport", "Aller courir dans le parc")

    # Création de la liste de tâches
    liste = ListeDeTaches()

    # Ajouter des tâches
    liste.ajouterTache(tache1)
    liste.ajouterTache(tache2)
    liste.ajouterTache(tache3)

    # Afficher toutes les tâches
    print("Affichage de toutes les tâches :")
    liste.afficherListe()

    # Marquer une tâche comme terminée
    liste.marquerCommeFinie("Acheter du lait")

    # Afficher toutes les tâches après modification
    print("\nAffichage de toutes les tâches après modification :")
    liste.afficherListe()

    # Filtrer les tâches par statut
    print("\nFiltrer les tâches 'à faire' :")
    liste.filterListe("à faire")

    print("\nFiltrer les tâches 'terminée' :")
    liste.filterListe("terminée")

    # Supprimer une tâche
    liste.supprimerTache("Répondre aux emails")

    # Afficher les tâches après suppression
    print("\nAffichage de toutes les tâches après suppression :")
    liste.afficherListe()