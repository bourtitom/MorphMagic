'''
importation des bibliothèque opencv et matplotlib

'''

import cv2 
import numpy as np
import os

'''
lienImage : variable contenant le lien vers l'iame à modifier
On enregistre l'image dans la variable img en appliquant le filtre de niveau de gris, on l'affiche et on l'enregistre
'''

def filterImgBTW():
    lienImage = str(input("entrer le lien de l'image à mettre en noir et blanc : "))
    nameNewImg = str(input("entrer le nom de votre nouvelle image : "))

    img = cv2.imread(lienImage, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(f'img/{nameNewImg}', img)
   

filterImgBTW()
 
'''
Fonction pour flouter l'image donnée
On enregistre l'image dans la variable img en appliquant le filtre de niveau de floutage, et on l'enregistre
'''
def FilterFlouImg():
    lienImage = str(input("Entrez le lien de l'image à flouter : "))
    nameNewImg = str(input("Entrez le nom de votre nouvelle image : "))

    img = cv2.imread(lienImage)
    blurred_img = cv2.GaussianBlur(img, (15, 15), 0)
    cv2.imwrite(f'img/{nameNewImg}', blurred_img)

FilterFlouImg()

