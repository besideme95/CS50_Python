import sys
import os
from PIL import Image, ImageOps

#create the command line
if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')


elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')


elif len(sys.argv) == 3:
    extensions = ['.jpeg','.jpg','.png']
    extension1 = os.path.splitext(sys.argv[1])
    extension2 = os.path.splitext(sys.argv[2])


    if extension1[1] == extension2[1] and extension1[1] in extensions:
        try:
            user_image = Image.open(sys.argv[1])
        except:
            sys.exit('Invalid output')


        shirt = Image.open("shirt.png")
        size = shirt.size
        user_image = ImageOps.fit(user_image, size)
        user_image.paste(shirt, shirt)
        user_image.save(sys.argv[2])


    elif extension1[1] != extension2[1] and extension1[1] in extensions and extension2[1] in extensions:
        sys.exit('Input and output have different extensions')

    elif extension1[1] not in extensions or extension2[1] not in extensions:
        sys.exit('Invalid output')

    else:
        sys.exit('Input does not exist')
