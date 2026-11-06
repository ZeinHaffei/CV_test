import cv2


class VideoSource:

    def __init__(
            self,
            source: str or int,
            width: int,
            height: int
    ):
        self.source = source
        self.width = width
        self.height = height
        self.cap = None

    def open(self):
        self.cap = cv2.VideoCapture(self.source)

        if not self.cap.isOpened():
            raise RuntimeError(f"Cannot open video from source: {self.source}")

        if isinstance(self.source, int):
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)

    def read(self):
        if self.cap is None:
            raise RuntimeError(" Video source is not open")
        success, frame = self.cap.read()

        return frame if success else None

    def release(self):
        if self.cap is not None:
            self.cap.release()
            cv2.destroyAllWindows()
