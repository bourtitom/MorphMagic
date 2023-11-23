'''
importation des bibliothèque opencv et matplotlib

'''

import cv2 
import numpy as np
import os
from PIL import Image

'''
lienImage : variable contenant le lien vers l'iame à modifier
On enregistre l'image dans la variable img en appliquant le filtre de niveau de gris, on l'affiche et on l'enregistre
'''

def filtreDilate(input_folder):
    kernel = np.ones((5, 5), np.uint8)
    # matrice 5px * 5px permettant de savoir si l'on doit étendre la couleur ou non
    #uint8 : entier non signé sur 8 bit, c'est utilisé par numpy dans le cadre de traitement d'image
    img = cv2.dilate(input_folder, kernel, iterations=1) # fonction d'opencv permettant la dilatation
    #cv2.imwrite(f'img/{output_folder}', img)
    return img

def filterImgBTW(input_folder):
    img = cv2.cvtColor(input_folder, cv2.COLOR_BGR2GRAY)
    return img

'''
Fonction pour flouter l'image donnée
On enregistre l'image dans la variable img en appliquant le filtre de niveau de floutage, et on l'enregistre
'''
def FilterFlouImg(img):

    blurred_img = cv2.GaussianBlur(img, (15, 15), 0)
    return blurred_img

def rotateImg(image, degree):

    (h, w) = image.shape[:2]
    cX, cY = w // 2, h // 2  ## recupe les dimensions de "image"

    M = cv2.getRotationMatrix2D((cX, cY), degree, 1.0) # créer la matrice de rotation

    rotated = cv2.warpAffine(image, M, (w, h)) # rotate img 
    return rotated

def redimImg(image, size):
    largeur = int(image.shape[1] * size / 100)
    hauteur = int(image.shape[0] * size / 100)
    dimension = (largeur, hauteur)
    image=cv2.resize(image,dimension, interpolation = cv2.INTER_AREA)
    return image
 

def writeImg(image,txt):

    ## proprietie du texte sur l'image
    position = (10, 50)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    fontColor = (255, 255, 0)
    thickness = 2

    #on ecrit le texte sur l'image avec toute les proprietés
    writed = cv2.putText(image, txt, position, font, fontScale, fontColor, thickness)

    return writed

def gifFromImg(input_folder, output_gif):
    images = []
    
    # on cherche tous les files dans le dossier qui a été listé 
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        
        # on check si c'est bien une image
        if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            img = Image.open(file_path)
            images.append(img)

    # Vérification s'il y a des images à convertir en GIF
    if images:
        images[0].save(output_gif, format='GIF', append_images=images[1:], save_all=True, duration=500, loop=0)
        print(f"GIF créé : {output_gif}")
    else:
        print("Aucune image trouvée dans le dossier.")