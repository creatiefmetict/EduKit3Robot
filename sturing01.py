import RPi.GPIO as GPIO
# Import the GPIO Library 
import time
# Import the Time library 
import curses
stdscr = curses.initscr()
curses.start_color()
curses.noecho()
stdscr.keypad(True)
temp = 0

# Set the GPIO modes 

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 

# Set variables for the GPIO motor pins 

pinMotorAForwards = 10 
pinMotorABackwards = 9 
pinMotorBForwards = 8 
pinMotorBBackwards = 7 

Frequency = 20
DutyCycleA = 60
DutyCycleB = 60
Stop = 0


# Set the GPIO Pin mode 

GPIO.setup(pinMotorAForwards, GPIO.OUT) 
GPIO.setup(pinMotorABackwards, GPIO.OUT) 
GPIO.setup(pinMotorBForwards, GPIO.OUT) 
GPIO.setup(pinMotorBBackwards, GPIO.OUT) 

pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency) 
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency) 
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency) 
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)

pwmMotorAForwards.start(Stop) 
pwmMotorABackwards.start(Stop) 
pwmMotorBForwards.start(Stop) 
pwmMotorBBackwards.start(Stop)

# Turn all motors off 

def StopMotors(): 
  pwmMotorAForwards.ChangeDutyCycle(Stop) 
  pwmMotorABackwards.ChangeDutyCycle(Stop) 
  pwmMotorBForwards.ChangeDutyCycle(Stop) 
  pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Turn both motors forwards 

def Forwards(): 
  pwmMotorAForwards.ChangeDutyCycle(DutyCycleA) 
  pwmMotorABackwards.ChangeDutyCycle(Stop) 
  pwmMotorBForwards.ChangeDutyCycle(DutyCycleB) 
  pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Turn both motors backwards 

def Backwards(): 
  pwmMotorAForwards.ChangeDutyCycle(Stop) 
  pwmMotorABackwards.ChangeDutyCycle(DutyCycleA) 
  pwmMotorBForwards.ChangeDutyCycle(Stop) 
  pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)

# Turn Left

def TurnLeft():
  pwmMotorAForwards.ChangeDutyCycle(Stop) 
  pwmMotorABackwards.ChangeDutyCycle(DutyCycleA / 2) 
  pwmMotorBForwards.ChangeDutyCycle(DutyCycleB / 2) 
  pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Turn Right

def TurnRight():
  pwmMotorAForwards.ChangeDutyCycle(DutyCycleA / 2) 
  pwmMotorABackwards.ChangeDutyCycle(Stop) 
  pwmMotorBForwards.ChangeDutyCycle(Stop) 
  pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB / 2)

# Update Screen

def WriteScreen(toets):
  if toets == 'Forward':
    window1.addstr(0,10,"Vooruit", curses.color_pair(1))
    window1.addstr(2,0,"Links")
    window1.addstr(2,20,"Rechts")
    window1.addstr(4,10,"Achteruit")
    window1.addstr(2,10,"Stoppen")
  if toets == 'Back':
    window1.addstr(0,10,"Vooruit")
    window1.addstr(2,0,"Links")
    window1.addstr(2,20,"Rechts")
    window1.addstr(4,10,"Achteruit", curses.color_pair(1))
    window1.addstr(2,10,"Stoppen")
  if toets == 'Left':
    window1.addstr(0,10,"Vooruit")
    window1.addstr(2,0,"Links", curses.color_pair(1))
    window1.addstr(2,20,"Rechts")
    window1.addstr(4,10,"Achteruit")
    window1.addstr(2,10,"Stoppen")
  if toets == 'Right':
    window1.addstr(0,10,"Vooruit")
    window1.addstr(2,0,"Links")
    window1.addstr(2,20,"Rechts", curses.color_pair(1))
    window1.addstr(4,10,"Achteruit")
    window1.addstr(2,10,"Stoppen")
  if toets == 'Stop':
    window1.addstr(0,10,"Vooruit")
    window1.addstr(2,0,"Links")
    window1.addstr(2,20,"Rechts")
    window1.addstr(4,10,"Achteruit")
    window1.addstr(2,10,"Stoppen", curses.color_pair(1))
  window1.refresh()


win1_begin_x = 2
win1_begin_y = 2
win1_height = 5
win1_width = 30
window1 = curses.newwin(win1_height, win1_width, win1_begin_y, win1_begin_x)
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
win2_begin_x = 32
win2_begin_y = 2
win2_height = 8
win2_width = 30

window2 = curses.newwin(win2_height, win2_width, win2_begin_y, win2_begin_x)
window2.addstr(0,0,"pijl omhoog : vooruit", curses.color_pair(1))
window2.addstr(1,0,"pijl omlaag : achteruit")
window2.addstr(2,0,"pijl links  : draai links")
window2.addstr(3,0,"pijl rechts : draai rechts")
window2.addstr(4,0,"s : stoppen")
window2.addstr(5,0,"e : einde") 
window2.noutrefresh()
curses.doupdate()

while temp == 0:
  c = stdscr.getch()
  if c == curses.KEY_UP:
    Forwards()
    WriteScreen('Forward')
  if c == curses.KEY_DOWN:
    Backwards()
    WriteScreen('Back')
  if c == ord('s'):
    StopMotors()
    WriteScreen('Stop')
  if c == curses.KEY_LEFT:
    TurnLeft()
    WriteScreen('Left')
  if c == curses.KEY_RIGHT:
    TurnRight()
    WriteScreen('Right')
  if c == ord('e'):
    temp=1

GPIO.cleanup()
stdscr.keypad(False)
curses.echo()
curses.endwin()


