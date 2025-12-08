import random 
import os 
import time

def generatePlayers():

    _rID = '1'
    for i in range(7): 
        _rID += str(random.randint(0,9))
    int(_rID)
    Stats = {'id': _rID, 'pv': 200, 'atk': 40, 'def': 25, 'cc': 5, 'dc': 120, 'spd': 10 }

    return Stats

def showStats(_stats):

    for cle in _stats.keys( ) :
        print (cle , end= ' ' )
    print(" ")

    for cle in _stats.values( ) :
        print ( cle, end= ' ' )
    print(" ")

def setStatsPoints(_stats):

    _nbPoint = 6 
    while _nbPoint > 0 : 
        
        modStats = input("Entrez le nom de la stats a modifier (atk def cc dc spd ) :")
        
        if modStats == "atk" :
            os.system("cls")
            _stats["atk"] += 1
            _nbPoint -= 1
            print("1 point d'attaque ajouté ")
            print("il vous reste :" , _nbPoint, " Points")
            showStats(_stats)

        if modStats == "def" :
            os.system("cls")
            _stats["def"] += 1
            _nbPoint -= 1
            print("1 point de défense ajouté ")
            print("il vous reste :" , _nbPoint, " Points")
            showStats(_stats)

        if modStats == "spd" :
            os.system("cls")
            _stats["spd"] += 1
            _nbPoint -= 1
            print("1 point de vitesse ajouté ")
            print("il vous reste :" , _nbPoint, " Points")
            showStats(_stats)

        if modStats == "cc" :
            os.system("cls")
            _stats["cc"] =  _stats["cc"] * 1 +(5/100)
            _nbPoint -= 1
            print("5% point de coup critique ajouté ")
            print("il vous reste :" , _nbPoint, " Points")
            showStats(_stats)

        if modStats == "dc" :
            os.system("cls")
            _stats["dc"] =  _stats["dc"] * 1 +(15/100)
            _nbPoint -= 1
            print("15% point de dégats critique ajouté ")
            print("il vous reste :" , _nbPoint, " Points")
            showStats(_stats)

def equipement(_stats):

    os.system("cls")
    showStats(_stats)
    print(r"""
    Vous pouvez choisir un equipement parmis ces trois pour vous aidez : 
    - L'armure : Vous ajoute 50 hp et 10 def
    - L'épée : Vous ajoute 10 atk et 10% de cc
    - Le drapeau : Vous ajoute 15% de cc et 20% de dc

    """)
    while True :
        choix = int(input("Entrez 1,2 ou 3 : "))
        if choix == 1: 
            _stats["pv"] += 50 
            _stats["def"] += 10
            return(0)
        elif choix == 2: 
            _stats["atk"] += 10
            _stats["cc"] += 10
            return(0)
        elif choix == 3: 
            _stats["cc"] += 15
            _stats["dc"] += 20
            return(0)

def CalculDegat(J1,J2):

    J1cc = int(J1["cc"])
    J1cc += 1
    ccFait = random.randint(0,100)

    if ccFait <= J1cc : 
        print("Coup critique")
        return(round(((J1["atk"]* 1.08) - J2["def"]) * (1 + (J1["dc"]/100))))
    else : 
            return(round((J1["atk"]* 1.08) - J2["def"]))

def Combat(J1,J2):

    while J1["pv"] > 0 and J2["pv"] > 0: 

        if (J1["spd"] > J2["spd"]) and (J1["spd"] != J2["spd"]):

            J2["pv"] -= CalculDegat(J1,J2) 
            print("Le joueur 2 a subit des dégats il a donc : ",round(J2["pv"]), " PV")
            if J2["pv"] <= 0:
                
                return(0)
            J1["pv"] -= CalculDegat(J2,J1) 
            print("Le joueur 1 a subit des dégats il a donc : ",round(J1["pv"]), " PV")

        elif (J2["spd"] > J1["spd"]) and (J1["spd"] != J2["spd"]):

            J1["pv"] -= CalculDegat(J2,J1) 
            print("Le joueur 1 a subit des dégats il a donc : ",round(J1["pv"]), " PV")
            if J1["pv"] <= 0:
                
                return(0)
            J2["pv"] -= CalculDegat(J1,J2) 
            print("Le joueur 2 a subit des dégats il a donc : ",round(J2["pv"]), " PV")

        elif J1["spd"] == J2["spd"]:

            firtP = random.randint(0,1)

            if firtP == 1:

                J2["pv"] -= CalculDegat(J1,J2) 
                print("Le joueur 2 a subit des dégats il a donc : ",round(J2["pv"]), " PV")
                if J2["pv"] <= 0:
                    
                    return(0)
                J1["pv"] -= CalculDegat(J2,J1) 
                print("Le joueur 1 a subit des dégats il a donc : ",round(J1["pv"]), " PV")

            elif firtP == 0:

                J1["pv"] -= CalculDegat(J2,J1) 
                print("Le joueur 2 a subit des dégats il a donc : ",round(J1["pv"]), " PV")
                if J1["pv"] <= 0:
                    
                    return(0)
                J2["pv"] -= CalculDegat(J1,J2) 
                print("Le joueur 1 a subit des dégats il a donc : ",round(J2["pv"]), " PV")

joueur1 = generatePlayers()
joueur2 = generatePlayers()

print("J1 : Vos statistiques :" )
showStats(joueur1)
setStatsPoints(joueur1)
equipement(joueur1)
os.system("cls")
print("J1 : Vos statistiques Final:" )
showStats(joueur1)
os.system("cls")

print("J2 : Vos statistiques :" )
showStats(joueur2)
setStatsPoints(joueur2)
equipement(joueur2)
os.system("cls")
print("J2 : Vos statistiques Final:" )
showStats(joueur2)
input("Appuyer sur n'importe quelle touche pour lancer le combat : ")
os.system("cls")

Combat(joueur1,joueur2)
if joueur1["pv"] < joueur2["pv"]:
    print("Joueur 2 gagne")
    
elif joueur1["pv"] > joueur2["pv"]:
    print("Joueur 1 gagne") 