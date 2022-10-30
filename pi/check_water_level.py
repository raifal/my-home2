import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering


GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
if GPIO.input(10) == GPIO.HIGH:
    print("Higher water line - WATER!!!!!!!!!!!")
else:
    print("Higher water line - no worries")

GPIO.cleanup()


time.sleep(4)

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
if GPIO.input(12) == GPIO.HIGH:
    print("Lower water line - WATER!!!!!!!!!!!")
else:
    print("Lower water line - no worries")

GPIO.cleanup()
