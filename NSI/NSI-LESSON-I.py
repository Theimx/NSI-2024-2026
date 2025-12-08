import random
import math

# ---------- - -    LES NOMBRES DE 1 A 20 DANS PLUSIEURS BASES : - - ---------------------------------------------------------------------------------------------------------
#Base 2 (Binaire) : 0000, 0001, 0010, 0011, 0100, 0101, 0110, 0111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111, 0001 0000, 0001 0001, 0001 0010, 0001 0011
#Base 10 (Décimal) : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
#Base 16 (Héxadécimal) : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F, 10, 11, 12, 13
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 1ère spé NSI


def COURS_Introduction():

    # Histoire de l'informatique : 

    # - 1. Augusta Ada King, comtesse de Lovelace (1815-1852): a conçu le premier algorithme destiné à
    #      être exécuté par une machine, en 1842-1843, dans ses notes sur la machine analytique de Charles Babbage.    
    # - 2. Alan Mathison Turing (1912-1954): 1936 construit mathématiquement la première machine universelle
    # - 3. John Von Neumann (1903-1957): 1944 Architecture de von Neumann 

    # - «Informatique», mot-valise né de la contraction des mots «Information» et «Automatique».
    # - 1971 : microprocesseur 4004 d'Intel,il développe des performanceséquivalents à celle de l'ENIAC (1946),
    #   qui occupait toute une pièce.

    #------------------ - -   Architecture de Von Neuman   - - ---------------------------------------------------------------------------------------------------------------

    # - 1. l'unité arithmétique et logique (UAL) ou unité de traitement, qui effectue les opérations de base.
    # - 2. l'unité de contrôle, qui est chargée du séquençage des opérations.
    # - 3. la mémoire, qui contient à la fois les données et le programme qui indique à l'unité de contrôle quels
    #      calculs faire sur ces données. La mémoire se divise en mémoire vive (programmes et données en cours de
    #      fonctionnement) et mémoire de masse (programmes et données de base de la machine).
    # - 4. les dispositifs d'entrée-sortie, qui permettent de communiquer avec le monde extérieur.

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    return 0

def COURS_Architecture_Materiel_I():

    #I. Les composants de base d’un ordinateur :

    # - 1. Le processeur (ou microprocesseur) :
    #      Il execute les programmes, il est fait de milliards de Transitors et est cadencé par une horloge.  
    #      Frequence : s'exprime en Hertz (Hz) Taille des données : 32 ou 64 bits
    # - 2. La mémoire vive :
    #      Elle est constituée de plusieurs milliards de circuits mémoires,Ces circuits sont regroupés en agrégats de 8, 16, 32, 64
    #      bits (ou davantage) que l’on appelle des cases mémoires.Elles ont des adresses.
    #      RAM = Random Acces Memory car On peut accéder directement à une donnée stockée dans une case mémoire à l’aide de son adresse.
    # - 3. Le bus:
    #      Le processeur, la mémoire et les périphériques sont reliés un canal appelé bus de communication.
    #      le bus de données qui permet l’échanger des données entre le processeur et la mémoire.
    #      le bus d’adresses qui permet d’accéder à une case mémoire. La carte mère joue le rôle de bus.      

    #II. Jeu d’instruction et programmes :

    # - 1. Le processeur d’un ordinateur possède une unité de contrôle et une unité de calcul.
    #      L’unité de contrôle est chargée de lire les programmes enregistrés dans la mémoire et de fournir à l’unité de
    #      calcul la séquence d’instructions à exécuter. Le processeur et la mémoire sont reliés par un bus d’adresses et
    #      un bus de données.
    #      La mémoire peut contenir des milliards de cases mémoire. Elle contient les données et les programmes.
    #      Le processeur possède un très petit nombre de cases mémoires à accès très rapide, appelées registres. Ces
    #      registres peuvent contenir des données ou des adresses.
    # - 2. Un processeur est associé à un jeu d’instructions,une instruction possède un code et un paramètre,
    #      occupe un nombre fixe de cases mémoire, il doit permettre par exemple d’effectuer les tâches suivantes :
    #      - Charger une donnée dans un registre.
    #      - Écrire dans une certaine case mémoire une donnée située dans un registre.
    #      - Faire un calcul (logique ou arithmétique) avec les données contenues dans les registres
    #      - Aller à une instruction située à une certaine adresse (branchement).
    #      - Aller à une instruction située à une certaine adresse si A contient zéro ou passer à l’instruction 
    #        suivante dans le cas contraire (branchement conditionnel).

    #III. L’organisation de la mémoire :

    # - 1. Les types de mémoire : On parle de mémoire vive quand le contenu est perdu lorsque 
    #      le courant est coupé :il s’agit des registres, des mémoires cache, de la mémoire centrale.
    #      la ROM (Read Only Memory) qui, comme son nom l’indique, ne fonctionne en principe qu’en lecture seule.
    # - 2. Un registre est un emplacement mémoire interne au processeur pour stocker des opérandes
    #      et des résultats intermédiaires lors des opérations effectuées dans l’UAL notamment.
    #      À noter que la plupart des PC actuels ont des registres de taille 64 bits.
    # - 3. Mémoires centrales et mémoire cache,La mémoire centrale est une mémoire volatile qui contient 
    #      les programmes en cours et les données qu’ils manipulent.Elle est organisée en cellules qui
    #      contiennent chacune une donnée ou une instruction repérées par un entier : une adresse mémoire.
    #      Pour pouvoir adapter la très grande vitesse du processeur à celle plus faible de la mémoire centrale,
    #      on place entre eux une mémoire plus rapide, la mémoire cache, qui contient les instructions et données
    #      en cours d’utilisation car, la plupart du temps,les données qui viennent d’être utilisées ont une probabilité plus grande d’être réutilisées que d’autres.

    return 0

