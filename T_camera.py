import picamera
from time import sleep


camera = picamera.PiCamera()

camera.start_preview()
sleep(5)
camera.capture('frige.jpg')


#test = open('fridge.jpg','wb')
#sleep(3)
#camera.capture(test)

#test.close()


