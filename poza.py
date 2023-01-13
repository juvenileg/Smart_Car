from PIL import Image, ImageFilter, ImageEnhance
from picamera import PiCamera
from time import sleep, time
import pytesseract
#import cv2
import io
import re
from lumini import procesare, aprinde
import ecran
import motor
import vars
import RPi.GPIO as GPIO

comanda = ["stanga", "dreapta", "inainte", "opreste", "accelereaza", "inapoi", "lumini", "final"]
comanda_reala = ["Stânga", "Dreapta", "Înainte", "Oprește", "Accelerează", "Înapoi", "Lumini", "Final"]
cautarecomanda =  ["tang", "reapt", "naint", "prest", "celerea", "napo", "umin", "ina"]
a = 0
b = 0
x = 0
y = 0
x1 = 0
y1 = 0
vit = 2

camera = PiCamera()
ecran.start("Aștept comandă...")

while vars.fin:
		#if vars.fin:
		#        break
		camera.start_preview()

		procesare(1)
		sleep(1)
		camera.capture('/home/pi/Proiect/Imagini/imagine.jpg')
		camera.stop_preview()

		procesare(0)

		imgine = Image.open("/home/pi/Proiect/Imagini/imagine.jpg")
		imgine = imgine.convert("RGBA")
		dateimagine = []
		dateactuale = imgine.getdata()

		for item in dateactuale:
			if item[0] < 70 and item[1] < 70 and item[2] < 70:
				dateimagine.append(item)
			else:
				dateimagine.append((255, 255, 255))
		imgine.putdata(dateimagine)
		#imgine.save('/home/pi/Proiect/Imagini/imagine_noua1.jpg')

		imgine = imgine.filter(ImageFilter.MedianFilter())
		#imgine.save('/home/pi/Proiect/Imagini/imagine_noua2.jpg')
		enhancer = ImageEnhance.Contrast(imgine)
		#imgine.save('/home/pi/Proiect/Imagini/imagine_noua3.jpg')
		imgine = enhancer.enhance(2)
		#imgine.save('/home/pi/Proiect/Imagini/imagine_noua4.jpg')
		imgine = imgine.convert('1')
		imgine.save('/home/pi/Proiect/Imagini/imagine_noua.jpg')

		text = pytesseract.image_to_string(Image.open('/home/pi/Proiect/Imagini/imagine_noua.jpg'),config='-c tessedit_char_whitelist=acdefgilmnoprstuz -psm 6')
		#print(text)

		for i in range(0, len(cautarecomanda)):
			searchstr= '[a-z]' + cautarecomanda [i] + '[a-z]'
			#searchstr= '$' + cautarecomanda [i] + '$'
			if re.search(searchstr, text.lower()):
				if vars.fwd_start > 0:
					varFile= open("vars.log", "r")
					wholeStr= varFile.read()
					ls= wholeStr.splitlines()
					index= ls[0].index(":")
					vars.fwd_end= int(ls[0][index+1:])
					if vars.fwd_end == 0:
						vars.fwd_end = time()
					else:
						y = -y
						y1 = y
					vars.fwd_time = abs(vars.fwd_end - vars.fwd_start)
					y = y + round(vars.fwd_time)
					y1 = y
					vars.fwd_time = vars.fwd_end = vars.fwd_start = 0
				b = b + 1
				print ("Comanda gasită: {}".format(comanda[i]))
				if i == 7:
					vars.fin = False
					varFile= open("vars.log", "w")
					varFile.write("fwd_End:0\nfin:False")
					varFile.close()
					ecran.final(a,b,x*vit,y*vit)
					break
				ecran.afiseaza(comanda_reala[i])
				if i == 0:
					x = y1
					y = -x1
					x1 = x
					y1 = y
				if i == 1:
					x = -y1
					y = x1
					x1 = x
					y1 = y
				if i == 2:
					vars.fwd_start = time()
				if i == 4:
					y = y + 5*1.4
					y1 = y
				if i == 5:
					y = y - 4
					y1 = y
				if i == 6:
					a = a + 1
					aprinde(a)
				else:
					motor.move(i)
				break

