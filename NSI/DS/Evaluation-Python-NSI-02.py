# Evalutaion de NSI du 07/05/2025
# Classe de 1 ere 
# Note : 20/20

#Exercice 1 : 
# Programmer la fonction multiplication, prenant en paramètres deux nombres entiers relatifs n1 et 
# n2, et qui renvoie le produit de ces deux nombres.
# Les seules opérations autorisées sont l'addition et la soustraction.

def multiplication(n1,n2):
    _res = 0
    
    if n1 == 0 or n2 == 0:
        _res = 0
    elif n1 < 0 and n2 > 0:
        for i in range(n2):
            _res += n1
    elif n2 < 0 and n1 > 0:
        for i in range(n1):
            _res += n2
    elif n1 < 0 and n2 < 0:
        n1 = -n1
        for i in range((n1)):
            _res -= n2
    print(_res)
#multiplication(-4,-8)

#Exercice 2 : 
# On considère dans cet exercice une representation binaire d'un entier non signé en tant que tableau
# de booléens.
# Si : tab = [True, False, True, False, True, True]
# est tel un tableau, alors l'entier qu'il représente est 2^6 + 2^4 + 2^1 + 2^0 = 83. Cette représentation
# consistant à placer en premier le booléen indiquant la puissance la plus élevée de 2 est dite big-endian 
# ou grand-boutiste.abs

# Ecrire une fonction gb_vers_entier qui prend en paramètre un tel tableau et renvoie l'entier qu'il 
# représente.

def gb_vers_entier(tab):
    _result = 0
    count = len(tab)
    for i in tab:
        count -= 1  # Remplace l'utilisation d'indice négatif 
        if i == True:
            _result += 2**count
        
    print(_result)
#gb_vers_entier([False,True,False])    

#Exercice 3 : 
# Ecrire une fonction indices_maxi qui prend en paramètre un tableau non vide de nombre entiers tab,
# représenté par une liste Python et qui renvoie un tuple (maxi, indices ) ou : 
#  - maxi est le plus grand élémentdu tableau tab ;
#  - indices est une liste Python contenant les indices du tableau tab ou apparait ce plus grand élément.

def fonctionindices_maxi(tab):
    maxi = tab[0]
    indices = []
    count = 0
    _res = []
    
    for i in tab:
        if i > maxi:
            maxi = i
    for i in range(len(tab)):
        if tab[i] == maxi:
            #indices.append(tab[i])
            indices.append(count)
        count += 1
    
    _res.append(maxi)
    _res.append(indices)
    return _res          
#print(fonctionindices_maxi([68,67,-30,-96,95,95]))
