class Noeud:
    """
    Docstring for Noeud
    """

    def __init__(self,x:int):
        self.etiquette = x
        
        # Appel au constructeur de la classe Arbre Binaire.
        self.sous_arbre_gauche = Arbre_Binaire()
        self.sous_arbre_droit = Arbre_Binaire()

class Arbre_Binaire:
    """
    Docstring for Arbre_Binaire
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

    def afficher(self):
        """
        Docstring for afficher
        """
        pass

