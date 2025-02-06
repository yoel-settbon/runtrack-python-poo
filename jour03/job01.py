class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants
    
    def get_nombre_habitants(self):
        return self.__nombre_habitants
    
    def ajouterPopulation(self):
        self.__nombre_habitants += 1

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
    
    def ajouterPopulation(self):
        self.__ville.ajouterPopulation()

paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

print(f"Le nombre d'habitants à Paris est : {paris.get_nombre_habitants()}")
print(f"Le nombre d'habitants à Marseille est : {marseille.get_nombre_habitants()}")

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

print(f"Après ajout, le nombre d'habitants à Paris est : {paris.get_nombre_habitants()}")
print(f"Après ajout, le nombre d'habitants à Marseille est : {marseille.get_nombre_habitants()}")