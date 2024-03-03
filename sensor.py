from gpiozero import MotionSensor
from datetime import datetime
from time import sleep 

motionSensor = MotionSensor(23)

def captureImage():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    imagePath = f"motion_capture_{timestamp}.jpg"

    #create a function that will tell individual that a pic was taken

try: 
    print("Motion detection system is active. Press Crtl+C to exit.")

    while True:
        if motionSensor.motion_detected:
            print("Motion Detected!")
            captureImage()
    sleep(2)

except KeyboardInterrupt:
    print("Motion detection system stopped.") 

finally: 
    motionSensor.close()