import cv2
import numpy as np


class VideoDisplay:
    def __init__(self, window_name: str):
        self.window_name = window_name

    def show(self, frame: np.ndarray):
        cv2.imshow(self.window_name, frame)

    def wait_key(self, delay: int = 1) -> int:
        cv2.waitKey(delay) & 0xFF

    def close(self):
        cv2.destroyAllWindows()