# --------------------------------------------
# CHAPITRE 3 : TRAVAIL PRATIQUE SUR LES FILES 
# --------------------------------------------


class File:
    def __init__(self):
        self.__file = []  # attribut privé

    def est_vide(self):
        return self.__file == []

    def enfiler(self, x):
        self.__file.append(x)

    def defiler(self):
        if not self.est_vide():
            return self.__file.pop(0)
        else:
            print("ERREUR Impossible de défiler : la file est vide.")

    def longeur(self):
        return len(self.__file)

    def afficher_file(self):
        print("File de longeur : " , longeur(self.__file))
        res = '>>> '
        for x in reversed(self.__file):
            res += str(x)
            res += ' > '
        
        print(res)
