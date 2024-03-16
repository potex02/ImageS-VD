import sys
import numpy as np
from PIL import Image


def compress_image(image_path: str, k: int) -> Image.Image:
    image: Image.Image = Image.open(image_path)
    image_array: np.ndarray = np.array(image)
    channels: int = 1
    compressed_channels: list[np.ndarray] = list()
    if len(image_array.shape) == 3:
        _, _, channels = image_array.shape
    for i in range(channels):
        if channels == 1:
            channel: np.ndarray = image_array
        else:
            channel: np.ndarray = image_array[:, :, i]
        u: np.ndarray
        s: np.ndarray
        vt: np.ndarray
        u, s, vt = np.linalg.svd(channel, full_matrices=False)
        print(u.shape, s.shape, vt.shape)
        print(s[k])
        s[k:] = 0
        compressed_channels.append(np.dot(u, np.dot(np.diag(s), vt)))
    compressed_image_array: np.ndarray = np.stack(compressed_channels, axis=-1)
    compressed_image_array = np.clip(compressed_image_array, 0, 255).astype(np.uint8)
    print("Shape:\t",compressed_image_array.shape)
    result: Image.Image = Image.fromarray(compressed_image_array.squeeze())
    return result


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Bad arguments", file=sys.stderr)
        sys.exit(1)
    original_image_path: str = sys.argv[1]
    compressed_image_path: str = sys.argv[2]
    k: int = int(sys.argv[3])
    compressed_image: Image.Image = compress_image(original_image_path, k)
    compressed_image.save(compressed_image_path)
