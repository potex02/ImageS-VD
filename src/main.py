import numpy as np
from PIL import Image


def compress_image(image_path: str, k: int) -> Image.Image:
    image: Image.Image = Image.open(image_path)
    image_gray: Image.Image = image.convert('L')
    image_array: np.ndarray = np.array(image_gray)
    U: np.ndarray
    s: np.ndarray
    V: np.ndarray
    U, s, V = np.linalg.svd(image_array, full_matrices=False)
    print(U.shape, s.shape, V.shape)
    print(U[0, 0], s[0], V[0, 0])
    s[k:] = 0
    compressed_image_array: np.ndarray = np.dot(U, np.dot(np.diag(s), V))
    compressed_image_array = np.clip(compressed_image_array, 0, 255).astype(np.uint8)
    compressed_image: Image.Image = Image.fromarray(compressed_image_array)
    return compressed_image


original_image_path: str = '../images/image.jpeg'
compressed_image_path: str = '../images/compressed_image.jpeg'
k: int = 500

compressed_image: Image.Image = compress_image(original_image_path, k)
compressed_image.save(compressed_image_path)
