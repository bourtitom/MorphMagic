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
    # Dictionnaire contenant les informations sur chaque filtre disponible
    infos = {
        'btw': 'Convertit en noir et blanc',
        'dilate': 'Dilate l\'image',
        'flou': 'Applique un flou à l\'image',
        'rotate:<degré>': 'Fait pivoter l\'image selon le degré spécifié',
        'redim:<taille>': 'Redimensionne l\'image selon la taille spécifiée',
        'rwite:<texte>': 'Écrit du texte sur l\'image',
        'aqua': 'Ajoute un filtre aquarelle',
        'gif': 'Utilise toutes les images que l\'on a modifié pour en faire un gif' 
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
    
    parser.add_argument('--config', '-c',  type = str, help ='pour ajouter les filtres depuis un fichier texte')
        
    args = parser.parse_args()
    
    '''
    si jamais l'utilisateur rentre info comme commande, il va voir l'ensemble des commandes et ce qu'elles font
    Sinon, si l'utilisateur remplit tous les champs pour pouvoir appliquer un filtre (les nom des filtres, l'emplacement du dossier source et du dossier receveur)
    on transforme la chaine de caractère filtres en une liste contenant chacun des chaines de caractère, chacune portant le nom d'un filtre
    si jamais le filtre correspond, on l'applique
    Une fois tous les filtres appliqués, on affiches le résultat à l'utilisateur et l'on enregistre les images dans le dossier receveur
    si jamais l'utilisateur voulait créer un gif, on va se servir des images ainsi créer et les assembles pour faire notre gif
    '''
    
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
                
    elif args.config:
        f = open(args.config, "r")
        ligne = f.readline() # lecture de la première ligne contenant le lien du dossier source des images
        ligne = ligne.replace("\n", "")
        
        ligne2 = f.readline() # lecture de la deuxième ligne contenant le lien du dossier receveur des images
        ligne2 = ligne2.replace("\n", "")
        
        ligne3 = f.readline() #lecture de la troisième ligne contenant l'ensemble des filtres que l'on voudra appliquer à nos images
        ligne3 = ligne3.replace("\n", "")
        
        filters = ligne3.split('&') # ondécoupe notre chaine de caractère en plusieurs autres chaine de caractère lorsque & les sépares
        listeImg = charger_images_dossier(ligne)
        nombreImg = len(listeImg)
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
                cv2.imwrite(f'{ligne2}/imageFiltre{nb}.png', listeImg[i])

            except:
                print("nous n'avons pas réussi a créer les images que vous souhaitez, le dossier n'existe pas")
            
        if 'gif' in filter_name:
            try: 
                listgif = gifFromImg(ligne2)
            except:
                print("le gif n'a pas réussi à être créé")
    f.close()
        
        

if __name__ == "__main__":
    main()