import cv2
import dlib #why?
from datetime import datetime

def detectFaces(image):
    self.detector = dlib.get_frontal_face_decector()