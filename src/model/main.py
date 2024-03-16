import os
import numpy as np
from PIL import Image


class Compressor:
    def __init__(self):
        self.__path: str = ""
        self.__channels: list[dict] = list[dict]()

    @staticmethod
    def get_compression_rate(original_file: str, compressed_file: str) -> float:
        original_size: int = os.path.getsize(original_file)
        compressed_size: int = os.path.getsize(compressed_file)
        compression_rate: float = 1 - (compressed_size / original_size)
        return compression_rate

    def load(self, path: str) -> None:
        self.__path = path
        image = Image.open(self.__path)
        image_array: np.ndarray = np.array(image)
        index: int = path.rfind('.')
        if index != -1 and path[index + 1:].lower() == "pbm":
            image_array = np.where(image_array, 0, 255)
        channels: int = 1
        if len(image_array.shape) == 3:
            _, _, channels = image_array.shape
        for i in range(channels):
            channel: np.ndarray
            if channels == 1:
                channel = image_array
            else:
                channel = image_array[:, :, i]
            u: np.ndarray
            s: np.ndarray
            vt: np.ndarray
            u, s, vt = np.linalg.svd(channel, full_matrices=False)
            self.__channels.append({"u": u, "s": s, "vt": vt})

    def save(self, path: str, k: int):
        compressed_channels: list[np.ndarray] = list[np.ndarray]()
        for i in self.__channels:
            i["s"][k:] = 0
            compressed_channels.append(np.dot(i["u"], np.dot(np.diag(i["s"]), i["vt"])))
        compressed_image_array: np.ndarray = np.stack(compressed_channels, axis=-1)
        compressed_image_array = np.clip(compressed_image_array, 0, 255).astype(np.uint8)
        result: Image.Image = Image.fromarray(compressed_image_array.squeeze())
        result.save(path)
        print(Compressor.get_compression_rate(self.__path, path))