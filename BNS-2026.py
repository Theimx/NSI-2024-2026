# ------------------
#  SUJETS ZERO (0/3)
# ------------------

#----------------------------------------------------------------------------------------------
# Exercice 1 : determine si une année est bissextile ou non. (Prend un entier, renvoie un Bool)
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
#----------------------------------------------------------------------------------------------