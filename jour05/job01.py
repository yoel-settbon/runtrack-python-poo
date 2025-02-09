class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material
    
    def change_material(self, new_material):
        self.material = new_material
    
    def __str__(self):
        return f"Nom : {self.material}\nMatériau : {self.material}"

class Ship:
    def __init__(self, name):
        self.name =name
        self.__parts = {
            "Mât": Part("Mât", "Bois"),
            "Coque": Part("Coque", "Bois"),
            "Voile": Part("Voile", "Coton")
        }
        self.history = []
    
    def displat_state(self):
        print(f"Etat du bateau {self.name} :")
        for part in self.__parts.values():
            print(part)
    
    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            self.history.append(f"Remplacement de {part_name} par {new_part.name}")
            self.__parts[part_name] = new_part
            print(f"{part_name} remplacé par {new_part.name}")
        else:
            print(f"La pièce {part_name} n'existe pas.")

    def change_part(self, part_name, new_material):
        if part_name in self.__parts:
            self.history.append(f"Changement de matériau de {part_name} : {self.__parts[part_name].material} -> {new_material}")
            self.__parts[part_name].change_material(new_material)
            print(f"Matériau de {part_name} changé en {new_material}")
        else:
            print(f"La pièce {part_name} n'existe pas.")

    def display_history(self):
        print("Historique des modifications :")
        for change in self.history:
            print(change)

class RacingShip(Ship):
    def __init__(self, name, max_speed):
        super().__init__(name)
        self.max_speed = max_speed

    def display_speed(self):
        print(f"Vitesse maximale : {self.max_speed} nœuds")

# Menu interactif
def menu():
    ship = Ship("Thésée")
    while True:
        print("\n--- Menu ---")
        print("1. Afficher l'état du bateau")
        print("2. Remplacer une pièce")
        print("3. Modifier le matériau d'une pièce")
        print("4. Afficher l'historique des modifications")
        print("5. Quitter")
        choice = input("Choisissez une option : ")

        if choice == "1":
            ship.display_state()
        elif choice == "2":
            part_name = input("Nom de la pièce à remplacer : ")
            new_name = input("Nom de la nouvelle pièce : ")
            new_material = input("Matériau de la nouvelle pièce : ")
            ship.replace_part(part_name, Part(new_name, new_material))
        elif choice == "3":
            part_name = input("Nom de la pièce à modifier : ")
            new_material = input("Nouveau matériau : ")
            ship.change_part(part_name, new_material)
        elif choice == "4":
            ship.display_history()
        elif choice == "5":
            break
        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    menu()