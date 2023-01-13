import RPi.GPIO as GPIO
import time
import ecran
import lumini
import motor

PIN_TRIGGER = 5
PIN_ECHO = 6

GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

GPIO.output(PIN_TRIGGER, GPIO.LOW)

varFile= open("vars.log", "w")
varFile.write("fwd_end:0\nfin:True")
varFile.close()

fin = "True"

while fin == "True":
	#print ("Resetarea senzorului")
	#if vars.fin:
	#               break
	time.sleep(1)
	#print ("Calculam distanta")
	GPIO.output(PIN_TRIGGER, GPIO.HIGH)
	time.sleep(0.00001)

	GPIO.output(PIN_TRIGGER, GPIO.LOW)

	while GPIO.input(PIN_ECHO)==0:
		pulse_start_time = time.time()
	while GPIO.input(PIN_ECHO)==1:
		pulse_end_time = time.time()

	pulse_duration = pulse_end_time - pulse_start_time
	distance = round(pulse_duration * 17150, 2) #viteza sunetului aproximativ 343m/s = 34300 cm/s, impartim la 2 deoarece pulsul se duce si se intoarce, deci parcurge distanta de 2 ori, si afisam doar ultimele 2 decimale.

	text = "Distanta este:" + str(distance) + "cm"
	text2 = str(distance)
	#print(text)

	if distance<30 and distance>10:
		varFile= open("vars.log", "r")
		wholeStr= varFile.read()
		ls= wholeStr.splitlines()
		index= ls[1].index(":")
		fin= ls[1][index+1:]
		print(fin)
		if fin == "False":
			break
		motor.move(3)
		fwd_end = round(time.time())
		#print(str(vars.fwd_end))
		ecran.eroare(text2)
		lumini.danger(1)
		motor.turn(1)
		varFile.close()
		varFile= open("vars.log", "w")
		varFile.write("fwd_End:" + str(fwd_end) + "\nfin:True")
		varFile.close()
#else:
#ecran.afiseaza(text)

