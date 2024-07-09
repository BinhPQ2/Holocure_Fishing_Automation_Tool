import mss.tools
import cv2 as cv
import numpy as np
import pydirectinput as di
import keyboard
import os 


class FishingBot:
    def __init__(self):
        self.running = False
        self.threshold = 0.8
        self.setup_hotkeys()
        self.assets_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')

    def toggle_running(self):
        self.running = not self.running
        if self.running:
            print("Script is running")
        else:
            print("Script is not running")

    def setup_hotkeys(self):
        keyboard.add_hotkey('o', self.toggle_running)

    def run(self):
        INDICATOR = cv.imread(os.path.join(self.assets_path, 'indicator.png'), cv.IMREAD_GRAYSCALE)
        UP = cv.imread(os.path.join(self.assets_path, 'up.png'), cv.IMREAD_GRAYSCALE)
        DOWN = cv.imread(os.path.join(self.assets_path, 'down.png'), cv.IMREAD_GRAYSCALE)
        LEFT = cv.imread(os.path.join(self.assets_path, 'left.png'), cv.IMREAD_GRAYSCALE)
        RIGHT = cv.imread(os.path.join(self.assets_path, 'right.png'), cv.IMREAD_GRAYSCALE)
        CIRCLE = cv.imread(os.path.join(self.assets_path, 'circle.png'), cv.IMREAD_GRAYSCALE)

        while True:
            if self.running:
                with mss.mss() as sct:
                    targetDim = {"top": 680, "left": 1131, "width": 96, "height": 124}
                    target = np.array(sct.grab(targetDim))

                target = cv.cvtColor(target, cv.COLOR_BGRA2GRAY)
                resIndicator = cv.matchTemplate(target, INDICATOR, cv.TM_CCOEFF_NORMED)

                if cv.minMaxLoc(resIndicator)[1] > self.threshold:
                    isFishing = True
                else:
                    isFishing = False
                    di.press("space")

                if isFishing:
                    resUp = cv.matchTemplate(target, UP, cv.TM_CCOEFF_NORMED)
                    resDown = cv.matchTemplate(target, DOWN, cv.TM_CCOEFF_NORMED)
                    resLeft = cv.matchTemplate(target, LEFT, cv.TM_CCOEFF_NORMED)
                    resRight = cv.matchTemplate(target, RIGHT, cv.TM_CCOEFF_NORMED)
                    resCircle = cv.matchTemplate(target, CIRCLE, cv.TM_CCOEFF_NORMED)

                    if cv.minMaxLoc(resUp)[1] > self.threshold:
                        di.press("w")
                    if cv.minMaxLoc(resDown)[1] > self.threshold:
                        di.press("s")
                    if cv.minMaxLoc(resLeft)[1] > self.threshold:
                        di.press("a")
                    if cv.minMaxLoc(resRight)[1] > self.threshold:
                        di.press("d")
                    if cv.minMaxLoc(resCircle)[1] > self.threshold:
                        di.press("space")


if __name__ == "__main__":
    bot = FishingBot()
    bot.run()
