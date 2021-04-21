from PIL import Image
import PIL.ImageOps    
def convert_and_save(name):
    img = Image.open('./test-images/raw/{}.png'.format(name)).resize((28,28),Image.ANTIALIAS)
    img = img.convert('L')
    #img = PIL.ImageOps.invert(img)
    img.save('./test-images/cropped/{}.png'.format(name))
convert_and_save("shirt")
convert_and_save("pants")
convert_and_save("shoes")
