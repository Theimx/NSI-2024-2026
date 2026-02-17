# --------------------------------------------
# CHAPITRE 3 : TRAVAIL PRATIQUE SUR LES PILES 
# --------------------------------------------


class Pile:
    """
    Implémentation Objet de la structure de donnée Pile.
    """

    def __init__(self):
        self.__pile = []  # attribut privé

    def est_vide(self):
        return self.__pile == []

    def empiler(self, x):
        self.__pile.append(x)

    def depiler(self):
        if self.est_vide():
            raise IndexError("Impossible de dépiler : la pile est vide.")
        return self.__pile.pop()

    def hauteur(self):
        return len(self.__file)

    def afficher_pile(self):
        print("^")
        for x in reversed(self.__pile):
            print(x)
        print("—")
        print("Pile de hauteur : " , hauteur(self.__pile))