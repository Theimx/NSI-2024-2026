
#
#
#

# -------------------------------------------------------------
# A.Sujet-Amérique-du-nord-journée 1-2022-Exercice-4 (4 points)
# -------------------------------------------------------------

# --------------------------------------------------------------
# B.Sujet-Centres-étrangers-journée-2-2022-Exercice-1 (4 points)
# --------------------------------------------------------------

# --------------------------------------------------------------
# C.Sujet-Centres-étrangers-journée-2-2022-Exercice-2 (4 points)
# --------------------------------------------------------------

# ---------------------------------------
# D.Sujet-zéro-2021-Exercice-2 (4 points)
# ---------------------------------------

# ---------------------------------------------------------------------
# E.Sujet-métropole-candidat-libre-journée-1-2021-Exercice-4 (4 points)
# ---------------------------------------------------------------------

#
#
#

# -------------------------------------------------
# A.Sujet-Asie-journée 1-2022-Exercice-4 (4 points)
# -------------------------------------------------

# -------------------------------------------------------------------
# B.Sujet-Métropole-journée-1-Remplacement-2021-Exercice-1 (4 points)
# -------------------------------------------------------------------

# ------------------------------------------------------
# C.Sujet-Polynésie-journée-1-2023-Exercice-2 (5 points)
# ------------------------------------------------------

# ------------------------------------------------------
# D.Sujet-Métropole-journée-2-2022-Exercice-5 (4 points)
# ------------------------------------------------------

# --------------------------------------------------------------
# E.Sujet-Centres-étrangers-journée-2-2022-Exercice-4 (4 points)
# --------------------------------------------------------------

#
#
#


# --------------------------------------------------------
# A.Sujet-Métropole-3-journée 2-2024-Exercice-2 (6 points)
# --------------------------------------------------------

def produire_jeu(n):
    resultat = Pile()
    for i in range(...):
        resultat.empiler(...)
    return resultat

# --------------------------------------------------------------
# B.Sujet-Centre-étranger-1-journée 1-2022-Exercice-2 (4 points)
# --------------------------------------------------------------

# ------------------------------------------------------------
# C.Sujet-Centre-étranger-journée 1-2021-Exercice-5 (4 points)
# --------------------------------------------------------------

import random 

def ajout(f):
    couleurs = ("bleu","rouge","jaune","vert")
    indice = randint(0,3)
    enfiler(f,couleurs[indice])
    return f

def vider(f):
    while not f.est_vide() : 
        f.defiler()

def affich_seq(sequence):
    stock = []

def tour_de_jeu(sequence):

    stock = creer_file_vide()
    while not est_vide(sequence) : 
        c_joueur = saisie_joueur()
        c_seq = None

# -------------------------------------------------
# D.Sujet-Asie-journée 2-2024-Exercice-2 (6 points)
# -------------------------------------------------

    # 1 : l'Expression  

# ---------------------------------------------------------------------
# A. Sujet Amérique du sud -journée 2-2022-Exercice 1 (4 points sur 12)
# ---------------------------------------------------------------------


#B

# ---------------------------------------
# A.Sujet-zéro-2021-Exercice-4 (4 points)
# ---------------------------------------

""" Question 1 : 
    Ce sont deslogiciels de type SGBD c'est à dire 
    Système de gestion de bases de données 
    (Anglais : DBMS : Database management system )
""" 
""" Question 2 : 

    a)
    - Dans la table Train, numT est clé primaire et 
    dans la table Reservation, numT est clé étrangère 
    faisant référence à la clé primaire du même nom de          
    la table Train.
    - La valeur 1241 est utilisée comme clé étrangère 
    dans la table Reservation, donc cette valeur doit 
    obligatoirement exister comme valeur de clé primaire 
    dans la table Train.
    - Il est interdit, par lescontraintes d'intégrité 
    référencielle, de supprimer de cette valeur de clé 
    primaire, tant qu'elle est utilisée comme valeur
    de clé étrangère.

    Remarque (Non attendue) : Pour que ces requêtes de
    suppression fonctionnent, il faut permuter l'ordre 
    afin de respecter la hierarchie des dépendances 
    fonctionnells entre les tables.

    b)
    On peut enfreindre les 3 niveaux de contraintes d'intégrité,
    ce qui donne 3 types de cas.
    - 1 er type : On essaie d'insérer un tuple de données pour 
    lequel les domaines dans champs/attributs ne sont pas respéctés.
    - 2 ème types : On essaie d'insérer un tuple de données avec une 
    valeur de clé primaire numR qui existe déjà.
    - 3 ème type : On essaie d'insérer un tuple de données avec une 
    valeur de valeur de clé étrangère numT qui n'existe pas comme
    valeurs de clé primaire dans la table Train.

    Remarque : Au Bac une seule des trois réponse est attendue. 
"""
""" Question 3 : 

a)
SELECT numT 
FROM Train
WHERE destination="Lyon";

b)
INSERT INTO Reservation
    (numR,nomClient,prenomClient,prix,numT)
VALUES 
    (1307,"Turing","Alan",33,654);

c)
UPDATE Train
SET horaireArrivee = "08:11"
WHERE numT = 7869;
"""
""" Question 4 : 
    Cette requête renvoie le nombre de réservations éfféctués
    par la cliente nommée Grace Hopper.
"""
""" Question 5 : 

SELECT destination, prix
FROM Reservation 
JOIN Train ON Reservation.numT = Train.numT
WHERE nom = "Hopper" AND prenom= Grace;

SELECT destination,prix
FROM Reservation,Train
WHERE Reservation.numT = Train.numT AND nom = "Hopper" AND prenom = "Grace";

"""

#
# B. Sujet Métropole - journée 1 - 2021 - Exercice 3 (4 points )
#

#
# C. Sujet Polynésie - journée 1 - 2023 - Exercice 1 (4 points)
# 

#
# D. Sujet Amérique du sud - journée 2 - 2022 - Exercice 3 (4 points)
#