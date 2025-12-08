# Evalutaion de rattrapage de NSI du 15/05/2025
# Classe de 1 ere 
# Note : 20/20

# Exercice 1 : 

# Ecrire une fonction nb_mot qui détermine le nombre de mots dans une chaine de charactère,
# renvoie 0 si le str est nul. (détecte les " " et les "'")

def nb_mot(_chaine): 
    if _chaine :
        total = 0 
        for i in _chaine:
            if i == " " or i == "'":
                total += 1 
        return(total)
    return(0)

#print(nb_mot(" J'aime la NSI")) # >>>  4

#Exercice 2 : 

# Ecrire une fonction Minmax qui prend une liste d'entier en paramètre et qui 
# détermine le plus grand et le plus petit élément d'une liste. La fonction 
# calcul aussi l'écart type entre le plus grand et le plus petit.

def Minmax(tab):
    mini = tab[0]
    maxi = tab[0]
    for i in tab:
        if i >= maxi :
            maxi = i
        if i <= mini :
            mini = i
    return(mini,maxi,(maxi-mini))

#print(Minmax([1,4,6,8,19,4,2,0]))  # >>> (0, 19, 19)