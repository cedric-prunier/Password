import string
from hashlib import sha256
import json

minuscule = string.ascii_lowercase
majuscule = string.ascii_uppercase
numbers = string.digits
caractere_speciaux = string.punctuation

mdp = input("Veuillez entrer votre mot de passe: ")


def verifier_mot_de_passe(mdp):
    if (
        len(mdp) < 8
        or not any(i in majuscule for i in mdp)
        or not any(i in minuscule for i in mdp)
        or not any(i in numbers for i in mdp)
        or not any(i in caractere_speciaux for i in mdp)
    ):
        return False
    else:
        return True


while not verifier_mot_de_passe(mdp):
    print("Le mot de passe ne respecte pas les exigences de sécurité.")
    mdp = input("Choisissez un nouveau mot de passe : ")
    
mdp_encode = sha256(mdp.encode("utf-8")).hexdigest()

with open("data.json", "a+") as mon_fichier:
    if mdp_encode in mon_fichier.read():
        print("Le mot de passe existe déjà.")
    else:
        with open("data.json", "a+") as mon_fichier:
            json.dump(mdp_encode, mon_fichier)
            mon_fichier.write("\n")
            print("Le mot de passe a été ajouté avec succès dans le fichier data.json.")

with open("data.json", "r") as mon_fichier:
    try:
        data = json.load(mon_fichier)
    except json.decoder.JSONDecodeError as err:
        data = []

while True:
    print("1. Ajouter un mot de passe")
    print("2. Afficher les mots de passe existants")
    print("3. Quitter le gestionnaire. À bientôt mon coco !")
    choice = input("Choisir une option: ")

    if choice == "1":
        mdp = input("Veuillez entrer votre mot de passe: ")
        with open("data.json", "r") as mon_fichier:
            mdp_encode = sha256(mdp.encode("utf-8")).hexdigest()
            if mdp_encode in mon_fichier.read():
                print("Le mot de passe existe déjà.")
            else:
                with open("data.json", "a+") as mon_fichier:
                    json.dump(mdp_encode, mon_fichier)
                    mon_fichier.write("\n")
                    print(
                        "Le mot de passe a été ajouté avec succès dans le fichier data.json."
                    )

    if choice == "2":
        with open("data.json", "r") as mon_fichier:
            print("Contenu du fichier data.json :")
            print(mon_fichier.read())

    if choice == "3":
        quit()
