class Student:
    def __init__(self, nom: str, prenom: str, numero_etudiant: int, credits: int = 0):
        self._nom = nom
        self._prenom = prenom
        self._numero_etudiant = numero_etudiant
        self._credits = credits
        self._level = self._student_eval()
    
    def add_credits(self, credits):
        if credits > 0:
            self._credits += credits
            self._level = self._student_eval()
        else:
            print("Erreur : Le nombre de crédits doit être supérieur à zéro.")
    def get_credits(self):
        return self._credits
    
    def _student_eval(self):
        if self._credits >= 90:
            return "Excellent"
        elif self._credits >= 80:
            return "Très Bien"
        elif self._credits >= 70:
            return "Bien"
        elif self._credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    def student_info(self):
        print(f"Nom = {self._nom}")
        print(f"Prénom = {self._prenom}")
        print(f"id = {self._numero_etudiant}")
        print(f"Niveau = {self._level}")


etudiant = Student("Doe", "John", 145)


etudiant.add_credits(80)
etudiant.student_info()

print(f"Le nombre de crédits de {etudiant._prenom} {etudiant._nom} est de {etudiant.get_credits()} points.")