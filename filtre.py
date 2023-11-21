'''
importation des bibliothèque opencv et matplotlib

'''

import cv2 
import numpy as np


'''
lienImage : variable contenant le lien vers l'iame à modifier
On enregistre l'image dans la variable img en appliquant le filtre de niveau de gris, on l'affiche et on l'enregistre
'''

def filtreDilate():
    lienImage = str(input("entrer le lien de l'image à mettre en noir et blanc : "))
    nameNewImg = str(input("entrer le nom de votre nouvelle image : "))
    kernel = np.ones((5, 5), np.uint8)
    # matrice 5px * 5px permettant de savoir si l'on doit étendre la couleur ou non
    #uint8 : entier non signé sur 8 bit, c'est utilisé par numpy dans le cadre de traitement d'image
    img = cv2.imread(lienImage, 1)
    img = cv2.dilate(img, kernel, iterations=1) # fonction d'opencv permettant la dilatation
    cv2.imwrite(f'img/{nameNewImg}', img)

def filterImgBTW():
    lienImage = str(input("entrer le lien de l'image à mettre en noir et blanc : "))
    nameNewImg = str(input("entrer le nom de votre nouvelle image : "))

    img = cv2.imread(lienImage, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(f'img/{nameNewImg}', img)
    

filterImgBTW()
filtreDilate()