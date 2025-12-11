# Evalutaion de rattrapage de NSI du 06/09/2025
# Classe de Terminal 
# Note : 19.25/20

#Exo 1: 

# a)
# Ecrire une version itérative d'une fonction en Python 3, qui calculela puissance du réel x à 
# l'exposant entier n > 0.
def fact_iter(x :float, n :int): # => Float
    """ Docstring """

    assert( (type(x) == float) or (type(x) == int) and (type(n) == int))
    assert( n >= 0)

    res = 1 
    for i in range(n):
        res = res * x 

    return(res)

# b)
print(fact_iter(0.1 ,4))
# res = 1
# res = 1 * 0.1

# res = 0.1 * 0.1
# res = 0.01 * 0.1
# res = 0.001 * 0.1
# res = 0.0001 * 0.1

def fact_rec(x: float, n: int):  # => float
    """ Calcule récursivement x puissance n (n >= 0) """

    # Cas de base
    if n == 0:
        return 1

    # Appel récursif
    return x * fact_rec(x, n - 1)

#Appels récursifs : 
# fact_rec(0.1, 4) → retourne 0.1 * fact_rec(0.1, 3)
# fact_rec(0.1, 3) → retourne 0.1 * fact_rec(0.1, 2)
# fact_rec(0.1, 2) → retourne 0.1 * fact_rec(0.1, 1)
# fact_rec(0.1, 1) → retourne 0.1 * fact_rec(0.1, 0)
# fact_rec(0.1, 0) → retourne 1 (cas de base)

#Remontée des résultats : 
# fact_rec(0.1, 1) = 0.1 * 1 = 0.1
# fact_rec(0.1, 2) = 0.1 * 0.1 = 0.01
# fact_rec(0.1, 3) = 0.1 * 0.01 = 0.001
# fact_rec(0.1, 4) = 0.1 * 0.001 = 0.0001

# Résultat final : 0.0001
