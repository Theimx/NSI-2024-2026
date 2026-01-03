#  Liste des 48 sujets de la Banque National des Sujets, accessible
#  librement au public pour le Bac 2025.
#  Sujet complété (10/48): 
#  13, 15, 18, 20, 21, 27, 29, 42, 44, 48 
#
#  Sujet à complété (39/48): 
#
#

# Epreuves Pratiques -BNS 2025- sujet n°1

# Epreuves Pratiques -BNS 2025- sujet n°2

# Epreuves Pratiques -BNS 2025- sujet n°3

# Epreuves Pratiques -BNS 2025- sujet n°4

# Epreuves Pratiques -BNS 2025- sujet n°5

# Epreuves Pratiques -BNS 2025- sujet n°6

# Epreuves Pratiques -BNS 2025- sujet n°7

# Epreuves Pratiques -BNS 2025- sujet n°8

# Epreuves Pratiques -BNS 2025- sujet n°9

# Epreuves Pratiques -BNS 2025- sujet n°10

# Epreuves Pratiques -BNS 2025- sujet n°11

# Epreuves Pratiques -BNS 2025- sujet n°12

# Epreuves Pratiques -BNS 2025- sujet n°13
def recherche13(elt : int,tab : list):

    for i in range(len(tab)):
        if tab[i] == elt:
            return(i)

def insert13(tab,a):
    """ 
    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le 
    nouveau tableau.
    """
    tab_a = [ a ] + tab #nouveau tableau contenant a suivi des éléments de tab

    i = 0
    while i < (len(tab_a)-1) and a > tab_a[i+1] :
        tab_a[i] = tab_a[i+1]
        tab_a[i+1] = a
        i = i + 1
    return tab_a

# Epreuves Pratiques -BNS 2025- sujet n°14

# Epreuves Pratiques -BNS 2025- sujet n°15

def multiplication(n1,n2): 
    res = 0
    if n1 == 0 or n2 == 0:
        return(0)
    elif n1 > 0 and n2 > 0:
        for i in range(n1):
            res += n2
        return(res)
    elif n1 < 0 and n2 < 0:
        n1 = -n1
        for i in range(n1):
            res += -n2
        return(res)
    elif (n1 < 0 and n2 > 0):
        for i in range(-n1):
            res += n2
        return -res
    elif (n1 > 0 and n2 < 0):
        for i in range(-n2):
            res += n1
        return -res

def chercher15(tab,x,i,j):
    '''Renvoie l'indice de x dans tab, si x est dans tab,
       None sinon.
       On suppose que tab est trié dans l'ordre croissant. '''
    if i > j:
        return None 
    m = (i + j) // 2
    if tab[m] < x :
        return chercher15(tab,x,m+1,j)
    elif tab[m] > x:
        return chercher15(tab,x,i,m-1)
    else : 
        return m 
        
# Epreuves Pratiques -BNS 2025- sujet n°16

# Epreuves Pratiques -BNS 2025- sujet n°17

# Epreuves Pratiques -BNS 2025- sujet n°18
def moyenne18(tab):
    somme = 0
    for i in tab:
        somme += i
    return float(somme/len(tab))

def dichotomie18(tab,x):
    """applique une recherche dichotomique pour déterminer
       si x est dans le tableau trié tab.
       La fonction renvoie True si tab contient x et False sinon"""
    
    debut = 0
    fin = len(tab) -1
    while debut <= fin:
        m = (debut + fin ) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m+1
        else :
            fin = m-1
    return False

# Epreuves Pratiques -BNS 2025- sujet n°19

# Epreuves Pratiques -BNS 2025- sujet n°20

def min_et_max(tab):
    res = {
        'min':tab[0],
        'max':tab[0]
    }

    for i in tab: 
        if i > res['max']:
            res['max'] = i 
        if i < res['min'] :
            res['min'] = i 
    return(res)

# Epreuves Pratiques -BNS 2025- sujet n°21 :A refaire
def indices_maxi(tab):
    maxi = tab[0]
    for x in tab:
        if x > maxi:
            maxi = x
    indices = []
    for i in range(len(tab)-1):
        if tab[i] == maxi:
            indices.append(i)

    return((maxi,indices))

def renverse(pile):
    ''' renvoie une pile contenant les mêmes éléments que pile,
        mais dans l'ordre inverse. 
        Cette fonction détruit pile. '''
    pile_inverse = []
    while pile != []:
        pile_inverse.append(pile.pop())

    return(pile_inverse) 

def positifs(pile):
    '''renvoie une pile contenant les mêmes éléments positifs de pile,
    dans le même ordre.Cette fonction détruit pile. '''
    pile_positifs = []
    while pile != []: 
        x = pile.pop()
        if x >= 0:
            pile_positifs.append(x)

    return reverse(pile_positifs)
       
# Epreuves Pratiques -BNS 2025- sujet n°22

# Epreuves Pratiques -BNS 2025- sujet n°23

# Epreuves Pratiques -BNS 2025- sujet n°24

# Epreuves Pratiques -BNS 2025- sujet n°25

# Epreuves Pratiques -BNS 2025- sujet n°26

# Epreuves Pratiques -BNS 2025- sujet n°27

