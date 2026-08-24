import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
            sys.exit('Too many command-line arguments')
    elif not sys.argv[1].lower().endswith(('.jpg', '.jpeg', '.png')) or not sys.argv[2].lower().endswith(('.jpg', '.jpeg', '.png')):
        sys.exit('Incorrect extension')
    elif sys.argv[1].split('.')[-1] != sys.argv[2].split('.')[-1]:
        sys.exit('Inconsistent extensions')

    try:
        image = Image.open(sys.argv[1])
        shirt = Image.open('shirt.png')
    except FileNotFoundError:
        sys.exit('File not found')
    else:
        cropped_image = ImageOps.fit(image, shirt.size)

        cropped_image.paste(shirt, box=(0,0), mask=shirt)

        cropped_image.save(sys.argv[2])

if __name__ == '__main__':
    main()