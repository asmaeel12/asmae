from datetime import date
def message_imc(IMC):
    if IMC<16.5:
        return "denutrition ou famine"
    elif IMC<18.5:
        return"maigreur"
    elif IMC<25:
        return"corpulence normale"
    elif IMC<30:
        return"surpoids"
    elif IMC<35:
        return"obesite moderee"
    elif IMC<40:
        return"obesite severe"
    else:
        return"obesite morbide"
    ##test
    def test_message_imc():
        listimc = [15, 17, 20, 28, 33, 38, 45]  

        for IMC in imc_list:
            interpretation = message_imc(IMC)
            print(f"Pour un IMC de {imc}, l'interprétation est : {interpretation}")
    test_message_imc()

    ##exercice 2
    def annee_bissextile(annee):
        if annee<0:
            return False
        elif (annee%4==0 and annee%100!=0)or annee%400==0:
            return True
        else:
            return False
        
    #test
    annee=2025
    resultat=annee_bissextile
    if resultat:
        print("l annee est bissextile")
    else:
        print("l annee n est pas bissextile")
    
    ## exercice 3
    def discriminant(a,b,c):
        if a==0:
            raise ValueError("la valeur de a ne peut pas etre different de 0 ")
        else:
            deltat=b**2-4*a*c
        return deltat
    #qst 2
    def racine_unique(a,b):
        if a==0:
            raise ValueError("la valeur de a ne peut pas etre different de 0 ")
        else:
            return -b/2*a
    #qst 3
    def racine_double(a,b,delta,num):
        if num==1:
            x=(-b+Math.sqrt(delta))/2*a
            return x
        elif num==2:
            x2=(-b-Math.sqrt(delta))/2*a
        else:
            raise ValueError("la valeur de la racine doit etre 1 ou 2")
     #qst 4
    def str_equation(a,b,c):
        strequation=str(a)+"x^2"+str(b)+"x"+str(c)
        return strequation
    #qst 5
    def equation(a,b,c):
        delta=b**2-4*a*c
        if delta<0:
            print("pas de racine relle")
        elif delta==0:
            x=-b/2*a
            print("il admet une seule racine",x)
        elif delta>0:
            x1=(-b+math.sqrt(delta))/(2*a)
            x2=(-b-math.sqrt(delta))/(2*a)
            print("la fonction admet deux racines ",x1 , x2)
        else:
            print("aucune solution reelle")
        
        #fonction test
        def test_equation():
            print("Test 1")
            equation(1, -3, 2)  # Deux racines réelles
            print()
            print("Test 2")
            equation(1, -4, 4)  # Une racine réelle unique
            print()
            print("Test 3")
            equation(2, 2, 2)  # Pas de racine réelle
            print()
            print("Test 4")
            equation(3, 0, -12)  # Deux racines réelles
            print()
        test_equation() 


        ## exercice 4
        def date_est_valide(jour, mois, annee):
            if mois < 1 or mois > 12:
                return False
            if jour < 1:
                return False

            if mois in [1, 3, 5, 7, 8, 10, 12]:
                return jour <= 31
            elif mois in [4, 6, 9, 11]:
                return jour <= 30
            if est_bissextile(annee):
                return jour <= 29
            else:
                return jour <= 28
                   
        return True   

   #qst 2
        def saisie_date_naissance(annee,mois,jour):
            while true:
                try:
                    annee=int(input("Entrer votre annee de naissance"))
                    mois=int(input("Entrer votre mois de naissance"))
                    jour=int(input("Entrer votre jour de naissance"))
                    date_naissance=date(annee,mois,jour)
                    return date_naissance
                except ValueError:
                    print("les donnees que vous avez entre ne sont pas valides ")  

    #qst 3
        def age(date_naissance):
            today_date=date.today()
            today_annee=today_date.year
            naissance_year=date_naissance.year
            age=today_annee-naissance_year
            return age
    ##qst 4
        def est_majeur(date_naissance):
            today_date=date.today()
            today_annee=today_date.year
            naissance_year=date_naissance.year
            age=today_annee-naissance_year
            naissance_year= date_naissance.year
            if  age>=18:
                print("cette personne est majeure")
            else:
                print("cette personne n est pas majeure")
    ##qst 5
    def test_acces ():
         while true:
            try:
                date_naissance=int(input("veuillez entrer votre date de naissance"))
                date_naissance=date(year,month,day)
                date_today=date.today
                annee_today=date_today.year
                age=annee_today-annee_naissance
                if est_majeur(date_de_naissance):
                    print(f"Bonjour, vous êtes majeur, Accès autorisé.")
                else:
                    print(f"Désolé, vous n'êtes pas majeur, Accès interdit.")
                break  # Sortir de la boucle après une saisie valide
            except ValueError:
                print("Les données que vous avez saisies sont invalides. Veuillez réessayer.")
    test_acces()
