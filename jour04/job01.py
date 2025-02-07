class Personne:
    def __init__(self, age=14):
        self.age = age
    
    def afficherAge(self):
        return f"Age : {self.age}"
    def bonjour(self):
        return "Hello"
    def modifierAge(self, nouvel_age):
        if isinstance(nouvel_age, int) and nouvel_age > 0:
            self.age = nouvel_age
        else:
            return "Veuillez entrer un âge valide (entier positif)."


class Eleve(Personne):
    def allerEnCours(self):
        return "Je vais en cours"
    def afficherAge(self):
        return f"J'ai {self.age} ans."

class Professeur:
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee
    def enseigner(self):
        return "Le cours va commencer."

personne = Personne()
eleve = Eleve()

print(eleve.afficherAge())
print(eleve.allerEnCours())

modification = eleve.modifierAge(18)
if modification:
    print(modification)

print(eleve.afficherAge())