from PIL import Image

im = Image.open('prog10/image.png')
for pixel in list(im.getdata()):
    print(pixel)
