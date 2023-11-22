from filtre import * 
from log import * 
from CLI import * 
import sys 
import argparse

def main():
    parser = argparse.ArgumentParser(description='Apply filters to images')
    parser.add_argument('--filters', '-f', type=str, help='Specify filters to apply to images')
    parser.add_argument('--input_folder', '-i', type=str, help='Input folder containing initial images')
    parser.add_argument('--output_folder', '-o', type=str, help='Output folder to save modified images')

    args = parser.parse_args()

    if args.filters and args.input_folder and args.output_folder:
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
