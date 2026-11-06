from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    # video_source: int = 0
    video_source: str or int = 0
    frame_width: int = 640
    frame_height: int = 480
    window_name: str = "Vision Toolkit"
    grayscale: bool = False
    gaussian_blur: bool = False
    blur_kernel: int = 5
    show_fps: bool = False
    show_shape: bool = False
