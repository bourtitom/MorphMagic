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

def filtreDilate(img):
    kernel = np.ones((5, 5), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1) # fonction d'opencv permettant la dilatation
    return img


def filterImgBTW(img):
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("fenetre3", img2)
    cv2.waitKey(0)
    return img2

'''
Fonction pour flouter l'image donnée
On enregistre l'image dans la variable img en appliquant le filtre de niveau de floutage, et on l'enregistre
'''
def FilterFlouImg(img):
    blurred_img = cv2.GaussianBlur(img, (15, 15), 0)
    return blurred_img

def rotateImg(image):
    degreRotate = int(input("Entrer le nombre de degrés de rotation souhaité : "))
    (h, w) = image.shape[:2]
    cX, cY = w // 2, h // 2  ## recupe les dimensions de "image"
    M = cv2.getRotationMatrix2D((cX, cY), degreRotate, 1.0) # créer la matrice de rotation
    rotated = cv2.warpAffine(image, M, (w, h)) # rotate img 
    return rotated

def redimImg(image):
    newSize = float(input("entrer le facteur de redimensionnement de l'image :"))
    largeur = int(image.shape[1] * newSize / 100)
    hauteur = int(image.shape[0] * newSize / 100)
    dimension = (largeur, hauteur)
    image=cv2.resize(image,dimension, interpolation = cv2.INTER_AREA)
    return image
 

def writeImg(image):
    TxtImage = str(input("Entrer le texte de l'image : "))
    position = (10, 50)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    fontColor = (255, 255, 0)
    thickness = 2
    writed = cv2.putText(image, TxtImage, position, font, fontScale, fontColor, thickness)
    return writed

def filterAll():
    test = 0
    listeImg = []
    while test == 0:
        lienImage = str(input("Entrer le chemin de l'image : "))
        
        if lienImage == "":
            test = 1

        else:
            img = cv2.imread(lienImage, 1) # transformation en noir et blanc
            listeImg.append(img)
    nombreImg = len(listeImg)
    
    while test < 7:
        print("si vous voulez appliquez le filtre noir et blanc, taper 1")
        print("si vous voulez appliquez le filtre flou, taper 2")
        print("si vous voulez appliquez le filtre dilate, taper 3")
        print("si vous voulez appliquez le filtre rotate, taper 4")
        print("si vous voulez appliquez le filtre resize, taper 5")
        print("si vous voulez appliquez le filtre rewrite, taper 6")
        print("si vous voulez enregistrer votre image, taper 7")
        test = int(input("entrer votre choix : "))
        if test == 1:
            for i in range (nombreImg):
                image = listeImg[i]
                image = filterImgBTW(image)
                listeImg[i] = image
                
        if test == 2:
            for i in range (nombreImg):
                image = listeImg[i]
                image = FilterFlouImg(image)
                listeImg[i] = image
                
        if test == 3:
            for i in range (nombreImg):
                image = listeImg[i]
                filtreDilate(image)
                listeImg[i] = image
                
        if test == 4:
            for i in range (nombreImg):
                image = listeImg[i]
                image = rotateImg(image)
                listeImg[i] = image
                
        if test == 5:
            for i in range (nombreImg):
                image = listeImg[i]
                image = redimImg(image)
                listeImg[i] = image
                
        if test == 6:
            for i in range (nombreImg):
                image = listeImg[i]
                image = writeImg(image)
                listeImg[i] = image
                
        if test == 7:
            nom_dossier = str(input("entrer le nom du dossier dans lequelle vous voulez enregistrer vos images : "))
            nameNewImg = str(input("Entrer le nom de votre nouvelle image : "))
            os.mkdir(nom_dossier)
            for i in range (nombreImg):
                image = listeImg[i]
                nb = str(i)

                cv2.imwrite(f'{nom_dossier}/{nameNewImg}{nb}.png', image)
        

filterAll()