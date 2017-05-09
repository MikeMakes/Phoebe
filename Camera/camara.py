sudo apt-get update
sudo apt-get upgrade

sudo apt-get install python-picamera

#!/usr/bin/python
import time
import picamera

with picamera.PiCamera() as picam:
    picam.start_preview()
    time.sleep(10)
    picam.stop_preview()
    picam.close()