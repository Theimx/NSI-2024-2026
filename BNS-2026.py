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

#Sujet 2 : 