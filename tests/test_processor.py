import numpy as np

from src.processing.image_processor import ImageProcessing

def test_processor_preserve_shape():
    image = np.zeros((480, 640, 3), dtype=np.uint8)

    processor = ImageProcessing(grayscale=True)

    result = processor.process(image)

    assert result.shape == image.shape

def test_processor_returns_copy():
    image = np.zeros((480, 640, 3), dtype=np.uint8)

    processor = ImageProcessing(grayscale=False)

    result = processor.process(image)

    assert result is not image
    assert np.array_equal(result, image)

