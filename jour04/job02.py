from jour05.job01 import Personne, Eleve, Professeur

eleve = Eleve()

print(eleve.bonjour())
print(eleve.allerEnCours())

eleve.modifierAge(15)
print(eleve.afficherAge())

professeur = Professeur(matiereEnseignee="Mathématiques", age=40)

print(professeur.bonjour())
print(professeur.enseigner())