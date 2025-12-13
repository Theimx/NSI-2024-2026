# ---------------------------------------------
# CHAPITRE 2 : TRAVAIL PRATIQUE SUR LES OBJETS 
# ---------------------------------------------


# une implémentation du type carte et paquet de carte et leurs fonction associé 

import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return (str(self.valeur) + "de" + str(self.couleur))

class PaquetDeCartes:
    def __init__(self):
        valeurs = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]
        couleurs = ["Coeur", "Carreau", "Trèfle", "Pique"]
        self.cartes = [Carte(v, c) for c in couleurs for v in valeurs]

    def melanger(self):
        random.shuffle(self.cartes)

    def piocher(self):
        if self.cartes:
            return self.cartes.pop()
        return None

    def __len__(self):
        return len(self.cartes)
