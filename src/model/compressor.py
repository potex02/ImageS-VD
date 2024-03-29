import os
from typing import List, Dict
import numpy as np
from PIL import Image
from .channel import Channel


class Compressor:
    """
    A class used to compress images using svd decomposition.

    Attributes:
        _path (str): The path to the image to compress.
        _channels (List[Channel]): The channels of the decomposed image.

    Methods:
        get_compression_rate(original_file: str, compressed_file: str) -> float:
            Calculates the compression rate of a result image.
        load_channels(path: str):
            Loads the decomposed image channels from a .npz file.
        load(path: str) -> None:
            Loads an image to compress.
        save_channels(path: str):
            Saves the decomposed channels on a .npz file.
        save(path: str, k: int) :
            Compresses and saves the image to the specified path using 'k' singular values.
    """

    def __init__(self) -> None:
        """
        Creates a Compressor instances.
        """
        self._path: str = ""
        self._channels: List[Channel] = []

    @property
    def path(self) -> str:
        """
        Gets the path of the image to compress.

        Returns:
            str: The path to the image.
        """
        return self._path

    @property
    def channels(self) -> List[Channel]:
        """
        Gets the image decomposed channels

        Returns:
            List[Channel]: The image decomposed channels.
        """
        return self._channels

    @staticmethod
    def get_compression_rate(original_file: str, compressed_file: str) -> float:
        """
        Calculates the compression rate of a result image.

        Args:
            original_file (str): The path to the original uncompressed file.
            compressed_file (str): The path to the compressed file.

        Returns:
            float: The compression rate.
        """
        original_size: int = os.path.getsize(original_file)
        compressed_size: int = os.path.getsize(compressed_file)
        compression_rate: float = 1 - (compressed_size / original_size)
        return compression_rate

    def load_channels(self, path: str) -> None:
        """
        Loads the decomposed image channels from a .npz file.

        Args:
            path (str): path to the file where channels are stored.
        """
        channels = np.load(path, allow_pickle=True)
        for i in sorted(channels.keys()):
            self._channels.append(Channel(channels[i]))

    def load(self, path: str) -> None:
        """
        Loads an image to compress.

        Args:
            path (str): path to the image.
        """
        self._path = path
        if os.path.splitext(self._path)[1] == ".npz":
            self.load_channels(self._path)
            return
        image = Image.open(self._path)
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
            self._channels.append(Channel(channel))

    def save_channels(self, path: str) -> None:
        """
        Saves the decomposed channels on a .npz file.

        Args:
            path (str): path to file.
        """
        channels: List[Dict] = []
        for i in self._channels:
            channels.append(vars(i))
        np.savez(path, *channels)

    def save(self, path: str, k: int) -> None:
        """
        Loads an image to compress.

        Args:
            path (str): path where to save the image.
            k (int): number of singular values to use for compression.
        """
        if os.path.splitext(path)[1] == ".npz":
            self.save_channels(path)
            return
        if k < 0:
            raise ValueError(f"Unexpected k value: {k}")
        compressed_channels: List[np.ndarray] = []
        for i in self._channels:
            compressed_channels.append(i.compose(k))
        compressed_image_array: np.ndarray = np.stack(compressed_channels, axis=-1)
        compressed_image_array = np.clip(compressed_image_array, 0, 255).astype(np.uint8)
        result: Image.Image = Image.fromarray(compressed_image_array.squeeze())
        result.save(path)
        print(Compressor.get_compression_rate(self._path, path))
