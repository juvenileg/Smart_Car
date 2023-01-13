#import time
import Robot

#comanda_reala = ["Stânga", "Dreapta", "Înainte", "Oprește", "Accelerează", "Înapoi", "Lumini"]

LEFT_TRIM   = 0
RIGHT_TRIM  = 0

robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

def move(i):
        if i==0:
                robot.left(180,2)
        if i==1:
                robot.right(180,2)
        if i==2:
                robot.forward(180)
        if i==3:
                robot.stop()
        if i==4:
                robot.forward(250,5)
        if i==5:
                robot.backward(180,4)

def turn(i):
    robot.right(180,2)