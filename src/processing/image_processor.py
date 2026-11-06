import cv2
import numpy as np


class ImageProcessing:

    def __init__(self, grayscale: bool = False, gaussian_blur: bool = False, blur_kernel: int = 5):

        if blur_kernel <= 0 or blur_kernel % 2 == 0:
            raise ValueError("Blur kernel must be a positive odd number")

        self.grayscale = grayscale
        self.gaussian_blur = gaussian_blur
        self.blur_kernel = blur_kernel


    def process(self, frame: np.ndarray) -> np.ndarray:

        result = frame.copy()

        if self.gaussian_blur:
            result = cv2.GaussianBlur(result, (self.blur_kernel, self.blur_kernel), sigmaX=0)

        if self.grayscale:
            gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
            return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

        return result