def COURS_Language_de_Programmation_II():

    return 0

def COURS_Représentation_des_Données_III():

    return 0

def COURS_Type_Construit_IV():

    return 0

def COURS_Algorithme_Avancés_V():

    return 0

def COURS_Algorithme_Avancés_et_IA_VI():

    return 0

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Une fonction pour calculer une moyenne Général avec plusieurs coeficients 
def moyenne_Bac(_note1,_note2,_note3,_coef1,_coef2,_coef3):

    _moyenneG = 0
    _coefG = 0 
    _moyenneG = _moyenneG + _note1 * _coef1
    _coefG += _coef1
    _moyenneG = _moyenneG + _note2 * _coef2 
    _coefG += _coef2 
    _moyenneG = _moyenneG + _note3 * _coef3 
    _coefG += _coef3 

    _bac = _moyenneG /_coefG

    return _bac

#Une fonction pour calculer une moyenne de maths avec deux coeficients prédéfinis
def moyenne_math2(_note1,_note2,_note3,_note4,_note5):
    _math = (((_note1+_note2+_note3) / 3) + ((_note4+_note4+_note5+_note5)) / 4) /2

    return _math

#Une fonction pour appliquer la TVA sur un produit à partir du prix de base et du % de la TVA
def TVA(_prix,_tva):
    _newPrice = float(_prix) * (1 + _tva/100)

    return _newPrice

#Une fonction pour connaitre son appréciation au Bac 
def bach(_note):
    _Bac = float(note)

    if _Bac <= 7.99:
        print("Refusé")
    elif _Bac >= 8 and _Bac <= 9.99 : 
        print("Ratrapage")
    elif _Bac >= 10 and _Bac <= 11.99:
        print("Bac sans mention")
    elif _Bac >= 12 and _Bac <= 13.99:
        print("Mention Assez bien")
    elif _Bac >= 14 and _Bac <= 15.99:
        print("Bien ")
    elif _Bac >= 16 and _Bac <= 17.99:
        print("Très bien")
    elif _Bac >= 18 and _Bac <= 21:
        print("Felicitation")

    else : 
        print("non")

#Une fonction qui permet de determiner si l'utilisateur peut consommer de l'alcool grâce au structures conditionelles 
def alcool():

    _enceinte = False
    _age = int(input("entrez votre age: "))

    _sexe_femme = input("si vous êtes une femme entrez : oui : ")
    if _sexe_femme == "oui":
        _sexe_femme = True

    if _sexe_femme == True:
        _enceinte = input("si vous êtes enceinte écrivez : oui: ")
    if _enceinte == "oui":
        _enceinte = True


    if _age <= 17.99 : 
        print("non trop petit")

    if _sexe_femme == True and _enceinte == True:
        print("non pas bon pour le bébé")
    if _age >= 18 and _enceinte != True :
        print("oui c'est bon")
        
