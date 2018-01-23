#!/usr/bin/env python
import RPi.GPIO as GPIO
from time import sleep
import time
import subprocess


GPIO.setmode(GPIO.BOARD)  # Set GPIO to Broadcom numbers not Pi numbers
buttonPin = 11          # Set pin numbers
ledPin    = 36

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Setup Button for taps
GPIO.setup(ledPin, GPIO.OUT) # setup LED

def hold():
	GPIO.output(ledPin, GPIO.HIGH)
	subprocess.call("png2pos -c -s 1 shutdown.png > /dev/usb/lp0", shell=True)
	subprocess.call("sync")
	subprocess.call(["shutdown", "-h", "now"])
	GPIO.output(ledPin, GPIO.LOW)

def tap():
	GPIO.output(ledPin, GPIO.HIGH)  # LED on while working
	subprocess.call(["python", "findpoem.py"]) # Print poem image
	print("Printing...")
	GPIO.output(ledPin, GPIO.LOW) # LED off while not working


# ---- Welcome Screen

subprocess.call("png2pos -c -s 1 startup.png > /dev/usb/lp0", shell=True)

# ---- Main Loop

prevButtonState = GPIO.input(buttonPin)  # Poll initial button state, should be 1
prevTime        = time.time()
tapEnable       = False
holdEnable      = False
holdTime        = 5
tapTime         = 0.01

while(True):
	buttonState = GPIO.input(buttonPin)  # Poll current button state and time
	t           = time.time()
	if buttonState != prevButtonState:   # Has button state changed, ie, a press?
		prevButtonState = buttonState    # save button state
		prevTime        = t
	else:
		if (t - prevTime) >= holdTime: # Button held for holdTime?
			if holdEnable == True:
				hold()
				holdEnable = False
				tapEnable = False
		elif (t - prevTime) >= tapTime:
			if buttonState == True:          # Has the button been released?
				if tapEnable == True:
					tap()
					tapEnable = False
					holdEnable = False
		else:
			tapEnable = True
			holdEnable = True

	if ((int(t) & 1) == 0) and ((t - int(t)) < 0.15):
		GPIO.output(ledPin, GPIO.HIGH)
	else:
		GPIO.output(ledPin, GPIO.LOW)