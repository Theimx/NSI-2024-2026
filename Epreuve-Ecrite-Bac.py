# Nombre de Sujet corrigé : 3
# Liste des thèmes des sujets : SQL, File, Pile


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
#Sujet sur les structures de données file

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


# ---------------------------------------------------------------
# B. Sujet Métropole -journée 1-2021-Exercice 4 (4 points sur 12)
# ---------------------------------------------------------------


# -----------------------------------------------------------------------------
# C. Sujet Métropole remplacment -journée 2 - 2021-Exercice 5 (4 points sur 12)
# -----------------------------------------------------------------------------


# ---------------------------------------
# A.Sujet-zéro-2021-Exercice-4 (4 points)
# ---------------------------------------
#Sujet sur les bases de données SQL

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

# --------------------------------------------------------------
# B. Sujet Métropole - journée 1 - 2021 - Exercice 3 (4 points )
# --------------------------------------------------------------

# -------------------------------------------------------------
# C. Sujet Polynésie - journée 1 - 2023 - Exercice 1 (4 points)
# -------------------------------------------------------------
#Sujet sur les bases de données SQL
""" Question 1:
a)  Expliquer pourquoi la requête suivante produit une erreur lors de
    l'ajout dans la table Equipe (voir docs):

INSERT INTO Equipe
VALUES (11,"Toulouse","2 rue du Nord, 40100 Dax", "05 04 03 02 01");

-Dans cette requête d'inserstion d'un nouveau tuble, la valeur de clé primaire est 11;
or celle-ci est déjà présente.L'erreur provient du non respect de l'unicité de la clé primaire.
Rupture de l'unicité (l'id_equipe 11 est déjà présent dans la table).

b) Justifier l'utilisation du type utilisé pour stocker l'attibut téléphone : 

-Le choix d'un domaine (type) relatif aux chaines de charactères permet de conserver le 
zéro en premier caractère et la présentation par blocs de 2 chiffres séparé par des 
espaces.

c) Donnez le résultat de la requête suivante : 
SELECT nom, adresse, telephone FROM Equipe WHERE id_equipe = 5;

-On obtient la vue : 
("Lyon", "451 cours d'Emile Zola, 69100 Villerbanne" , "04 05 06 07 08" )

d) Donner et expliquer le résultat de la requête suivante :
SELECT COUNT(*) FROM Equipe;

-La requête renvoie 12, car la requêtede sélection utilise la fonction d'aggrégation COUNT(),
qui permet de dénombrer tous les tuples de données de la table Equipe.
(Le paramètre * dans la fonction COUNT() indique que l'on prend en compte tous les attributs.)

e) Ecrire la requête SQL permettant d'afficher les noms des équipes par ordre alphabétique : 

SELECT nom FROM Equipe
ORDER BY nom;

f) Ecrire la requête permettant de corriger le nom de l'équipe dont l'id_equipe est 4 :

UPDATE Equipe
SET nom="Tarbes"
WHERE id_equipe = 4;
"""
""" Question 2:
a) Expliquer pourquoi id_equipe est t'il déclaré clé étrangère dans la nouvelle table Joueuse.id_equipe :

-La clès étrangère Joueuse.id_equipe qui fait référence à la clè primaire Equipe.id-equipe permet de savoir
à quelle équipe appartient une joueuse. (Pas d'ambiguité car la clé primaire est unique : Une joueuse appartient
à une seule équipe.)

b) Expliquer pourquoi on ne peut pasdiréctement supprimer  toute les informations relatives dans la table équipe : 

-Pour respecter les contraintes d'intégrité référentielle, si on veut supprimer l'équipe d'identifiant n dans la table
Equipe, il faut d'abord supprimmer toutes données des joueuse de cette équipe, c'est à dire tous les tuples de données 
de la table Joueuse ayant la valeurs n comme id_equipe.
(Respect de la hiérarchie de dépendance fonctionelle entre la clé primaire et la clé étrangère.)

c) Ecrire la requête SQL qui permet d'afficher les noms et les prenoms des joueuse de l'équipe d'Angers par ordre
Alphabétique des noms. On supposera que l'utilisateur qui écrit cette requête ne connaît pas l'identifiant de l'équipe.

version avec jointure:

SELECT Joueuse.nom, prenom
FROM Joueuse
JOIN Equipe ON
Joueuse.id-equipe = Equipe.id-equipe
WHERE Equipe.nom = "Angers";

version avec produit cartésien:

SELECT Joueuse.nom,prenom
FROM Joueuse,Equipe
WHERE Joueuse.id-equipe=Equipe.id-equipe
AND Equipe.nom="Angers";
"""
""" Question 3:
a) Proposer un schéma relationel pour la table Match,préciser les clés étrangère si besoin:

Match:
id_match    --> INT (clé primaire)
date_match  --> DATE
#id_equipe1 --> INT (clé étrangère qui référence la clé primaire id-equipe de la table Equipe)
#id_equipe2 --> INT (clé étrangère qui référence la clé primaire id-equipe de la table Equipe)
score1      --> INT
score2      --> INT

b) Requête d'insertion:
INSERT INTO Match(id_match,date_match,id_equipe1,id_equipe2,score1,score2)
VALUES (10,"23/10/2021",3,6,73,78);
"""
# -------------------------------------------------------------------
# D. Sujet Amérique du sud - journée 2 - 2022 - Exercice 3 (4 points)
# -------------------------------------------------------------------
#Sujet sur les bases de données SQL

