import cv2
import os
import shutil
import argparse

from ...compositions.bubblecam.bubblecam_config import *
from ...compositions.bubblecam.bubblecam import BubbleCam
from ...compositions.bubblecam.logger import Logger

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--interactive', dest='interactive', action='store_true', default=False,
                        help='interact with the captured image before saving/discarding')
    return parser.parse_args()

if __name__ == "__main__":

    IMAGE_DIR = './single_image_test_results/'
    PROMPT = "Navigate to the open window. Press (s) to save the image and close the window, (q) to not save the image and close the window."

    print("WARNING! READ ME!")
    print("This test uses Bubble Cam Module's bubblecam.py implementation.")

    args = parse_args()
    print("Starting Test...")
	
    bubblecam = BubbleCam(Logger(True, False), Logger (True, True))

    # prework for testing 
    try:
         # create new images directory each time test starts up
        if os.path.exists(IMG_DIR):
            shutil.rmtree(IMG_DIR)
        os.mkdir(IMG_DIR)

        # name of image to save
        filename = os.path.join(IMG_DIR, f"test_photo.png")

        # capture an image
        success, frame = bubblecam.capture_image()

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
        # Power off camera (release camera)
        bubblecam.power_off()
        print("Completed Test...")