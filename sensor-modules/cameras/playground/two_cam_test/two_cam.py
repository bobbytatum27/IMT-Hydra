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
import time

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
        filename = os.path.join(IMG_DIR, f"test1.png")

        # capture, then show/save  an image
        ret, frame = cap.read()
        # cv2.imshow(filename, frame)
        cv2.imwrite(filename, frame)

        time.sleep(2)
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
    # directory for test images, deleted and replaced each run
    if os.path.exists(IMG_DIR):
        shutil.rmtree(IMG_DIR)
    os.mkdir(IMG_DIR)

    start = time.time()
    while True:
        dt = time.time() - start
        if (dt > 9):
            runWhiteCapCam()
            # reset the start time
            start = time.time()
        else:
            runFoamCam()

        time.sleep(3)
