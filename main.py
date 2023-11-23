from filtre import * 
from log import * 
from CLI import * 
import sys 
import argparse
import os

def charger_images_dossier(chemin_dossier):
    liste_images = []

    # Parcourir tous les fichiers du dossier
    for nom_fichier in os.listdir(chemin_dossier):
        chemin_complet = os.path.join(chemin_dossier, nom_fichier)

        # Vérifier si le fichier est une image
        if os.path.isfile(chemin_complet) and any(chemin_complet.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg']):
            # Charger l'image avec OpenCV
            image = cv2.imread(chemin_complet)

            # Ajouter l'image à la liste
            liste_images.append(image)

    return liste_images

def afficher_info_filtres():
    # Dictionnaire contenant les informations sur chaque filtre disponible
    infos = {
        'btw': 'Convertit en noir et blanc',
        'dilate': 'Dilate l\'image',
        'flou': 'Applique un flou à l\'image',
        'rotate:<degré>': 'Fait pivoter l\'image selon le degré spécifié',
        'redim:<taille>': 'Redimensionne l\'image selon la taille spécifiée',
        'rwite:<texte>': 'Écrit du texte sur l\'image'
    }

    # Affichage des informations sur chaque filtre
    print("Liste de tous les filtres disponibles :")
    for key, value in infos.items():
        print(f"{key:<20} : {value}")

def main():
    parser = argparse.ArgumentParser(description='applique les filtres sur des images')

    # Argument pour afficher la liste de tous les filtres
    parser.add_argument('--info', action='store_true', help='Affiche la liste de tous les filtres')

    # Argument pour spécifier les filtres à appliquer sur l'image
    parser.add_argument('--filters', '-f', type=str, help='spécifié les filtres sur l\'image')

    # Argument pour spécifier le dossier d'entrée contenant l'image à modifier
    parser.add_argument('--input_folder', '-i', type=str, help='Input folder pour prendre l\'image a modifier')

    # Argument pour spécifier le dossier de sortie pour sauvegarder l'image modifiée
    parser.add_argument('--output_folder', '-o', type=str, help='Output folder pour sauvegarder l\'image')
        
    args = parser.parse_args()
    if args.info:
        afficher_info_filtres()
    elif args.filters and args.input_folder and args.output_folder:
        listeImg = charger_images_dossier(args.input_folder)
        nombreImg = len(listeImg)
        filters = args.filters.split('&')
        input_folder = args.input_folder
        output_folder = args.output_folder

        for filter_name in filters:
            if 'btw' in filter_name: 
                for i in range (nombreImg):
                    listeImg[i] = filterImgBTW(listeImg[i])
                    
            if 'dilate' in filter_name:
                for i in range (nombreImg):
                    listeImg[i] = filtreDilate(listeImg[i])
                    
            if 'flou' in filter_name:
                for i in range (nombreImg):
                    listeImg[i] = FilterFlouImg(listeImg[i])

            if filter_name.startswith('rotate:'):
                degree = int(filter_name.split(':')[1])
                for i in range (nombreImg):
                   listeImg[i] = rotateImg(listeImg[i], degree)
                
            if filter_name.startswith('redim:'):
                size = int(filter_name.split(':')[1])
                for i in range (nombreImg):
                    listeImg[i] = redimImg(listeImg[i], size)
                
            if filter_name.startswith('rwite:'):
                text = str(filter_name.split(':')[1])
                for i in range (nombreImg):
                    listeImg[i] = writeImg(listeImg[i], text)
                
        for i in range (nombreImg):
            cv2.imshow("fenetre",listeImg[i])
            cv2.waitKey(0)
            nb = str(i)
            cv2.imwrite(f'{output_folder}/imageFiltre{nb}.png', listeImg[i])
            
        if 'gif' in filter_name: 
                    listgif = gifFromImg(output_folder,output_folder)
            #else:
                #print(f"Filtre '{filter_name}' non reconnu.")
            #cv2.imwrite(f'img/{output_folder}', img)
        #print("Filtres appliqués avec succès aux images.")
    #else:
        #print("Utilisation: image-filter --filters <filters> --input_folder <input_folder> --output_folder <output_folder>")

if __name__ == "__main__":
    main()
