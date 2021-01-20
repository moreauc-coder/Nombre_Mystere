import random
"""
on demande le niveau que veut le joueur
"""
niveau = 0
partie = "oui"

while partie.lower() == "oui":
    while not 0 < niveau < 5:

        niveau = input("Bonjour choisissez le niveau de difficulté, le niveau 1 (1-10) le niveau 2 (1-100)"
                       "le niveau 3 (1-1000) et le niveau 4(modulable) pour cela tapez 1, 2 , 3 ou 4:")
        try:
            niveau = int(niveau)
        except:
            print("il faut taper un chiffre.")
            niveau = 0
        else:
            if 0 < niveau < 5:
                break
            else:
                print("le chiffre doit être compris entre 1 et 4")


    if niveau == 1:
        nb_mystere = random.randint(1,10) #nombre random entre 1 et 10
        nb_maximum = 10
    elif niveau == 2:
        nb_mystere = random.randint(1,100) #nombre random entre 1 et 100
        nb_maximum = 100
    elif niveau == 3:
        nb_mystere = random.randint(1, 1000)  # nombre random entre 1 et 1000
        nb_maximum = 1000
    elif niveau == 4:
        nb_maximum = 0
        while not nb_maximum > 0:
            nb_maximum = input("selectionne le nombre que tu veux: ")
            try:
                nb_maximum = int(nb_maximum)
            except:
                print("mets un nombre")
                nb_maximum = 0
    nb_mystere = random.randint(1, nb_maximum)  # nombre random entre 1 et le nombre que tu veux

    #print(nb_mystere)

    nb_joueur = 0
    nb_coup = 0

    while not nb_joueur == nb_mystere:
        nb_joueur = input("quel est le nombre mystère? ")

        try:
            nb_joueur = int(nb_joueur)
            nb_coup = nb_coup + 1
        except:
            print("Il faut taper un nombre.")
        else:
            if 0 < nb_joueur <= nb_maximum:
                if nb_joueur < nb_mystere:
                    print("c'est plus!")
                elif nb_joueur > nb_mystere:
                    print("c'est moins !")
                else:
                    print("bravo!!")
            else:
                nb_coup = nb_coup - 1
                print("il faut taper un nombre entre 1 et "+str(nb_maximum))
    print("tu as trouvé le nombre mystere en " + str(nb_coup) + " coups")
    partie_fin = ""
    while not partie_fin.lower() == "oui":
        partie_fin = input("si tu veux recommencer tape oui si tu ne veux pas tape non: ")
        if partie_fin.lower() == "oui":
            print("c'est reparti pour un tour!")
            partie = partie_fin
            niveau = 0
        elif partie_fin.lower() == "non":
            print("merci, à la prochaine")
            partie = partie_fin
            break
        else:
            print("il faut soit taper oui ou soit taper non , c'est trop compliqué?")
