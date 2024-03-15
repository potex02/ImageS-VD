import numpy as np
from PIL import Image


def compress_image(image_path, k):
    image = Image.open(image_path)
    image_gray = image.convert('L')
    image_array = np.array(image_gray)
    U, s, V = np.linalg.svd(image_array, full_matrices=False)
    s[k:] = 0
    compressed_image_array = np.dot(U, np.dot(np.diag(s), V))
    compressed_image_array = np.clip(compressed_image_array, 0, 255).astype(np.uint8)
    compressed_image = Image.fromarray(compressed_image_array)

    return compressed_image


original_image_path = 'images/image.jpeg'
compressed_image_path = 'images/compressed_image.jpeg'
k = 500

compressed_image = compress_image(original_image_path, k)
compressed_image.save(compressed_image_path)
