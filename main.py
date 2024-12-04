# Partie 1 : Variables (grille ; joueur_actuel ; fin_jeu ; gagnant)

# La grille de jeu est représentée par une liste de 9 éléments (chaque case étant initialement vide "-")
grille = ["-", "-", "-",
          "-", "-", "-",
          "-", "-", "-"]

# Variable qui représente le joueur actuel. Elle sera définie plus tard en fonction du choix du joueur.
joueur_actuel = ""

# Variable qui indique si la partie est terminée ou non.
fin_jeu = False

# Variable qui stocke le gagnant. Elle sera vide ("") si personne n'a gagné, ou contiendra "X" ou "O" si un joueur a gagné.
gagnant = ""

# Partie 2 : Fonctions (jouer + choix_joueur + affichage_grille)

# Fonction principale qui gère le déroulement du jeu
def jouer():
    choix_joueur()  # Demande à l'utilisateur de choisir son symbole (X ou O)
    affichage_grille()  # Affiche l'état actuel de la grille
    while fin_jeu == False :  # Tant que la partie n'est pas finie
        tour(joueur_actuel)  # Un joueur joue son tour
        verifier_fin_jeu()  # Vérifie si le jeu est terminé (victoire ou match nul)
        joueur_suivant()  # Change de joueur
    resultat()  # Affiche le résultat de la partie une fois finie


# Fonction pour demander à l'utilisateur de choisir X ou O
def choix_joueur():
    global joueur_actuel  # Cette variable sera utilisée dans la fonction jouer pour savoir quel joueur est actif.
    joueur_actuel = input("Veuillez choisir soit une croix (X), soit un rond (O) : ")
    
    while True:
        joueur_actuel = joueur_actuel.upper()  # Convertit la réponse en majuscule
        if joueur_actuel == 'X':  # Si le joueur choisit X
            print("Vous avez choisi X. Le joueur 2 aura O")
            break
        elif joueur_actuel == 'O':  # Si le joueur choisit O
            print("Vous avez choisi O. Le joueur 2 aura X")
            break
        else:  # Si l'entrée n'est pas valide, on redemande
            joueur_actuel = input("Veuillez choisir soit une croix (X), soit un rond (O) : ")

# Appeler la fonction pour tester le choix du joueur
choix_joueur()

# Fonction pour afficher l'état actuel de la grille
def affichage_grille():
    print("\n")  # Ajoute une ligne vide avant d'afficher la grille pour la rendre plus lisible
    print("-------------")
    print("|", grille[0], "|", grille[1], "|", grille[2], "|")  # Première ligne
    print("-------------")
    print("|", grille[3], "|", grille[4], "|", grille[5], "|")  # Deuxième ligne
    print("-------------")
    print("|", grille[6], "|", grille[7], "|", grille[8], "|")  # Troisième ligne
    print("-------------")
    print("\n")  # Ajoute une ligne vide après la grille

# Appeler la fonction pour afficher la grille
affichage_grille()

# Fonction qui gère le tour d'un joueur
def tour(joueur):
    print("C'est le tour du joueur : ", joueur)  # Affiche quel joueur doit jouer
    pos = input("Veuillez sélectionner un espace vide sur la grille entre 1 et 9 : ")
    
    valide = False  # Variable qui vérifie si la position choisie est valide
    while valide == False:
    
        # Si la position choisie n'est pas un nombre entre 1 et 9, on redemande
        while pos not in ["1","2","3","4","5","6","7","8","9"]:
            pos = input("Veuillez sélectionner un espace vide sur la grille entre 1 et 9 :")
        pos = int(pos) - 1  # Convertit la position en indice de la liste (indices de 0 à 8)
        
        # Si la case est vide, on peut jouer. Sinon, on redemande.
        if grille[pos] == "-":
            valide = True
        else:
            print("Vous ne pouvez pas accéder à cette position")
            
    # Une fois la position validée, on place le symbole du joueur dans la grille
    grille[pos] = joueur
    affichage_grille()  # Affiche à nouveau la grille après le coup

# Fonction qui vérifie si la partie est terminée (victoire ou match nul)
def verifier_fin_jeu():
    verfifier_victoire()  # Vérifie si un joueur a gagné
    verifier_match_nul()  # Vérifie si la partie est un match nul
    
# Fonction qui vérifie les conditions de victoire
def verfifier_victoire():  # conditions de victoires
    global fin_jeu
    global gagnant
    # Vérification des lignes
    if grille[0] == grille[1] == grille[2] and grille[2] != "-":
        fin_jeu = True
        gagnant = grille[1]
    if grille[3] == grille[4] == grille[5] and grille[3] != "-":
        fin_jeu = True
        gagnant = grille[3]
    if grille[6] == grille[7] == grille[8] and grille[7] != "-":
        fin_jeu = True
        gagnant = grille[6]
    # Vérification des colonnes
    if grille[0] == grille[3] == grille[6] and grille[0] != "-":
        fin_jeu = True
        gagnant = grille[1]
    if grille[1] == grille[4] == grille[7] and grille[4] != "-":
        fin_jeu = True
        gagnant = grille[4]
    if grille[2] == grille[5] == grille[8] and grille[8] != "-":
        fin_jeu = True
        gagnant = grille[5]
    # Vérification des diagonales
    if grille[0] == grille[4] == grille[8] and grille[8] != "-":
        fin_jeu = True
        gagnant = grille[8]
    if grille[2] == grille[4] == grille[6] and grille[3] != "-":
        fin_jeu = True
        gagnant = grille[3]
        
# Fonction qui vérifie s'il y a un match nul
def verifier_match_nul():
    global fin_jeu
    if "-" not in grille:  # Si plus aucune case vide
        fin_jeu = True
    
# Fonction qui permet de passer au joueur suivant
def joueur_suivant():
    global joueur_actuel
    if joueur_actuel == "X":  # Si le joueur actuel est X, le suivant sera O
        joueur_actuel = "O"
    else:  # Sinon, le joueur suivant sera X
        joueur_actuel = "X"
        
# Fonction pour afficher le résultat du jeu
def resultat():
    if gagnant == "X" or gagnant == "O":  # Si un joueur a gagné
        print("Le joueur : ", gagnant, "a gagné")
    else:  # Si c'est un match nul
        print("Match nul")

# Lancement du jeu
jouer()