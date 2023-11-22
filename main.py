from filtre import * 
from log import * 
from CLI import * 
import sys 

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Commandes :blush:")
        print("Créer un film : pip3 main.py create <name> <genre> <fav>")
        print("afficher tous les films: pip3 main.py -lm")
        print("afficher tous les favoris: pip3 main.py -fv")
        print("afficher la liste de films pour un genre donné: pip3 main.py -g <genre>")

    else:
            commande = sys.argv[1]

            if commande == "-fd":
                filtreDilate()
            elif commande == "-fmBtW":
                filterImgBTW()
            elif commande == "-ff":
                FilterFlouImg()
            elif commande == "-roi":
                rotateImg()
            elif commande == "-rwi":
                rotateImg()
            else:
                print("Error Commande")