# Epreuves Pratiques -BNS 2025- sujet n°27
def verifie27(tab):
    for i in range(1,len(tab)-1,1):
        if tab[i-1] > tab[i]:
            return False
    return True

def depouille27(urne):
    """Prend en paramètre une liste de suffrages et renvoie un 
    dictionnaire avec le nombre de voix pour chaque candidat"""
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else :
            resultat[bulletin] = 1
    return resultat

def vainqueurs27(election):
    """prend en paramètre un dictionnaire non vide avec le nombre de voix
       pour chaque candidat et renvoie la liste des vainqueurs """
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax : 
            nmax = election[candidat]
    liste_finale = [nom for nom in election if (election[nom]==nmax)]
    
    return liste_finale

# Epreuves Pratiques -BNS 2025- sujet n°28

# Epreuves Pratiques -BNS 2025- sujet n°29

def selection_enclos(tab,num_enclos):
    res = []
    for i in range(len(tab)):
        if tab[i]['enclos'] == num_enclos:
            res.append(tab[i])
    return res

def trouver_intrus(tab,g,d):
    """Renvoie la valeur de l'intrus situé entre les indices g et d
       dans le tableau tab ou : 
       tab verifie les conditions de l'exercice,
       g et d sont des multiples de 3."""
    if g == d:
        return tab[g]
    else : 
        nombre_de_triplets = (d - g) // 3
        indice = g + 3 * (nombre_de_triplet) 
        if ... :
            return ...
        else : 
            return ...

# Epreuves Pratiques -BNS 2025- sujet n°30

# Epreuves Pratiques -BNS 2025- sujet n°31

# Epreuves Pratiques -BNS 2025- sujet n°32

# Epreuves Pratiques -BNS 2025- sujet n°33

# Epreuves Pratiques -BNS 2025- sujet n°34

# Epreuves Pratiques -BNS 2025- sujet n°35
def max_dico35(dico): 
    
    key1 = ''
    res2 = -1
    for x in dico.items():
        if x[1] > res2 : 
            key1 = x[0]
            res2 = x[1]

    return (key1,res2)

# Epreuves Pratiques -BNS 2025- sujet n°36

# Epreuves Pratiques -BNS 2025- sujet n°37

# Epreuves Pratiques -BNS 2025- sujet n°38

# Epreuves Pratiques -BNS 2025- sujet n°39

# Epreuves Pratiques -BNS 2025- sujet n°40

# Epreuves Pratiques -BNS 2025- sujet n°41

# Epreuves Pratiques -BNS 2025- sujet n°42 
def nb_repetions42(elt,tab):
    if tab :
        count = 0 
        for x in tab:   #Parcours séquentiel de la liste
            if elt == x:
                count += 1 
        return(count)
    return()

def binaire42(a):
    """convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de charactères."""
    if a == 0:
        return '0'
    bin_a = ""
    while a > 0:
        bin_a = str(a%2) + bin_a
        a = a//2
    return bin_a

# Epreuves Pratiques -BNS 2025- sujet n°43 

# Epreuves Pratiques -BNS 2025- sujet n°44
def moyenne44(tab):
    note,coef = 0,0
    for i in range(len(tab)):
        note += tab[i][0] * tab[i][1]
        coef += tab[i][1]
    return(note/coef)

def affiche(dessin):
    ''' affichage d'une grille : les 1 sont représentés par 
        un "*" , les 0 par un espace " ". '''
    for ligne in dessin:
        affichage = ''
        for col in ligne:
            if col == 1:
                affichage = affichage + "*"
            else :
                affichage = affichage + " "
        print(affichage)

def liste_zoom(liste_depart,k):
    ''' renvoie une liste contenant k fois chaque élément de 
        liste_depart '''
    liste_zoomee = []
    for elt in range(len(liste_depart)) : 
        for i in range(k):
            liste_zoomee.append(liste_depart[elt])
    return liste_zoomee

def dessin_zoom(grille,k):
    '''renvoie une grille ou les lignes sont zoomées k fois 
       ET répétées k fois'''
    grille_zoomee = []
    for ligne in grille:
        ligne_zoomee = liste_zoom(ligne,k)
        for i in range(k):
            grille_zoomee.append(ligne_zoomee)
    return grille_zoomee

# Epreuves Pratiques -BNS 2025- sujet n°45

# Epreuves Pratiques -BNS 2025- sujet n°46

# Epreuves Pratiques -BNS 2025- sujet n°47

# Epreuves Pratiques -BNS 2025- sujet n°48
def recherche48(tab,n):
    for i in range((len(tab)-1),0,-1): # Parcourirs la liste depuis la fin a la recherche 
        print(i)                       # de notre  valeur et renvoyer son indice.
        if n == tab[i]:
            return(i)

def distance_carre48(point1,point2):
    """ Calcule et renvoie la distance au carre entre 
        deux points."""
    return( (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 )

def point_le_plus_proche48(depart,tab):
    """ Renvoie les coordonnées du premier point du tableau tab se
    trouvant à la plus courte distance du point depart."""
    
    min_point = tab[0]
    min_dist = distance_carre48(tab[0],depart)
    for i in range(1,len(tab)):
        if distance_carre48(tab[i],depart) < min_dist : 
            min_point = tab[i]
            min_dist = distance_carre48(tab[i],depart)

    return min_point
