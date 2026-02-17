class Noeud:
    """
    Un Noeud de l'arbre, il a une donnée x associée
    """

    def __init__(self,x:int):
        self.etiquette = x
        
        # Appel au constructeur de la classe Arbre Binaire.
        self.sous_arbre_gauche = Arbre_Binaire()
        self.sous_arbre_droit = Arbre_Binaire()

class Arbre_Binaire:
    """
    Implémentation Objet de la structure de donnée Arbre Binaire.
    """

    def __init__(self):

        # Quand l'arbre est vide racine=None sinon racine=Noeud.
        self.racine = None 

    def est_vide(self):

        return self.racine == None 
    
    def etiquette_racine(self):
        """
        Renvoie une erreur si l'arbre passé en paramètre est vide,
        sinon renvoie l'etiquette de la racine de l'arbre.
        """
        assert not self.est_vide()
        return self.racine.etiquette


    def gauche(self):
        """
        Renvoie une erreur si l'arbre passé en paramètre est vide,
        sinon renvoie le sous arbre gauche de l'arbre.
        """
        assert not self.est_vide()
        return self.racine.sous_arbre_gauche
    
    def droit(self):
        """
        Renvoie une erreur si l'arbre passé en paramètre est vide,
        sinon renvoie le sous arbre droit de l'arbre.
        """
        assert not self.est_vide()
        return self.racine.sous_arbre_droit
    
    def assembler(self, x:int, sous_arbre_gauche:"Arbre_Binaire", sous_arbre_droit:"Arbre_Binaire"):
        """
        Docstring for assembler
        
        :param self: Description
        :param x: Description
        :type x: int
        :param sous_arbre_gauche: Description
        :type sous_arbre_gauche: Arbre_Binaire
        :param sous_arbre_droit: Description
        :type sous_arbre_droit: Arbre_Binaire
        """

        self.racine = Noeud(x)
        self.racine.sous_arbre_gauche = sous_arbre_gauche
        self.racine.sous_arbre_droit = sous_arbre_droit
    
    def hauteur(self):
        if self.est_vide():
            return 0
        else : 
            return 1 + max(self.gauche())

    def afficher(self):
        """
        Docstring for afficher
        """
        pass


# Fonction de test de l'implementation de la structure de donnée arbre binaire.
def test_arbre_binaire():
    """
    On créer l'arbre [7; 2; 10; 1; 5; 8; 3; 6; 9] en assemblant plusieurs sous arbres de bas en haut.
    """
    arbre1 = Arbre_Binaire()
    arbre1.assembler(1, Arbre_Binaire(), Arbre_Binaire())
    arbre3 = Arbre_Binaire()
    arbre3.assembler(3, Arbre_Binaire(), Arbre_Binaire())
    arbre6 = Arbre_Binaire()
    arbre6.assembler(6, Arbre_Binaire(), Arbre_Binaire())
    arbre9 = Arbre_Binaire()
    arbre9.assembler(9, Arbre_Binaire(), Arbre_Binaire())

    arbre5 = Arbre_Binaire()
    arbre5.assembler(5, arbre3, arbre6)
    arbre8 = Arbre_Binaire()
    arbre8.assembler(8, Arbre_Binaire(), arbre9)

    arbre2 = Arbre_Binaire()
    arbre2.assembler(2, arbre1, arbre5)
    arbre10 = Arbre_Binaire()
    arbre10.assembler(10, arbre8, Arbre_Binaire())

    arbre7 = Arbre_Binaire()
    arbre7.assembler(7, arbre2, arbre10)
