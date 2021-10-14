import cv2
from imutils.video import WebcamVideoStream
import time
import random

class VideoCamera(object):
    def __init__(self):
        self.stream = WebcamVideoStream(src=0).start() 
        #start streaming of webcam

    def __del__(self):
        self.stream.stop()

    def get_frame(self):
        image = self.stream.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        # if curr_time - last_recorded_time >= 5.0:
        #     cv2.imwrite('logs/img'+str(random.randint(0, 100))+'.png', image)
        data = []
        data.append(jpeg.tobytes())
        return data
        #returns the frame of the webcam