#Une fonction pour calculer l'évolution de la valeur d'une maison sur 15 ans
def InflationMaison15():
    _prix_base = 206000
    _nb_années = 15
    _inflations = 1 + (3/100)

    for i in range (_nb_années):
        print(_prix_base * _inflations)   
        _prix_base = _prix_base * _inflations
    return _prix_base

#Une fonction pour calculer l'évolution de la valeur d'une maison après un certains nombre d'années
def InflationMaison(_valeur, _année):
    _prix_base = _valeur
    _nb_années = _année
    _inflations = 1 + (3/100)

    for i in range (_nb_années):
        print(_prix_base * _inflations)   
        _prix_base = _prix_base * _inflations
    return _prix_base

#Une fonction qui retourne la longueur d'une chaine de caractère donnée
def lenght(_chaine):
    _chaine = str(_chaine)
    _lenght = 0
    for i in _chaine:
        _lenght += 1

    return(_lenght)

#exo cours 28/11/2024
#Une fonction pour afficher tout les chiffres de 1 a 100
def hundred():
    for i in range(101):
        print(i)

#Une fonction pour afficher toute les secondes,minutes et heures d'une journée
def hour():
    for b in range(24):
        for a in range(60):
            for i in range(60):
                print("h",b,"m",a,"s",i)

#Une fonction qui permet d'afficher tout les jours de la semaine sur une durée de 4 semaines
def week():
    for a in range(4):
        for i in range(7):
            if i == 0:
                print("jour", i+1, "semaine" ,a+1, "donc Samedi")
            if i == 1:
                print("jour", i+1, "semaine" ,a+1,"donc Dimanche")
            if i == 2:
                print("jour", i+1, "semaine" ,a+1,"donc Lundi")
            if i == 3:
                print("jour", i+1, "semaine" ,a+1,"donc Mardi")
            if i == 4:
                print("jour", i+1, "semaine" ,a+1,"donc Mercredi")
            if i == 5:
                print("jour", i+1, "semaine" ,a+1,"donc Jeudi")
            if i == 6:
                print("jour", i+1, "semaine" ,a+1,"donc Vendredi")

#Exo cours 4/12/2024 : Boucle Borné et non Borné
#Une fonction qui permet de detecter toute les voyelles d'une chaine de caractère fournis
def voyelleDansMot(_mots):

    for i in _mots:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "y" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U" or i == "Y":
            print("voyelle :" + i )
        else : 
            print("autres : " + i )

    #faut parcourir des choses avec les boucles for

#Une fonction qui permet de demander a un utilisateur de resoudre le calcul 5 fois 6 (exercice de cours)
def tableMultiplication():
    _reponse = 0
    _chiffre1 = 5
    _chiffre2 = 6
    while _reponse != _chiffre1 * _chiffre2 : 
        _reponse = int(input("combien fond 5 fois 6 ?"))
    print("gg")

#Une fonction qui permet de se tester sur ses tables de multiplications
def tableMultiplicationRandom():
    _rejouer = "oui"

    while _rejouer == "oui":
        _reponse = 0
        _chiffre1 = random.randint(1,9)
        _chiffre2 = random.randint(1,9)
        _question = "combien fond " + str(_chiffre1) + " fois " + str(_chiffre2) + " ?  "
        while _reponse != _chiffre1 * _chiffre2 : 

            _reponse = int(input(_question))
        print("Bravo")
        _rejouer = input("Ecrivez oui si vous voulez rejouer : ")

