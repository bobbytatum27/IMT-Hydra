import cv2
import os
import shutil
import argparse

import EasyPySpin

from ...cameras.bubble_cam.bubblecam_config import *

if __name__ == "__main__":
    print("WARNING! READ ME!")
    print("This test uses Bubble Cam Module's bubblecam.py implementation.")

    # prework for testing 
    try:
       pass
    except Exception as e:
        print("Exception occurred...")
        print(e)
    finally:
        pass
        # Release camera
        
        print("Completed Test...")