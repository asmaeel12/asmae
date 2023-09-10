def somme(L : list) -> int : ##retourne la somme des valeurs de la liste en utilisant range 
    sum = 0
    for i in range (len(L)):
        sum += L[i]
    return sum

## la deusieme sans utiliser le range 
def somme_ele(L : list) :
    sum = 0
    for e in L :
        sum += e
    return sum


def somme_while (L : list) :
    sum = 0
    i = 0
    while i < len(L) :
        sum += L[i]
        i += 1
    return sum

def moyenne(L : list) -> float :
    if len (L) == 0 : #tester si la lsite est vide
        return 0
    else :
        somme = sum (L)
        moyenne = sum (L) / len ( L)
        return moyenne 
    
def nb_sup(L: list, e: int):
    # Initialise un compteur à zéro pour suivre le nombre d'éléments supérieurs à e dans la liste L
    count = 0

    # Parcours de la liste L en utilisant des indices
    for i in range(len(L)):
        # Vérifie si l'élément à l'indice i est supérieur à e
        if L[i] > e:
            # Si c'est le cas, incrémente le compteur
            count += 1
    # Retourne le nombre d'éléments supérieurs à e dans la liste L
    return count




def nb_sup(L : list, e : int):
    count = 0
 
    for element in L:
        # Vérifie si l'élément actuel (element) est supérieur à e
        if element > e:
            # Si c'est le cas, incrémente le compteur
            count += 1

    # Retourne le nombre d'éléments supérieurs à e dans la liste L
    return count

    
def moy_sup(L : list, e :int) -> float:
    somme = 0  # Initialise la somme des éléments supérieurs à e à zéro
    count = 0  # Initialise le compteur du nombre d'éléments supérieurs à e à zéro
    for element in L:
        if element > e:
            somme += element  # Ajoute l'élément à la somme
            count += 1  # Incrémente le compteur

    # la if pour éviter  la division par zéro
    if count == 0:
        return 0   
    else:
        moyenne = somme / count   
        return moyenne  # Retourne la moyenne


def val_max(L : list ):
    valeur_maximal = L[0]  # on va supposer que la valeur maximal est celle d indice 0
    for element in L:
        if element > valeur_maximal:
            valeur_maximal = element
    return valeur_maximal
def ind_max(L: list) :

    max_value = L[0] 
    max_index = 0  

    for i in range(1, len(L)):
        if L[i] > max_value:
            max_value = L[i]
            max_index = i
    return max_index

## exercice 2
## en utilisant la methode for 
def position(lst, elt):
    for i in range(len(lst)):
        if lst[i] == elt: ## si l indice egale l entier
            return i
    return -1  

def position(lst, elt):
## en utilisant le methode while
    i = 0
    while i < len ( lst): ## si l indice egale l entier
        if lst[i] == elt :
            return i
        i +=1
    return -1


def nb_occurrences(lst,e) :
    count = 0  # Initialise le compteur à zéro
    for element in lst:
        if element == e: ## si un element  egale a l entier e on incremente le compteur a chaque onccurence
            count += 1  
    return count

def  est_triee(lst : list ) :
    if len (lst) < 1:
        return True        # Une  liste ou une liste d un seul element est tjrs triee
    for i in range (1,len (lst)) :
        if lst[i] < lst [i-1] :
            return False     # Si on trouve un element inferieur a l element precedent donc la liste n est pas triee.
    return True  # Si la boucle s est terminee sans retourner false daonc la liste est  triee.



## la deusieme facon en utilisant le while
def est_triee (lst : list) :
    if len (lst) < 1:
        return True     ## une liste vide ou bien qui ne contient q un seul element une liste tjrs triee
    i = 0
    while i < len (lst) :
        if lst [i] > lst [i+1] :
            return False  ## si on trouve un element superieur a l element suivant donc la liste n est pas triee
            i += 1
            ## si la boucle s est termine sans retourner false donc la liste est triee
    return True


def position_tri(lst : list,e : int) :
    # l'algorithme de recherche dichotomique sert a trouve un element cible dans une liste triee en la divisant sur deux parties
    debut = 0 # on va initialiser la partie gauche a 0
    fin = len (lst )-1 # la partie droite on va l initialiser a la longuer de la liste - 1

    while debut <= fin :
        milieu = (debut + fin)// 2
        
        if lst[milieu] == e:   #Si l element du milieu egale a e donc l element  a ete trouve  et son indice est retourne
            return milieu  # L'élément a été trouvé, retourne son indice.
        elif lst[milieu] < e:
            debut = milieu + 1  # L'élément est inferieur a e donc on doit chercher  dans la partie droite du sous-tableau.
        else:
            fin = milieu - 1  # L'élément est dans la partie gauche du sous-tableau.
    
    return -1  # L'élément n'est pas présent dans la list



## exercice 3 
def a_repetitions(lst : list ) -> bool :
    T = []  # Initialisation de la liste T à la liste vide qui va stocker les elements uniques de la liste lst
    i = 0  # Indice pour parcourir la liste Lst
    while i < len(lst):
        element = lst[i]
        
        if element not in T: # 
            T.append(element)  # Ajout de l'élément dans la liste T
        else:
            return True  # Répétition trouvée
        i += 1  # Passer à l'élément suivant
    return False  # Aucune répétition trouvée, la boucle a parcouru toute la liste







 





 


 