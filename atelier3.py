
def full_name(str_arg: str) -> str:
    # Initialise une  chaine vide pour stocker le nom en majuscules
    nom_majuscules = ""

    # Initialise une variable pour suivre si nous sommes en train de traiter le nom ou le prenom
    est_nom = True

    for caractere in str_arg:
        if caractere == ' ':
            # Lorsque nous atteignons un espace, cela signifie que nous avons terminele nom et nous allons commencer a traiter le prnom
            est_nom = False
        elif est_nom:
            # Si nous sommes en train de traiter le nom, convertissons le caractre en majuscule et ajoutons-le  la chane des noms en majuscules
            nom_majuscules += caractere.upper()
        else :
            if nom_majuscules[-1]  == " ":
                nom_majuscules += caractere.upper()
            else:
                nom_majuscules += caractere

    return nom_majuscules
##ex 2
def full_name(str_arg: str) -> str:
    # Sépare la chaîne en nom et prénom
    nom, prenom = str_arg.split(' ', 1)
    
    # Met le nom en majuscules et le prénom en minuscules avec la première lettre en majuscule
    nom = nom.upper()
    prenom = prenom.capitalize()
    
    # Retourne le nom et prénom formatés
    return f"{nom} {prenom}"


nom_complet = full_name("doe john")
print(nom_complet)  # Résultat attendu : "DOE John"


def is_mail(str_arg: str) -> (int, int):
    # Sépare l'adresse e-mail en partie locale (local_part) et domaine (domain_part) en utilisant l'@
    parts = str_arg.split('@')
    
    if len(parts) != 2:
        # Il doit y avoir exactement un @ dans l'adresse e-mail
        return (0, 2)  # (0, 2) : Le mail n'est pas valide, il manque l'@

    local_part, domain_part = parts

    if not local_part or not domain_part:
        # Vérifie si les parties locale et domaine ne sont pas vides
        return (0, 3)  # (0, 3) : Le mail n'est pas valide, le domaine n'est pas valide

    # Vérifie si le domaine contient un point (.)
    if '.' not in domain_part:
        return (0, 4)  # (0, 4) : Le mail n'est pas valide, il manque le .

    # Si toutes les vérifications passent, l'adresse e-mail est valide
    return (1, 0)  # (1, 0) : Le mail est valide

# Exemple d'utilisation :
adresse_mail = "bisgambiglia@univ-corse.fr"
resultat = is_mail(adresse_mail)

if resultat == (1, 0):
    print("L'adresse e-mail est valide.")
else:
    print("L'adresse e-mail n'est pas valide. Code d'erreur :", resultat[1])
def is_mail(str_arg: str) -> (int, int):
    # Vérifie si l'adresse e-mail contient un @
    if '@' not in str_arg:
        return (0, 2)  # (0, 2) : Le mail n'est pas valide, il manque l'@

    # Sépare l'adresse e-mail en parties locale (local_part) et domaine (domain_part)
    local_part, domain_part = str_arg.split('@')

    # Vérifie si le domaine contient un point (.)
    if '.' not in domain_part:
        return (0, 4)  # (0, 4) : Le mail n'est pas valide, il manque le .

    # Si toutes les vérifications passent, l'adresse e-mail est valide
    return (1, 0)  # (1, 0) : Le mail est valide

# Exemple d'utilisation :
adresse_mail = "bisgambiglia@univ-corse.fr"
resultat = is_mail(adresse_mail)

if resultat == (1, 0):
    print("L'adresse e-mail est valide.")
else:
    print("L'adresse e-mail n'est pas valide. Code d'erreur :", resultat[1])


def mots_Nlettres(lst_mot, n):
    mots_filtres = []
    for mot in lst_mot:
        if len(mot) == n:
            mots_filtres.append(mot)
    return mots_filtres

def test_exercice1():
    # Testons la fonction mots_Nlettres avec quelques exemples
    mots = ["chat", "chien", "oiseau", "rat", "lion", "tigre"]

    # Test 1 : n = 3
    resultat = mots_Nlettres(mots, 3)
    assert resultat == ["chat", "rat"], f"Erreur pour n=3, résultat obtenu : {resultat}"

    # Test 2 : n = 4
    resultat = mots_Nlettres(mots, 4)
    assert resultat == ["chien", "oiseau", "lion", "tigre"], f"Erreur pour n=4, résultat obtenu : {resultat}"

    # Test 3 : n = 5
    resultat = mots_Nlettres(mots, 5)
    assert resultat == [], f"Erreur pour n=5, résultat obtenu : {resultat}"

    # Test 4 : n = 6
    resultat = mots_Nlettres(mots, 6)
    assert resultat == [], f"Erreur pour n=6, résultat obtenu : {resultat}"

    print("Tous les tests ont réussi.")

# Appeler la procédure de test
test_exercice1()
