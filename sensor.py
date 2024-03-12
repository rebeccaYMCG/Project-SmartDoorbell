from gpiozero import MotionSensor, Button
from datetime import datetime
from time import sleep 
import subprocess

motionSensor = MotionSensor(23) # these will be changed for actual GPIO pins
button = Button(13)

def captureImage():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    imagePath = f"motion_capture_{timestamp}.jpg"
    print(f"Capturing Image: {imagePath}")

    # send to SQL database to then send to phone ?

    # calls the face detection py
    subprocess.run(['python', 'faceDetection.py', imagePath])

try: 
    print("Motion detection system is active. Press Crtl+C to exit.")

    while True:
        if motionSensor.motion_detected:
            print("Motion Detected!")
            captureImage()

        if button.is_pressed: 
            print("Button Pressed!")
            captureImage()
    sleep(2)

except KeyboardInterrupt:
    print("Motion detection system stopped.") 

finally: 
    motionSensor.close()
    button.close()