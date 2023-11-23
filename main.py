from filtre import * 
from log import * 
from CLI import * 
import sys 
import argparse
import os
import log

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
    infos = {
        'btw': 'Convertit en noir et blanc',
        'dilate': 'Dilate l\'image',
        'flou': 'Applique un flou à l\'image',
        'rotate:<degré>': 'Fait pivoter l\'image selon le degré spécifié',
        'redim:<taille>': 'Redimensionne l\'image selon la taille spécifiée',
        'rwite:<texte>': 'Écrit du texte sur l\'image'
    }

    print("Liste de tous les filtres disponibles :")
    for key, value in infos.items():
        print(f"{key:<20} : {value}")

def main():
    parser = argparse.ArgumentParser(description='applique les filtres sur des images')
    parser.add_argument('--info', action='store_true', help='Affiche la liste de tous les filtres')
    parser.add_argument('--filters', '-f', type=str, help='spécifié les filtres sur l\'image')
    parser.add_argument('--input_folder', '-i', type=str, help='Input folder pour prendre l\'image a modifier')
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
                log.log(f'il y a {nombreImg} image qui ont été mise en noir et blanc ')
                    
            if 'dilate' in filter_name:
                for i in range (nombreImg):
                    listeImg[i] = filtreDilate(listeImg[i])
                log.log(f'il y a {nombreImg} image qui ont été dilaté ')
                    
            if 'flou' in filter_name:
                for i in range (nombreImg):
                    listeImg[i] = FilterFlouImg(listeImg[i])
                log.log(f'il y a {nombreImg} image qui ont été flouté ')

            if filter_name.startswith('rotate:')and not filter_name.endswith('rotate:'):
                degree = int(filter_name.split(':')[1])

                if degree > 0:
                    for i in range (nombreImg):
                        listeImg[i] = rotateImg(listeImg[i], degree)
                log.log(f'il y a {nombreImg} image qui ont fait une rotation ')

                
            if filter_name.startswith('redim:')and not filter_name.endswith('redim:'):
                size = int(filter_name.split(':')[1])

                if size > 0:
                    for i in range (nombreImg):
                        listeImg[i] = redimImg(listeImg[i], size)
                log.log(f'il y a {nombreImg} image qui ont été redimensioné ')

                
            if filter_name.startswith('rwrite:')and not filter_name.endswith('rwrite:'):
                text = str(filter_name.split(':')[1])
                for i in range (nombreImg):
                    listeImg[i] = writeImg(listeImg[i], text)
                log.log(f'il y a {nombreImg} image sur lequel on a écrit ')
            
            if  'aqua' in filter_name:
                for i in range (nombreImg):
                    listeImg[i] = aquaImg(listeImg[i])
                log.log(f'il y a {nombreImg} image sur lequel on a apliqué le filtre aquarelle ')
                
        for i in range (nombreImg):
            cv2.imshow("fenetre",listeImg[i])
            cv2.waitKey(0)
            nb = str(i)
            try:
                cv2.imwrite(f'{output_folder}/imageFiltre{nb}.png', listeImg[i])

            except:
                print("nous n'avons pas réussi a créer les images que vous souhaitez, le dossier n'existe pas")
            
        if 'gif' in filter_name:
            try: 
                listgif = gifFromImg(output_folder)
            except:
                print("le gif n'a pas réussi à être créé")
            #else:
                #print(f"Filtre '{filter_name}' non reconnu.")
            #cv2.imwrite(f'img/{output_folder}', img)
        #print("Filtres appliqués avec succès aux images.")
    #else:
        #print("Utilisation: image-filter --filters <filters> --input_folder <input_folder> --output_folder <output_folder>")

if __name__ == "__main__":
    main()