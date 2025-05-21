import string
import secrets
valeur = input("Choisissez la longueur du mot de passe (par défaut 12) : ")
try:
    longueur = int(valeur) if valeur else 12
    if longueur <= 0:
        raise ValueError("La longueur doit être un entier positif.")
except ValueError:
    print("Veuillez entrer un nombre entier valide.")
    exit()
majuscule = input("inclure des majuscules? (o/n): ").lower() == 'o'
chiffres = input("inclure des chiffres? (o/n): ").lower() == 'o'
symbole = input("inclure des symboles? (o/n) : ").lower() == 'o'

alphabet = string.ascii_lowercase
if majuscule:
    alphabet += string.ascii_uppercase
if chiffres:
    alphabet += string.digits
if symbole:
    alphabet += string.punctuation

mot_de_passe = ''
for _ in range(longueur):
    mot_de_passe += secrets.choice(alphabet)

print(f">>> {mot_de_passe}")
def verifier_force(mdp):
    force = 0
    if any(c.islower() for c in mdp):
        force += 1
    if any(c.isupper() for c in mdp):
        force += 1
    if any(c.isdigit() for c in mdp):
        force += 1
    if any(c in string.punctuation for c in mdp):
        force += 1
    if len(mdp) >= 12:
        force += 1

    if force <= 2:
        return "Faible"
    elif force == 3:
        return "Moyenne"
    elif force == 4:
        return "Forte"
    else:
        return "Très forte"
niveau = verifier_force(mot_de_passe)
print(f"🔒 Force estimée du mot de passe : {niveau}")
