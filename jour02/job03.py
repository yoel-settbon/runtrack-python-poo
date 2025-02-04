from job02 import Livre

livre = Livre("MAUS","Art Spiegleman", 100)

livre.emprunter()
livre.rendre()
print(livre.verification)