"""
jointure : 

SELECT nom 
FROM Fabricant
JOIN ModeleVelo ON Fabricant.idFabricant = ModeleVelo.idFabricant
WHERE Stock > 0;

produit cartésien : 

SELECT nom 
FROM Fabricant,ModeleVelo
WHERE Fabricant.id = ModeleVelo.idFabricant AND Stock > 0;
"""

#
# E.
#
#Sujet sur les bases de données SQL.

""" 
Q1 : Les deux premières requêtes d'insertion ne génère pas d'erreur (si les valeurs clés primaire
128 et 200 sont libres pour l'attribut idEleve ) en revanche, la troisième requête essaie d'insérer
un tuple de données avec la valeur de clé primaire 128, qui est déjà utilisée; ainsi, il y a une
erreur de nom respect des contraintes d'intégrités d'unicité de la clé primaire.

Q2 : Pour insérer un tuple de données dans la relation Emprunts, le champ Empunts.idEleve, qui est
une clé étrangère faisant référence à la clé primaire Eleves.idEleve, doit obligatoirement utiliser 
une valeur déjà présente dans ue tuple de données de la relation Eleves. Il faut donc impérativement 
que le tuple des données de l'élève dans la table Eleves.

Q3 : 
SELECT titre FROM Livres WHERE auteur="Molière";

Q4 : 
SELECT COUNT(*)
FROM Eleves 
WHERE class='T2';

Q5 : 
INSERT INTO Emprunts
VALUES(640, 192, "9782", "2020-09-15", NULL);

UPDATE Emprunts SET dateRetour="2020-09-30" WHERE idEmprunt=640;

Q6 : 
SELECT DISTINCT nom, prenom 
FROM Eleves, Emprunts
WHERE Eleves.idEleves=Emprunts.idEleves
AND Eleves.classe='T2';

Q7 : 
SELECT nom, prenom
FROM Eleves, Emprunts, Livres
WHERE Eleves.idELeves=Emprunts.idEleve AND Livres.isbn=Emprunts.isbn AND titre="Les misérables";
"""

# -------------------------------------------------------------------
# A. Sujet Amérique du sud - journée 2 - 2025 - Exercice 2 (6 points)
# -------------------------------------------------------------------
#Sujet sur les listes chainées.