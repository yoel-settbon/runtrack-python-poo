class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
    
    def afficher(self):
        print(f"Numéro de compte : {self.__numero_compte}")
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        print(f"Solde : {self.__solde}")
        print(f"Découvert autorisé : {'Oui' if self.__decouvert else 'Non'}")
    
    def afficherSolde(self):
        print(f"Solde actuel : {self.__solde} euros")
    
    def versement(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"Versement de {montant}euros effectué. Nouveau solde : {self.__solde}euros")
        else:
            print("Le montant versé doit être positif.")
    
    def retrait(self, montant):
        if montant <= 0:
            print("Le montant du retrait doit être positif.")
        elif self.__solde - montant < 0 and not self.__decouvert:
            print(f"Erreur : Solde insuffisant pour un retrait de {montant}euros.")
        else:
            self.__solde -= montant
            print(f"Retrait de {montant}euros effectué. Nouveau solde : {self.__solde}euros.")
    
    def agios(self):
        if self.__solde < 0:
            agios = abs(self.__solde) * 0.02
            self.__solde -= agios
            print(f"Agios appliqués : {agios}euros. Nouveau solde : {self.__solde}euros.")
    
    def virement(self, compte_destinataire, montant):
        if montant <= 0:
            print(f"Le montant du virement doit être positif.")
        elif self.__solde < montant and not self.__decouvert:
            print(f"Erreur : Solde insuffisant pour effectuer ce virement.")
        else:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant}euros effectué vers le compte de {compte_destinataire.__prenom} {compte_destinataire.__nom}. Nouveau solde : {self.__solde}euros.")

compte1 = CompteBancaire("12345", "Dupont", "Jean", 1500)
compte2 = CompteBancaire("67890", "Martin", "Lucie", -200, True)

print("Compte de Jean Dupont :")
compte1.afficher()
print("\nCompte de Lucie Martin :")
compte2.afficher()

compte1.versement(500)
compte1.retrait(1000)
compte1.afficherSolde()

compte2.agios()
compte2.retrait(50)
compte2.afficherSolde()

compte1.virement(compte2, 500)

print("\nCompte de Jean Dupont après virement : ")
compte1.afficher()
print("\nCompte de Lucie Martin après virement : ")
compte2.afficher()