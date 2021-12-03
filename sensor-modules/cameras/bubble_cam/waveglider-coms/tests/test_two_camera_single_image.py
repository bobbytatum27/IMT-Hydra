#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Single image capture test.

Author: Bobby Tatum
Email: rmtatum@ucsd.edu

Usage:
# in a new terminal
python test_capture_single_image.py

Adapted from code written by Imran Matin.
"""

import EasyPySpin
import cv2
import os
import shutil
from camera_config import *
import threading

IMG_DIR = "test_capture_single_image"
PROMPT = "Navigate to the open window. Press (q) to close the window."

# Cam name need to be confirmed with index
WC_CAM = 0
FOAM_CAM = 1

def initializeCamera(cam_num):
    """Initializes camera object with the correct settings."""
    cap = EasyPySpin.VideoCapture(cam_num)

    cap.set(cv2.CAP_PROP_EXPOSURE, EXPOSURE)
    cap.set(cv2.CAP_PROP_GAIN, GAIN)
    cap.set(cv2.CAP_PROP_BRIGHTNESS, BRIGHTNESS)
    cap.set(cv2.CAP_PROP_GAMMA, GAMMA)
    cap.set(cv2.CAP_PROP_FPS, FPS)
    cap.set(cv2.CAP_PROP_BACKLIGHT, BACKLIGHT)

    return cap

# cap is the camera reference
def captureImageTest(cam_name, cap):
    print("Starting Test on ", cam_name, "...")
    try:
        # capture an image
        ret, frame = cap.read()
        print(PROMPT)
        while True:
            # display the captured image
            cv2.imshow(filename, frame)
            key = cv2.waitKey(0)

            # break on pressing 'q'
            if key == ord("q"):
                break
    except Exception as e:
        print("Exception occurred...")
        print(e)
    finally:
        cv2.destroyAllWindows()
        # Release camera
        cap.release()
        print("Completed Test...")


def runWhiteCapCam():
    cap = initializeCamera(WC_CAM)
    captureImageTest("White Cap Cam", cap)

def runFoamCam():
    cap = initializeCamera(FOAM_CAM)
    captureImageTest("Foam Cam", cap)

if __name__ == "__main__":
    t1 = threading.Thread(target=runWhiteCapCam)
    t2 = threading.Thread(target=runFoamCam)
    t1.start()
    t2.start()
