import logging
import os
from typing import List, Dict, Optional
import numpy as np
from PIL import Image
from PySide6.QtCore import QCoreApplication
from src.model.channel import Channel


class Compressor:
    """
    A class used to compress images using svd decomposition.

    Attributes:
        _path (str): The path to the image to compress.
        _channels (List[Channel]): The channels of the decomposed image.
        _image (np.ndarray): The image ndarray.

    Methods:
        get_compression_rate(original_file: str, compressed_file: str) -> float:
            Calculates the compression rate of a result image.
        load(path: str) -> int:
            Loads an image to compress.
        compose(k: int) -> None:
            Composes a compressed image.
        save(path: str) -> Optional[float]:
            Saves a compressed image.
        _load_channels(path: str) -> int:
            Loads the decomposed image channels from a .npz file.
        _save_channels(path: str) -> None:
            Saves the decomposed channels on a .npz file.
    """

    def __init__(self) -> None:
        """
        Creates a Compressor instances.
        """
        self._path: str = ""
        self._channels: List[Channel] = []
        self._image: np.ndarray

    @property
    def image(self) -> np.ndarray:
        """
        Gets the image.

        Returns:
            np.ndarray: The ndarray representing the image.
        """
        return self._image

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

    def load(self, path: str) -> int:
        """
        Loads an image to compress.

        Args:
            path (str): path to the image.

        Returns:
            int: The number of the singular values of the image.
        """
        self._path = path
        if os.path.splitext(self._path)[1] == ".npz":
            return self._load_channels(self._path)
        image: Image.Image = Image.open(self._path)
        image_array: np.ndarray = np.array(image)
        index: int = path.rfind('.')
        if index != -1 and path[index + 1:].lower() == "pbm":
            image_array = np.where(image_array, 0, 255)
        channels: int = 1
        k: int = 0
        if len(image_array.shape) == 3:
            _, _, channels = image_array.shape
        for i in range(channels):
            channel_array: np.ndarray
            if channels == 1:
                channel_array = image_array
            else:
                channel_array = image_array[:, :, i]
            channel: Channel = Channel(channel_array)
            values: int = channel.get_singular_values()
            if values > k:
                k = values
            self._channels.append(channel)
        return k

    def compose(self, k: int) -> None:
        """
        Composes a compressed image.

        Args:
            k (int): number of singular values to use for compression."""
        if k < 0:
            error: str
            raise ValueError(QCoreApplication.translate("Cli", "unexpected_value").format(k=k))
        compressed_channels: List[np.ndarray] = []
        for i in self._channels:
            compressed_channels.append(i.compose(k))
        compressed_image_array: np.ndarray = np.stack(compressed_channels, axis=-1)
        self._image = np.clip(compressed_image_array, 0, 255).astype(np.uint8)

    def save(self, path: str) -> Optional[float]:
        """
        Saves a compressed image.

        Args:
            path (str): path where to save the image.

        Returns:
            Optional[float]: The compression ratio if both input and output files are images.
        """
        if os.path.splitext(path)[1] == ".npz":
            self._save_channels(path)
            return None
        result = Image.fromarray(self._image.squeeze())
        try:
            result.save(path)
        except Exception:
            result = result.convert("RGB")
            result.save(path)
        if os.path.splitext(self._path)[1] == ".npz":
            return None
        return Compressor.get_compression_rate(self._path, path)

    def _load_channels(self, path: str) -> int:
        """
        Loads the decomposed image channels from a .npz file.

        Args:
            path (str): path to the file where channels are stored.

        Returns:
            int: The number of the singular values of the image.
        """
        k: int = 0
        channels = np.load(path, allow_pickle=True)
        for i in sorted(channels.keys()):
            channel: Channel = Channel(channels[i])
            self._channels.append(channel)
            if k == 0:
                k = channel.get_singular_values()
        return k

    def _save_channels(self, path: str) -> None:
        """
        Saves the decomposed channels on a .npz file.

        Args:
            path (str): path to file.
        """
        channels: List[Dict] = []
        for i in self._channels:
            channels.append(vars(i))
        np.savez(path, *channels)
