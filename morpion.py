# Liste interieur de la grille
grille = ["-","-","-",
          "-","-","-",
          "-","-","-"]

# Creation de variable
joueur_actuel =""
fin_jeu = False
gagnant = ()

# Permet appliquer le jeu dans le terminal(reprend toutes les étapes)
def jouer():
    choix_joueur()
    affichage_grille()
    while fin_jeu == False:
        tour(joueur_actuel)
        verifier_fin_jeu()
        joueur_suivant()
    resultat()

# Creation d'une définition pour le choix du joueur
def choix_joueur():
    global joueur_actuel
    joueur_actuel = input("Veuillez choisir soit une croix (X), soit un rond (O): ")
    while True:
        joueur_actuel = joueur_actuel.upper()
        if joueur_actuel == 'X' :
            print("Vous avez choisi X. Le joueur 2 aura O")
            break
        elif joueur_actuel == 'O' :
            print("Vous avez choisi O. Le joueur 2 aura X")
            break
        else:
            joueur_actuel = input("Veuillez choisir soit une croix (X), soit un rond (O): ")

# Creation et affichage de la grille
def affichage_grille():
    print("\n")
    print("-------------")
    print("|",grille[0],"|",grille[1],"|",grille[2],"|")
    print("-------------")
    print("|",grille[3],"|",grille[4],"|",grille[5],"|")
    print("-------------")
    print("|",grille[6],"|",grille[7],"|",grille[8],"|")
    print("-------------")
    print("\n")

# Definition et boucle pour le tour par tour
def tour(joueur) :
    print("C'est le tour du joueur :", joueur)
    pos = input("Veuillez choisir un numéro de case entre 1 et 9 :")

    valide = False
    while valide == False:

        while pos not in ["1","2","3","4","5","6","7","8","9"] :
            pos = input("Veuillez choisir un numéro de case entre 1 et 9 :")
        pos = int(pos) - 1

        if grille[pos] == "-" :
            valide = True
        else :
            print("Vous ne pouvez pas choisir cette case :")

    grille[pos] = joueur
    affichage_grille()

# Condition de jeu
def verifier_fin_jeu() :
    verifier_victoire()
    verifier_match_nul()

def verifier_victoire() :
    global fin_jeu
    global gagnant

# Les Lignes
    if grille [0] == grille[1] == grille[2] and grille[2] != "-" :
        fin_jeu = True
        gagnant = grille[2]
    if grille [3] == grille[4] == grille[5] and grille[5] != "-" :
        fin_jeu = True
        gagnant = grille[5]
    if grille [6] == grille[7] == grille[8] and grille[8] != "-" :
        fin_jeu = True
        gagnant = grille[8]

# Les colonnes
    if grille [0] == grille[3] == grille[6] and grille[6] != "-" :
        fin_jeu = True
        gagnant = grille[6]
    if grille [1] == grille[4] == grille[7] and grille[7] != "-" :
        fin_jeu = True
        gagnant = grille[7]
    if grille [2] == grille[5] == grille[8] and grille[8] != "-" :
        fin_jeu = True
        gagnant = grille[8]
     
# Les diagonales
    if grille [0] == grille[4] == grille[8] and grille[8] != "-" :
        fin_jeu = True
        gagnant = grille[8]
    if grille [2] == grille[4] == grille[6] and grille[6] != "-" :
        fin_jeu = True
        gagnant = grille[6]

# Résultat et fin de jeu
def verifier_match_nul() :
    global fin_jeu
    if "-" not in grille :
        fin_jeu = True

def joueur_suivant() :
    global joueur_actuel
    if joueur_actuel == "X":
        joueur_actuel = "O"
    else:
        joueur_actuel = "X"

def resultat() :
    if gagnant == "X" or gagnant == "O" :
        print("Le joueur : ",gagnant,"a gagné")
    else:
        print("Match nul")

jouer()



