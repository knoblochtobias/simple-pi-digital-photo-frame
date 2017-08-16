#!/bin/python  
# Simple script for shutting down the raspberry Pi at the press of a button.  
# by Inderpreet Singh  
  
import RPi.GPIO as GPIO  
import time  
import os  
from time import gmtime, strftime

# Save script start time to log (start it in rc.local)
text_file = open("/home/pi/simple-pi-digital-photo-frame/info.log", "a")
text_file.write("%s: boot\n" % strftime("%Y-%m-%d %H:%M:%S", gmtime()))
text_file.close()

# Use the Broadcom SOC Pin numbers
# Setup the Pin with Internal pullups enabled and PIN in reading mode.  
GPIO.setmode(GPIO.BCM)  
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)  
 
# Our function on what to do when the button is pressed  
def Shutdown(channel):
    text_file = open("/home/pi/simple-pi-digital-photo-frame/info.log", "a")
    text_file.write("%s: shutdown\n" % strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    text_file.close()
    os.system("sudo shutdown -h now")  
 
# Add our function to execute when the button pressed event happens  
GPIO.add_event_detect(18, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)  
 
# Now wait!  
while 1:  
    time.sleep(1)