#Une fonction qui permet de créer un numéro de sécurité social unique a partir d'information entré par l'utilisateur.
def carteVital():
    _sexe = int(input("entrez : 1 si vous êtes un Garçon ou 2  si vous êtes une fille : "))

    if _sexe == 1 or _sexe == 2 : 
        _annaissance = int(input("entrez les deux derniers chiffres de votre année de naissance (ex 07) : "))

        if _annaissance < 99 or _annaissance > 0:
            _moisnaissance = int(input("entrez votre mois de naissance (ex 05) : "))

            if _moisnaissance <= 12 or _moisnaissance >= 1:
                _departement = int(input("entrez le numero de votre departement de naissance ou 99 si vous êtes née a l'etranger : "))

                if _departement < 99 or _departement > 0:

                    _code1 = random.randint(100,999)
                    _code2 = random.randint(100,999)
                    if _annaissance <= 9 : 
                        _annaissance = '0' + str(_annaissance)
                    if _moisnaissance <= 9 : 
                        _moisnaissance = '0' + str(_moisnaissance)
                    if _departement <= 9 : 
                        _departement = '0' + str(_departement)

                    _securiteSocial = str(_sexe)  + str(_annaissance)  + str(_moisnaissance) + str(_departement)  + str(_code1) + str(_code2)
                    int(_securiteSocial)
                    print(_securiteSocial)

                    _securiteSocial = int(_securiteSocial)
                    return _securiteSocial
                else : 
                    cartevital()
            else : 
                cartevital()
        else : 
            cartevital()
    else : 
        cartevital()

#A refaire avec les boucles while, Refaire une version optimisé de celle du dessus et coder La fonction 
#inverse (A partir d'un numéro de carte, renvoyer une liste d'information deduis de celui ci.)
def carteVitalBoucle(): 
    _result = 0
    return _result

#Cette fonction devra permettre a partir d'un numéro de carte vital, d'en obtenir des informations
def carteVitalAnalyse(_num):
    _num = int(_num)
    return 0

#Exercice de cours : Stocké le nom des élèves de la classe
def NomClasse(_nbPerson):
    _nbPerson = int(_nbPerson)
    eleve = []
    for i in range(_nbPerson):
        eleve.append(input("Entre le nom des élèves : "))
    return eleve

#Exercice de cours : Afficher les signes du zodiac simplement 
def Zodiac():
    _signe = ["Belier","Taureau","Poisson","Sagitaire","Balance","Cancer","Cappricorne","Scorpion","Versau","Germea","Lion","Vierge"]
    for i in _signe :
        print(i)

#Exercice du Devoir commun de spé NSI, la suite de Fibonacci
def fib(n):
    a = 0
    b = 1
    for i in range(1, n + 1):
        if i % 2 != 0:
            c = a + b
            a = c
        else:
            c = a + b
            b = c

#Exercice cours liste : Faire la somme des eentier d'une liste donné
def sommeEntierListe(l):
    total = 0
    for i in l:
        total += i
    return(total)

#Detectez une occurence dans une liste sans la fonction count
def occurence():
    maListe = ["Soleil","Mordor","Citron","Arche","soleil","Grenouille","Livre","Citron"]
    bufferList = maListe

    for i, motListeA in enumerate(maListe):
        for j, motListeB in enumerate(bufferList):
            if i != j:
                if motListeA == motListeB:
                     return (True,motListeA )

    return False

#Difference entre A et a Table ASCII : 32
#Detectez une occurence dans une liste sans la fonction count et sans difference entre Minuscule et Majuscule 
def occurenceV2():

    maListe = ["Soleil","Mordor","Citron","Arche","soleil","Grenouille","Livre","Citron"]
    bufferList = maListe

    for i, motListeA in enumerate(maListe):
        for j, motListeB in enumerate(bufferList):
            if i != j:
                if str.lower(motListeA) == str.lower(motListeB):
                     return (True,motListeA )

    return False

#Une fonction qui fait la moyenne des éléments d'une liste 
def MedianListe(l): 
    total = 0
    upper = 0
    under = 0
    underList = []
    for i in l:
        total += i
        if i >= 9.99 : 
            upper += 1
        elif i < 10 :
            under += 1
            underList.append(i)
    return( (total / len(l)),"Au dessus de 10 : " + str(upper), "En dessous de 10 : " + str(under),underList)

#renvoie la plus Grande et la plus petite valeur d'une liste 
def plusGrandPlusPetit(l):
    under = l[0]
    upper = l[0]
    for i in l:
        if i < under:
            under = i
        if i > upper: 
            upper = i
    return(under,upper)

