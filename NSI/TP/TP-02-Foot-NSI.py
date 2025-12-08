import random

print("Bienvenue dans le soft de gestion de l'équipe de foot")

def fcompo():


    compo=[ ]
    print("veuillez saisir la compo de votre équipe")
    nombrejoueurs=10
    nombredef=int(input("combien de defenseur? "))
    nombrejoueurs=nombrejoueurs-nombredef

    nombremilieu=int(input("Combien de milieu ? "))
    nombrejoueurs=nombrejoueurs-nombremilieu

    nombreattaque=int(input("Combien d'attaquant? "))
    nombrejoueurs=nombrejoueurs-nombreattaque

    if(nombrejoueurs!=0):
        print("configuration équipe incorrect, veuillez recommencer")
        fcompo()

    else:
        print("Configuration correcte")
        print("votre équipe est composé de 1 gardien ",nombredef, " Defenseur, ",nombremilieu, " Millieu, ",nombreattaque," Attaquant")
        print("la configuration de votre équipe est donc : 1-",nombredef,"-",nombremilieu,"-",nombreattaque)

    numerojoueur=random.randint(0,99)
    while numerojoueur in compo:
        numerojoueur=random.randint(0,99)
    compo.append(numerojoueur)
    compo.append("GARDIEN")
    nomjoueur=input("comment s'appel votre gardien : ")
    compo.append(nomjoueur)
    

    for i in range(nombredef):
        while numerojoueur in compo:
            numerojoueur=random.randint(0,99)
        compo.append(numerojoueur)
        nomjoueur=input("comment s'appel votre defenseur : ")
        compo.append("DEFENSEUR")
        compo.append(nomjoueur)

    for j in range(nombremilieu):
        while numerojoueur in compo:
            numerojoueur=random.randint(0,99)
        compo.append(numerojoueur)
        compo.append("MILIEU")

        nomjoueur=input("comment s'appel votre milieu : ")
        compo.append(nomjoueur)

    for k in range(nombreattaque):
        while numerojoueur in compo:
            numerojoueur=random.randint(0,99)
        compo.append(numerojoueur)
        compo.append("ATTAQUANT")
        nomjoueur=input("comment s'appel votre attaquant : ")
        compo.append(nomjoueur)

    #print (compo)
    j=0
    for i in range(11):
        print(compo[j:j+3])
        j=j+3


fcompo()