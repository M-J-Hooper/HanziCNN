from PIL import Image, ImageDraw, ImageFont
import common

imageSize = 100
fraction = 0.8
fontSize = int(fraction*imageSize)
font = ImageFont.truetype("ARIALUNI.ttf", fontSize)

def generateImages():
    f1 = open(common.trainPath, 'r', encoding='utf8')
    for line in f1:
        generateImage(line)
    f1.close()
    
    f2 = open(common.testPath, 'r', encoding='utf8')
    for line in f2:
        generateImage(line)
    f2.close()

    
def generateImage(line):
    c = line.split(',')[0]
    fp = 'images\\' + c + '.png'
    
    print(fp)
    
    img = Image.new('RGB', (imageSize, imageSize), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    w, h = draw.textsize(c, font=font) #use text size to centre char
    draw.text(((imageSize-w)/2,(imageSize-h)/2), c, (0,0,0), font=font)
    
    img.save(fp, 'PNG')

    
#generateImages();