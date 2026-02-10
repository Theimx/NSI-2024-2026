# ------------------
#  SUJETS ZERO (0/3)
# ------------------

#----------------------------------------------------------------------------------------------
# Sujet 1 : determine si une année est bissextile ou non. (Prend un entier, renvoie un Bool)
def est_bissextile(annee):
    return (annee % 4 == 0) and (annee%100 != 0)  or (annee%400 ==0)

# print(est_bissextile(2026)) --> False
# print(est_bissextile(2024)) --> True
# print(est_bissextile(2100)) --> False
# print(est_bissextile(2000)) --> True

def est_bissextil_variante(annee):
    if (annee % 400 == 0):
        return True
    elif (annee % 100 == 0):
        return False
    elif (annee % 4 == 0):
        return True
    else :
        return False

# print(est_bissextil_variante(2024)) --> True
# print(est_bissextil_variante(2100)) --> False
# print(est_bissextil_variante(2000)) --> True
# print(est_bissextil_variante(2026)) --> False

# Exercice 2 : determine une phase (int) a partir d'un jour (int) donné (entre 1 et 28).
def determiner_phase(day):
    assert (day <= 28) and (day >= 1), "mauvais domaine de definition"
    if (day <= 5) and (day >= 1) : 
        return 1

    elif (day <= 13) and (day >= 6) :
        return 2

    elif day == 14 : 
        return 3
    else : 
        return 4
# print(determiner_phase(1))   --> 1
# print(determiner_phase(7))   --> 2
# print(determiner_phase(14))  --> 3
# print(determiner_phase(17))  --> 4
# print(determiner_phase(100)) --> AssertionError: mauvais domaine de definition

# Exercice 3 : jours dans mois : A completer et a corriger
def Exercice3():
    def jours_dans_mois(annee, mois):
        """Renvoie le nombre de jours dans un mois donné d'une année donnée.
        Utilise le module calendar pour gérer les années bissextiles."""
        if mois == 2:  # février
            return 29 if est_bissextile(annee) else 28
        elif mois in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        else:
            return 30

    def ajouter_jours(date, nb_jours):
        """Ajoute nb_jours à une date donnée et renvoie la nouvelle date.
        La date est représentée par un tuple (jour, mois, année)."""
        jour, mois, annee = date
        jour = jour + nb_jours

        # Ajustement du jour et du mois si dépassement
        while jour > jours_dans_mois(annee, mois):
            jour = jour - jours_dans_mois(annee, mois)
            mois = mois + 1
            if mois > 12:  # passage à l'année suivante
                mois = 1
                annee = annee + 1

        return (jour, mois, annee)

    def test_ajouter_jours():
        assert ajouter_jours((7, 9, 2025), 3) == (10, 9, 2025)
        assert ajouter_jours((7, 9, 2025), 0) == (7, 9, 2025)
        assert ajouter_jours((7, 9, 2025), 30) == (7, 10, 2025)
        assert ajouter_jours((7, 9, 2025), 365) == (7, 9, 2026)

#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#Sujet 2 : 

import donnees
import donnees_completes
from math import sqrt

def salaire_moyen_condition(employes, champ, valeur):
    '''Renvoie le salaire moyen des employes ayant val comme valeur associée
    au champ donné en argument.
    Si le nombre d'employés considéré est nul, cette fonction renvoie None'''
    somme = 0
    compteur = 0

    for c in employes:
        #print(c[champ])
        #print(somme, compteur)
        if c[champ] == valeur :
            compteur += 1
            somme += c['salaire']

    if compteur != 0 :
        return somme/compteur
#print("Salaire moyen femme : ",salaire_moyen_condition(donnees_completes.employes, "sexe", "F"))
#print("Salaire moyen homme : ",salaire_moyen_condition(donnees_completes.employes, "sexe", "M"))


def test_salaire_moyen_condition():
    e = donnees.employes
    assert salaire_moyen_condition([], 'sexe', 'F') == None
    assert salaire_moyen_condition(e, 'sexe', 'F') == 2400.0
    assert salaire_moyen_condition(e, 'etudes', 3) == 2550.0
    assert salaire_moyen_condition(e, 'etudes', 12) == None

#test_salaire_moyen_condition()

def effectif_par_sexe(employes):
    '''Renvoie un dictionnaire ayant deux clés 'F' et 'M'
    associée respectivement au nombre d'employées femmes et au
    nombre d'employés hommes dans les données en arguments.'''
    res = {
        "M" : 0,
        "F" : 0
           }

    for c in employes:
        if c["sexe"] == "F":
            res["F"] += 1
        elif c["sexe"] == "M":
            res["M"] += 1
    return res

#print(effectif_par_sexe(donnees.employes))

def test_effectif_par_sexe():
    e = donnees.employes
    assert effectif_par_sexe(e) == { 'F' : 3, 'M' : 3 }

#test_effectif_par_sexe()

def calcul_ecart_sexe(employes):
    '''Renvoie l'écart de salaire en pourcentage pour les femmes
    par rapport aux hommes'''
    moy_h = salaire_moyen_condition(donnees.employes, 'sexe', 'M')
    moy_f = salaire_moyen_condition(donnees.employes, 'sexe', 'F')
    #return moy_h - moy_f

    if moy_f == None or moy_h == None :
        return None
    return (moy_h - moy_f) / moy_h * 100

#print(calcul_ecart_sexe(donnees.employes))
# Attribution d'un premier salaire après embauche par les k plus proches voisins

def sexe_vers_entier(e):
    if e['sexe'] == 'F':
        return 1
    else:
        return 1

def distance(e1, e2):
    '''Renvoie la mesure de distance entre deux personnes.'''
    s = 0
    s = s + (sexe_vers_entier(e1) - sexe_vers_entier(e2))**2
    s = s + (e1['experience'] - e2['experience'])**2
    s = s + (e1['etudes'] - e2['etudes'])**2
    return sqrt(s)

def k_plus_proches(k, employes, e):
    '''Renvoie les k employes les plus proches de e par la
    distance définie au dessus.'''
    e_d = [(distance(e, employes[i]), i) for i in range(len(employes))]
    e_d.sort() # va trier en premier sur la distance
    voisins = []
    for i in range(k):
        voisins.append(employes[e_d[i][1]])
    return voisins

def salaire_moyen(employes):
    '''Renvoie le salaire moyen pour une liste d'employes'''
    if len(employes) == 0:
        return None
    s = sum(e['salaire'] for e in employes)
    return s/len(employes)

def salaire_par_proximite(employes, e):
    '''Prend en entrée une liste d'employés et un dictionnaire comportant
    les champs experience, etudes et sexe et renvoie le salaire le plus
    proche en moyennant les 3 plus proches voisins'''
    voisins = k_plus_proches(3, employes, e)
    return salaire_moyen(voisins)

#print(salaire_par_proximite(donnees.employes,{'experience':3, 'etudes':3,'sexe':'F'}))
#print(salaire_par_proximite(donnees.employes,{'experience':3, 'etudes':3,'sexe':'M'}))

#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------