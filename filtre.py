'''
importation des bibliothèque opencv et matplotlib

'''

import cv2 
import numpy as np

'''
lienImage : variable contenant le lien vers l'iame à modifier
On enregistre l'image dans la variable img en appliquant le filtre de niveau de gris, on l'affiche et on l'enregistre
'''

lienImage = str(input("entrer le lien de l'image à mettre en noir et blanc"))
img = cv2.imread(lienImage, cv2.IMREAD_GRAYSCALE)
cv2.imshow("fenetre", img)
cv2.waitKey(0)
cv2.imwrite('myImage.png', img)