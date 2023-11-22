from filtre import * 
from log import * 
from CLI import * 
import sys 
import argparse
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
        filters = args.filters.split('&')
        input_folder = args.input_folder
        output_folder = args.output_folder

        for filter_name in filters:
            if filter_name == 'btw':
                filterImgBTW(input_folder, output_folder)
            elif filter_name == 'dilate':
                filtreDilate(input_folder, output_folder)
            elif filter_name == 'flou':
                FilterFlouImg(input_folder, output_folder)

            elif filter_name.startswith('rotate:'):
                degree = int(filter_name.split(':')[1])
                rotateImg(input_folder, output_folder, degree)
            elif filter_name.startswith('redim:'):
                size = int(filter_name.split(':')[1])
                rotateImg(input_folder, output_folder, size)
            elif filter_name.startswith('rwite:'):
                text = str(filter_name.split(':')[1])
                writeImg(input_folder, output_folder, text)            
            else:
                print(f"Filtre '{filter_name}' non reconnu.")

        print("Filtres appliqués avec succès aux images.")
    else:
        print("Utilisation: image-filter --filters <filters> --input_folder <input_folder> --output_folder <output_folder>")

if __name__ == "__main__":
    main()
