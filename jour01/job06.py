"""Créez une classe Animal avec un attribut age initialisé à zéro et prenom
initialisé vide dans son constructeur.
Instanciez un objet Animal et affichez en console l’attribut âge. Créez une
méthode vieillir qui ajoute 1 à l'âge de l’animal. Faites vieillir votre animal et
affichez son âge mis à jour en console.

- Résultat attendu :
L'âge de l'animal 0 ans
#Age de l'animal apres appel de la methode vieillir
L'age de l'animal 1 ans

Créez une méthode nommer qui prend en paramètre le nom de l'animal. Nommez votre animal et affichez en console son nom

- Résultat attendu :
L'animal se nomme Luna"""


class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

mon_animal = Animal()

print(f"L'âge de l'animal {mon_animal.age} ans")

mon_animal.vieillir()

print(f"L'âge de l'animal après appel de la méthode vieillir: {mon_animal.age} ans")

mon_animal.nommer("Luna")

print(f"L'animal se nomme {mon_animal.prenom}")