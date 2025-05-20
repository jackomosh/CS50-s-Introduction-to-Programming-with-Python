from PIL import Image
from PIL import ImageFilter

def main():
    
    with Image.open("esafe.png") as img:

        img = img.rotate(90)
        # img = img.filter(ImageFilter.BLUR)
        img.save("esafe1.png")

main()