#Exo de cours : detecter si une liste est un Palindrome ou non 
#utiliser le pas négatif
def isPalindrome(chaine):
    n = len(chaine)
    for i in range(n // 2):
        if chaine[i] != chaine[n - 1 - i]:
            return False
    return True

#Une fonction pour obtenir la taille d'un tableau de tableau
def lent(tab):
    total = 0
    for i in range(0,len(tab)):
        total += len(tab[i])
    print(total)
#lent([[1,2,3],[4,5,6],[7,8,9]])

def TestImbriquation():
    lst = [(4,7), (3, -4,5), (6, (8,9.2))]
    print(lst[2][1][1]) # renvoie la valuer 9.2

def compr():
    # Affiche tout les chiffres pairs entre 0 et 100
    compr = [i for i in range(0,100,2)]
    #print(compr)

    # Affiche les 100 premières puissances de 2
    compr2 = [2**i for i in range(100)]
    #print(compr2)

    # Affiche tout les carré entre 1 et 50 qui se finnisse pars 9
    compr3 = [i**2 for i in range(2,51) if (i**2) % 10 == 9 ]
    #print(compr3)
    
# Découper une grande chaîne en fragments de 5 caractères chacun. Rassemblez ces morceaux
# dans l'ordre inverse. La chaîne doit pouvoir contenir des caractères accentués.

def exo10_2(_chaine):
    double = []
    index = 0
    index2 = 5
    result = ""

    for i in range((len(_chaine)//5) +1):

        current_str = ""
        current_str += _chaine[index:index2]
        index += 5
        index2 += 5
        double.append(current_str)
        
    result = result.join(double[::-1])

    return(result)

def exo10_3(_chaine):
    double = []
    result = ""
    for i in range(0, len(_chaine), 5):
        current_str = _chaine[i:i+5]  
        double.append(current_str)  

    return result.join(double[::-1])

#print(exo10_2("Cette phrase seras mélangée"))
#print(exo10_3("Cette phrase seras mélangée"))

# Il est possible d’écrire un algorithme dans une fonction qui permet le renvoie de la moyenne
# d’âge, arrondie à l’entier inférieur, d’une liste de personne.
def Calcul_de_moyenne(tab):
    result = 0
    for i in range(len(tab)):
        result += tab[i][1]

    return(result//len(tab))
#print(Calcul_de_moyenne([("Wiliam",16),("Yanis",18),("Mathéo",21),("Jean",42)]) )

#Voici une fonction qui compte le nombre de personnes d’une liste qui ont plus de 18 ans (majeur).
def majeur_test(tab): 
    count = 0 
    for i in range(len(tab)) : 
        if tab[i][1] >= 18 :
            count += 1 
    return(count)
#print(majeur_test([("Wiliam",16),("Yanis",18),("Mathéo",21),("Jean",42)]))

def older(tab): 
    count = ''
    maxi = tab[0][1]
    for i in range(len(tab)) : 
        if tab[i][1] >= maxi :
            count = tab[i][0]
            maxi = tab[i][1]
    return(count)
#print(older([("Wiliam",16),("Yanis",18),("Mathéo",21),("Jean",42)]))

def dicoto(tab,x):
    if tab :
        tab.sort()
        indice = (len(tab)//2)
        
        while True:
            if tab[indice] == x :
                return True
            elif tab[indice] > x :
                indice = indice//2
                
            elif tab[indice] < x :
                indice = (indice + len(tab))//2
                
    return False 

testab = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] 
testx = 9
#print(dicoto(testab,testx))

def correction(tab,x):
    indD = 0
    indF = len(tab) -1

    while indD <= indF : 
        ind_M =(indD + indF) // 2
        MiD = tab[ind_M]
        if MiD == x :
            return True
        elif MiD < x :
            indD = ind_M +1
        else:
             indF = ind_M -1
    return False
#print(correction(testab,testx))

def  insertion(tab):
    temp = 0

    for i in range (len(tab)*4) :
        
        for i in range(len(tab)-1):
            if tab[i] > tab[i+1]:
                print("oui")
                temp = tab[i+1]
                tab[i+1] = tab[i]
                tab[i] = temp

     

#testab = [100,90,40,79,48,10,173,478] 
def insertion2(tab):
    for i in range(1,len(tab)):
        j = i
        print("+ 1")
        while j>0 and tab[j] < tab[j-1]:
            tab[j],tab[j-1] = tab[j-1],tab[j]
            j -= 1
            print("+ 1")
#insertion2(testab)
#print(testab)   

def selection(tab):
    count = 0  
    temp = 0
    for j in tab:
        if j <= mini:
            mini = j
    for i in range(0,len(tab)):
        
        for j in tab:
            if j <= tab[count]:
                mini = j

        temp = tab[count]
        tab[count] = mini
        count += 1

def correctionSelection(tab): 
    for i in range(0,len(tab)-1):
        Mini = i 
        for j in range(i+1,len(tab)) :
            if tab[j] < tab[Mini] :
                Mini = j 
        tab[i],tab[Mini] = tab[Mini],tab[i]

# test = [100,90,40,79,48,10,173,478]
# print(test)
# print(correctionSelection(test))
# print(test)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#   Glossaire : 
# - ROM = Read Only Memory
# - RAM = Random Acces Memory
# - BIOS = Basic Input/Ouput System : qui est le premier programme exécuté au démarrage de l’ordinateur.
# - SSD = Solid State Drive
# - bash = Bourne Again Shell

#  Commande Bash :  Description :
#  - ls    : Lister le contenu du répertoire courant
#  - cp    : Copier des fichiers ou des répertoires 
#  - mv    : Déplacer ou renommer des fichiers ou des répertoires
#  - rm    : Effacer des fichiers ou des répertoires
#  - cd    : Se déplacer dans l’arborescence
#  - cat   : Visualiser le contenu d’un fichier
#  - echo  : Afficher un message ou le contenu d’une variable
#  - touch : Réinitialiser le timestamp d’un fichier ou créer un fichier vide

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Assembleur :

# LDR R1,78      : Place la valeur stockée de la cellule mémoire 78 dans le registre R1
# STR R3,125     : Place la valeur stockée du registre R3 dans la cellule mémoire 125
# ADD R1,R0,#128 : Additionne la valeur « 128 » avec la valeur stockée de R0 et stocke le résultat dans le registre R1
# ADD R0,R1,R2   : Additionne les valeurs stockées des registres R2 et R1 et stocke le résultat dans le registre R0
# SUB R1,R0,#128 : Soustrait la valeur « 128 » avec la valeur stockée de R0 et stocke le résultat dans le registre R1
# SUB R0,R1,R2   : Soustrait la valeur stockée du registre R2 avec la valeur du registre R1 et stocke le résultat dans le registre R0
# MOV R1, #23    : Place la valeur « 23 » dans le registre R1
# MOV R0, R3     : Place la valeur stockée du registre R3 dans le registre R0

# CMP R0, #23    : Si la valeur stockée dans R0 est égale à « 23 » alors j’exécute ce qui se
# BEQ repereA      trouve dans le label « repereA »

# CMP R0, #23    : Si la valeur stockée dans R0 n’est pas égale à « 23 » alors j’exécute ce qui
# BNE repereA      se trouve dans le label « repereA »

# CMP R0, #23    : Si la valeur stockée dans R0 est plus grande que « 23 » alors j’exécute ce
# BGT repereA      qui se trouve dans le label « repereA »

# CMP R0, #23    : Si la valeur stockée dans R0 est plus petite que « 23 » alors j’exécute ce qui
# BLT repereA      se trouve dans le label « repereA »

# B repereA      : Passer directement à la partie du label « repereA » du programme
# HALT           : Arrête l’exécution du programme
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#   Convention d'écriture : 
#   Les variables dans les focntions : 
#   Les noms de variable : 

# Héxadécimal :     -217
# Décimal :         -535
# Binaire :         -0000 0010 0001 0111
# Signé :            1000 0010 0001 0111
# Complément à 1 :   1111 1101 1110 1000
# Complement à 2 :   1111 1101 1110 1001

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Fiche pour le Bac NSI 2024-2026 :
#   - Fiche sur l'Assembleur                             ☑
#   - Fiche sur les bases binaires, décimal, héxadécimal ☐ 
#   - Fiche sur la table ASCII                           ☐