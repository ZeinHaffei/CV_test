from src.config import AppConfig
from src.app import AppController


def main():
    config = AppConfig(
        video_source=0,
        frame_width=1280,
        frame_height=720,
        grayscale=True,
        gaussian_blur=True,
        blur_kernel=5,
        show_fps=True,
        show_shape=True
    )
    app = AppController(config)
    app.run()


if __name__ == '__main__':
    main()