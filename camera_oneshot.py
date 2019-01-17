#! /usr/bin/env python

import picamera
import time
import datetime

timestr = time.strftime("%Y-%m-%d %H:%M:%S")

print("Make a photo...")
camera = picamera.PiCamera()
camera.capture('/home/pi/motion_camera/image_{}.jpg'.format(timestr))
print("Photo taken! image_{}.jpg".format(timestr))
