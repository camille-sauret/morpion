# Liste interieur de la grille
grille = ["-","-","-",
          "-","-","-",
          "-","-","-"]

# Creation de variable
joueur_actuel =""
fin_jeu = False
gagnant = ()

# Permet appliquer le jeu dans le terminal (structure principale)
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
    print("|",grille[0],"|",grille[1],"|",grille[2],"|") # Valeurs de la liste
    print("-------------")
    print("|",grille[3],"|",grille[4],"|",grille[5],"|")
    print("-------------")
    print("|",grille[6],"|",grille[7],"|",grille[8],"|")
    print("-------------")
    print("\n")