'''
importation des bibliothèque opencv et matplotlib

'''

import cv2 
import imutils
import numpy as np

'''
lienImage : variable contenant le lien vers l'iame à modifier
On enregistre l'image dans la variable img en appliquant le filtre de niveau de gris, on l'affiche et on l'enregistre
'''

def filterImgBTW():
    lienImage = str(input("entrer le lien de l'image à mettre en noir et blanc : "))
    nameNewImg = str(input("entrer le nom de votre nouvelle image : "))

    img = cv2.imread(lienImage, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(f'img/{nameNewImg}', img)
    
def rotateImg():
    lienImage = str(input("Entrer le chemin de l'image à pivoter : "))
    degreRotate = int(input("Entrer le nombre de degrés de rotation souhaité : "))
    nameNewImg = str(input("Entrer le nom de votre nouvelle image : "))

    image = cv2.imread(lienImage) ## charge l'image qui viens de lienImage

    (h, w) = image.shape[:2]
    cX, cY = w // 2, h // 2  ## recupe les dimensions de "image"

    M = cv2.getRotationMatrix2D((cX, cY), degreRotate, 1.0) # créer la matrice de rotation

    rotated = cv2.warpAffine(image, M, (w, h)) # rotate img 
    cv2.imwrite(f'img/{nameNewImg}', rotated)



