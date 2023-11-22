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

def filtreDilate(input_folder, output_folder):
    kernel = np.ones((5, 5), np.uint8)
    # matrice 5px * 5px permettant de savoir si l'on doit étendre la couleur ou non
    #uint8 : entier non signé sur 8 bit, c'est utilisé par numpy dans le cadre de traitement d'image
    img = cv2.imread(input_folder, 1)
    img = cv2.dilate(img, kernel, iterations=1) # fonction d'opencv permettant la dilatation
    cv2.imwrite(f'img/{output_folder}', img)

def filterImgBTW(input_folder, output_folder):
    img = cv2.imread(input_folder, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(f'img/{output_folder}', img)

'''
Fonction pour flouter l'image donnée
On enregistre l'image dans la variable img en appliquant le filtre de niveau de floutage, et on l'enregistre
'''
def FilterFlouImg(input_folder, output_folder):

    img = cv2.imread(input_folder)
    blurred_img = cv2.GaussianBlur(img, (15, 15), 0)
    cv2.imwrite(f'img/{output_folder}', blurred_img)

def rotateImg(input_folder, output_folder, degree):

    image = cv2.imread(input_folder) ## charge l'image qui viens de lienImage

    (h, w) = image.shape[:2]
    cX, cY = w // 2, h // 2  ## recupe les dimensions de "image"

    M = cv2.getRotationMatrix2D((cX, cY), degree, 1.0) # créer la matrice de rotation

    rotated = cv2.warpAffine(image, M, (w, h)) # rotate img 
    cv2.imwrite(f'img/{output_folder}', rotated)

def redimImg(input_folder, output_folder, size):
    image = cv2.imread(input_folder)
    largeur = int(image.shape[1] * size / 100)
    hauteur = int(image.shape[0] * size / 100)
    dimension = (largeur, hauteur)
    image=cv2.resize(image,dimension, interpolation = cv2.INTER_AREA)
    cv2.imwrite(f'img/{output_folder}', image)
 

def writeImg(input_folder, output_folder,txt):

    image = cv2.imread(input_folder)

    ## proprietie du texte sur l'image
    position = (10, 50)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    fontColor = (255, 255, 0)
    thickness = 2

    #on ecrit le texte sur l'image avec toute les proprietés
    writed = cv2.putText(image, txt, position, font, fontScale, fontColor, thickness)

    cv2.imwrite(f'img/{output_folder}', writed)

