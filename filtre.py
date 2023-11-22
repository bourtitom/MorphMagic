'''
importation des bibliothèque opencv et matplotlib

'''

import cv2 
import imutils
import numpy as np
import os

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


def writeImg():
    lienImage = str(input("Entrer le chemin de l'image : "))
    TxtImage = str(input("Entrer le texte de l'image : "))
    nameNewImg = str(input("Entrer le nom de votre nouvelle image : "))

    image = cv2.imread(lienImage)

    ## proprietie du texte sur l'image
    position = (10, 50)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    fontColor = (255, 255, 0)
    thickness = 2

    #on ecrit le texte sur l'image avec toute les proprietés
    writed = cv2.putText(image, TxtImage, position, font, fontScale, fontColor, thickness)

    cv2.imwrite(f'img/{nameNewImg}', writed)

