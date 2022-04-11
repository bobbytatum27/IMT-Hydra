import cv2
import os
import shutil
import argparse

import EasyPySpin

from ...cameras.bubble_cam.bubblecam_config import *

IMAGE_DIR = './single_image_test_results/'
PROMPT = "Navigate to the open window. Press (s) to save the image and close the window, (q) to not save the image and close the window."

def initializeCamera():
    """Initializes camera object with the correct settings."""
    cap = EasyPySpin.VideoCapture(1)

    cap.set(cv2.CAP_PROP_EXPOSURE, EXPOSURE)
    cap.set(cv2.CAP_PROP_GAIN, GAIN)
    cap.set(cv2.CAP_PROP_BRIGHTNESS, BRIGHTNESS)
    cap.set(cv2.CAP_PROP_GAMMA, GAMMA)
    cap.set(cv2.CAP_PROP_FPS, FPS)
    cap.set(cv2.CAP_PROP_BACKLIGHT, BACKLIGHT)

    return cap

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--interactive', dest='interactive', action='store_true', default=False,
                        help='interact with the captured image before saving/discarding')
    return parser.parse_args()

if __name__ == "__main__":
    print("WARNING! READ ME!")
    print("This test does not utilize the Bubble Cam Module's bubblecam.py implementation.")
    print("This test is only a sanity check that the FLIR camera can capture images programmatically.")
    print("As such, treat the results of this test merely as a baseline for the camera's functional status.\n")

    args = parse_args()
    print("Starting Test...")

    # initialize the camera with specified settings
    cap = initializeCamera()
    try:
        # create new images directory each time test starts up
        if os.path.exists(IMG_DIR):
            shutil.rmtree(IMG_DIR)
        os.mkdir(IMG_DIR)

        # name of image to save
        filename = os.path.join(IMG_DIR, f"test_photo.png")

        # capture an image
        ret, frame = cap.read()
        print(PROMPT)
        while True:
            # display the captured image
            cv2.imshow(filename, frame)
            key = cv2.waitKey(0)

            # only display img if interactive flag is passed!
            if args['interactive']:
                # save on pressing 's'
                if key == ord("s"):
                    # write the image to disk
                    cv2.imwrite(filename, frame)
                    break
                # break on pressing 'q'
                if key == ord("q"):
                    break
            else:
                cv2.imwrite(filename, frame)
    except Exception as e:
        print("Exception occurred...")
        print(e)
    finally:
        cv2.destroyAllWindows()
        # Release camera
        cap.release()
        print("Completed Test...")