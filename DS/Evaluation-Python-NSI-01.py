# Evalutaion de NSI du 10/02/2025
# Classe de 1 ere 
# Note : 18/20
import random

# Proposer une fonction pour le jeux de la roulette
# L’utilisateur possède 60 jetons, a chaque manche, il peut parier sur 1 a 3 cases. Chaque pari consomme un jeton.
# Si l’utilisateur gagne en ayant parié sur 1 case, il gagne 10 jetons.
# Si l’utilisateur gagne en ayant parié sur 2 cases, il gagne 6 jetons
# Si l’utilisateur gagne en ayant parié sur 3 case il gagne 4 jetons
# Si l’utilisateur choisie de parier sur 0 case, c’est qu’il souhaite s’arrêter.
# L’ordinateur doit générer un nombre aléatoire compris entre 1 et 25
# Le jeux continue tant que l’utilisateur le souhaite ou si ses jetons sont épuisées 
# Le logiciel ne faite pas de vérification sur le nombre de jeton pariés.
# 25 cases

# https://www.quiziniere.com/diffusions/ZJXLPN/copie/PDM

def roulette():
    _banque = 60 
    _rejouer = True
    

    while _rejouer == True:

        _num = random.randint(1,25)
        _nbParis = int(input("entrez combien de pari vous souhaitez réalisez Maximum 3 (0 si vous ne souhaitez pas jouer): "))
        _banque -= 1
        print("Vous avez depensez 1 jetons pour réaliser votre paris")

        if _nbParis == 0 :
            print("Bonne continuation, score : ",_banque)
            break

        if _nbParis == 1 :
            print("debug reponse (c'est pas un oublie je vous la laisse pour que vous testiez ): ",_num)
            _reponse = int(input("entrez un nombre entre 1 et 25 : "))

            if _reponse == _num :
                _banque += 10
                print("Vous avez gagnez, 10 jetons ont été ajouter a votre Banque .")
                print(" ")

        elif _nbParis == 2 :
            print("debug reponse (c'est pas un oublie je vous la laisse pour que vous testiez ): ",_num)
            _reponse = int(input("entrez un nombre entre 1 et 25 : "))
            _reponse2 = int(input("entrez un second nombre entre 1 et 25 : "))

            if _reponse == _num or _reponse2 == _num:
                _banque += 6
                print("Vous avez gagnez, 6 jetons ont été ajouter a votre Banque .")
                print(" ")

        elif _nbParis == 3 :
            print("debug reponse (c'est pas un oublie je vous la laisse pour que vous testiez ): ",_num)
            _reponse = int(input("entrez un nombre entre 1 et 25 : "))
            _reponse2 = int(input("entrez un second nombre entre 1 et 25 : "))
            _reponse3 = int(input("entrez un troisième nombre entre 1 et 25 : "))

            if _reponse == _num or _reponse2 == _num or _reponse3 == _num:
                _banque += 4
                print("Vous avez gagnez, 4 jetons ont été ajouter a votre Banque .")
                print(" ")

# Proposer une fonction qui réalise le jeux de la pierre.
# Le jeu du Pierre, est un jeux ou les joueurs retirent des pierres d'un ensemble et 
# celui qui retire la dernière pierre gagne. Le tas de pierre est fixé a 25.
# Les joueurs retirent à tour de rôle un nombre de pierres entre 1 et 3. Le joueur ne doit
#  pas pouvoir retirer plus de 3 pierre et moins d’une pierre.
# Le joueur qui prend la dernière pierre gagne.
# Le programme doit vérifier après chaque tour si un joueur a gagné et il 
# vérifie que les joueurs entre un nombre de pierre correcte.

def pierre():
    _nbCailloux = 25 
    print(""" Chaque joueur vas devoir a tour de role, retirer entre 1 et 3 pierre du tat de 25 au départs
             Celui qui retireras la dernière pierre du paquets gagne la partie .
    
    """)
    _player1 = 0
    _player2 = 0
    _win = False 
    while _win != True :

        print("Le joueur 1 doit entrez combien de pierre il veut retirer (entre 1 et 3): ")
        _player1 = int(input("Combien ? :  "))

        if _player1 == 1 or _player1 == 2 or _player1 == 3:
            _nbCailloux -= _player1 
            print("Il reste ",_nbCailloux," dans le tat.")
            if _nbCailloux <= 0 :
                print("Le joueur 1 gagne la partie .")
                break
        else : 

            print("Mauvaise entrez, au joueur suivant .")
        _player1 = 0

        print("Le joueur 2 doit entrez combien de pierre il veut retirer (entre 1 et 3): ")
        _player2 = int(input("Combien ? :  "))

        if _player2 == 1 or _player2 == 2 or _player2 == 3:
            _nbCailloux -= _player2 
            print("Il reste ",_nbCailloux," dans le tat.")
            if _nbCailloux <= 0 :
                print("Le joueur 2 gagne la partie .")
                break
        else : 
            print("Mauvaise entrez, au joueur suivant .")
        _player2 = 0