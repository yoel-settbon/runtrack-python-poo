"""Créez une classe Personne avec les attributs nom et prenom. Ajoutez une
méthode SePresenter qui retourne le nom et le prénom de la personne.
Ajoutez aussi un constructeur prenant en paramètres de quoi donner des
valeurs initiales aux attributs nom et prenom. Instanciez plusieurs personnes
avec les valeurs de construction de votre choix et faites appel à la méthode
SePresenter afin de vérifier que tout fonctionne correctement.
Le résultat attendu est : Je suis John Doe /n Je suis Jean Dupond"""


class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"


personne1 = Personne("Doe", "John")
personne2 = Personne("Dupond", "Jean")

print(personne1.SePresenter())
print(personne2.SePresenter())