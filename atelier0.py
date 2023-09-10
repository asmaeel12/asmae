import random

continuer_partie = True

while continuer_partie:
    nombre_manche = 5
    nom_joueur1 = input("Quel est votre nom ? ")
    print("Bienvenue, " + nom_joueur1 + ", nous allons jouer ensemble")

    nom_joueur2 = input("Quel est le nom du deuxième joueur (ou 'Machine' si vous jouez contre l'ordinateur) ? ")
    print("Bienvenue, " + nom_joueur2 + ", nous allons jouer ensemble")

    score_joueur1 = 0
    score_joueur2 = 0

    for numero_manche in range(1, nombre_manche + 1):
        print("Manche " + str(numero_manche))
        choix_joueur1 = ""
        choix_joueur2 = ""

        while choix_joueur1 not in ['pierre', 'papier', 'ciseaux']:
            choix_joueur1 = input(nom_joueur1 + ", faites votre choix parmi (pierre, papier, ciseaux): ")
            if choix_joueur1 not in ['pierre', 'papier', 'ciseaux']:
                print("Je n'ai pas compris votre réponse")

        if nom_joueur2 == 'Machine':
            choix_joueur2 = random.choice(['pierre', 'papier', 'ciseaux'])
        else:
            while choix_joueur2 not in ['pierre', 'papier', 'ciseaux']:
                choix_joueur2 = input(nom_joueur2 + ", faites votre choix parmi (pierre, papier, ciseaux): ")
                if choix_joueur2 not in ['pierre', 'papier', 'ciseaux']:
                    print("Je n'ai pas compris votre réponse")

        print("Si on récapitule : " + nom_joueur1 + " a choisi " + choix_joueur1 + " et " + nom_joueur2 + " a choisi " + choix_joueur2)

        # Logique pour déterminer le gagnant de la manche et mettre à jour les scores
        gagnant = ""
        if choix_joueur1 == choix_joueur2:
            gagnant = "Personne, vous êtes ex aequo"
        elif (
            (choix_joueur1 == "pierre" and choix_joueur2 == "ciseaux")
            or (choix_joueur1 == "papier" and choix_joueur2 == "pierre")
            or (choix_joueur1 == "ciseaux" and choix_joueur2 == "papier")
        ):
            gagnant = nom_joueur1
            score_joueur1 += 1
        else:
            gagnant = nom_joueur2
            score_joueur2 += 1

        print("Le gagnant est " + gagnant)
        print("Les scores à l'issue de cette manche sont donc " + nom_joueur1 + ": " + str(score_joueur1) + " et " + nom_joueur2 + ": " + str(score_joueur2) + "\n")

        if numero_manche < nombre_manche:
            continuer_partie = input("Souhaitez-vous refaire une partie " + nom_joueur1 + " contre " + nom_joueur2 + " ? (O/N) ")
            if not continuer_partie.lower() in ['o', 'oui']:
                print("Merci d'avoir joué ! A bientôt")
