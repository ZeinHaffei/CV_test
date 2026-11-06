import cv2
import numpy as np
import time

from src.config import AppConfig

from src.processing.image_processor import ImageProcessing
from src.display.video_display import VideoDisplay
from src.capture.video_source import VideoSource


class AppController:
    def __init__(self, config: AppConfig):
        self.config = config

        self.source = VideoSource(
            source=config.video_source,
            width=config.frame_width,
            height=config.frame_height
        )

        self.processor = ImageProcessing(
            grayscale=config.grayscale
        )

        self.display = VideoDisplay(
            config.window_name
        )

    def run(self):
        previous_time = time.perf_counter()

        try:
            self.source.open()

            while True:
                frame = self.source.read()

                if frame is None:
                    break

                processed = self.processor.process(frame)

                current_time = time.perf_counter()
                elapsed_time = current_time - previous_time

                previous_time = current_time

                fps = 1.0 / elapsed_time if elapsed_time > 0 else 0.0

                if self.config.show_fps:
                    if self.config.show_fps:
                        cv2.putText(
                            processed,
                            f"Loop FPS: {fps:.1f}",
                            (20, 40),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0, 255, 0),
                            2
                        )
                if self.config.show_shape:
                    height, width = processed.shape[:2]

                    cv2.putText(
                        processed,
                        f"Shape: {width} * {height}",
                        (220, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2
                    )

                self.display.show(processed)

                if self.display.wait_key() == ord('q'):
                    break

        finally:
            self.source.release()
            self.display.close()





