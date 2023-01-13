from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
from font_intuitive import Intuitive
from font_source_serif_pro import SourceSerifProSemibold
from font_source_sans_pro import SourceSansProSemibold

inky_display = InkyPHAT("black")
inky_display2 = InkyPHAT("yellow")
inky_display.set_border(inky_display.WHITE)


#font = ImageFont.truetype(FredokaOne, 18)
#font2 = ImageFont.truetype("/home/pi/Proiect/Resurse/ChiKareGo.ttf", 18)
#font = ImageFont.truetype("/home/pi/Proiect/Resurse/ChiKareGo.ttf", 23)

font = ImageFont.truetype(HankenGroteskBold, 22)
font2 = ImageFont.truetype(HankenGroteskBold, 18)
font3 = ImageFont.truetype(HankenGroteskBold, 16)

directie = ["Stânga", "Dreapta", "Înainte", "Înapoi"]
#mesaj = "Merge??"

def final(a,b,x,y):
                s = directie[0]
                i = directie[2]
                if x>0:
                        s = directie[1]
                if y>0:
                        i = directie[3]
                img = Image.open("/home/pi/Proiect/Imagini/electronica.png")
                draw = ImageDraw.Draw(img)
                draw.text((105, 5), "Mulțumesc", inky_display.BLACK, font)
                draw.text((107, 25), str(abs(a)) + " apelări", inky_display.YELLOW, font3)
                draw.text((135, 39), "lumini", inky_display.YELLOW, font3)
                draw.text((107, 53), str(abs(b)) + " comenzi", inky_display.YELLOW, font3)
                draw.text((107, 67), str(abs(x)) + " cm " + s, inky_display.YELLOW, font3)
                draw.text((107, 81), str(abs(y)) + " cm " + i, inky_display.YELLOW, font3)
                inky_display2.set_image(img)
                inky_display2.show()

def afiseaza(mesaj):
                #print("/home/pi/Proiect/Imagini/" + mesaj + ".png")
                #img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
                img = Image.open("/home/pi/Proiect/Imagini/" + mesaj + ".png")
                draw = ImageDraw.Draw(img)
                draw.text((100, 50), mesaj, inky_display.BLACK, font)
                inky_display.set_image(img)
                inky_display.show()

def eroare(mesaj):
        img = Image.open("/home/pi/Proiect/Imagini/electronica.png")
        draw = ImageDraw.Draw(img)
        draw.text((112, 5), "STOP!!", inky_display.BLACK, font)
        draw.text((112, 25), "în " + mesaj + " cm", inky_display.BLACK, font=font2)
        draw.text((112, 45), "Pericol", inky_display.BLACK, font=font2)
        draw.text((115, 65), "Impact", inky_display.BLACK, font=font2)
        inky_display.set_image(img)
        inky_display.show()

def start(mesaj):
        img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
        draw = ImageDraw.Draw(img)
        draw.text((30, 35), mesaj , inky_display.BLACK, font)
        inky_display.set_image(img)
        inky_display.show()

#final(2,3,4,-5)
#afiseaza(mesaj)