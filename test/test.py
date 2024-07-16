import os
import functools
import unittest
import numpy as np
from src.model.compressor import Compressor
from src.model.channel import Channel


class Test(unittest.TestCase):
    """
    The class used to test the application.

    Attributes:
        _matrix (np.ndarray): The matrix used during some test cases.
        _values: (List[int]): The values to test the image decomposiotion.
        _max_values (int): The number of singular values of the test images.

    Methods:
        setUp() -> None:
            Creates the _matrix attributes.
        compare_matrices(matrix: np.ndarray, threshold: float) -> None:
            Compares two matrices with a threshold value.
        test_channel_from_matrix() -> None:
            Tests a channel creation from a np.ndarray.
        test_channel_out_of_bound_value() -> None:
            Tests the exception throwing for an out of bound singular value.
        test_compressor_from_svd() -> None:
            Tests a channel creation from a {u, s, vt} dictionany.
        test_compressor_negative_value() -> None:
            Tests the exception throwing for a negative singular value.
        test_compressor_grayscale() -> None:
            Tests the compression of a grayscale image.
        test_compressor_rgb() -> None.
            Tests the compression of a RGB image.
        test_npz_grayscale() -> None:
            Tests the saving and loading of an .npz file of a grayscale image.
        test_npz_rgb() -> None:
            Tests the saving and loading of an .npz file of a RGB image.
    """

    def setUp(self) -> None:
        """
        Creates the _matrix attributes.
        """
        self._matrix: np.ndarray = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
        self._values: List[int] = [500, 250, 100, 75, 50, 10]
        self._max_values: int = 1334

    def compare_matrices(self, matrix: np.ndarray, threshold: float) -> None:
        """
        Compares two matrices with a threshold value.

        Args:
            matrix (np.ndarray): The matrix to compare.
            threshold (float): The threshold to use during the composition.
        """
        for i in range(self._matrix.shape[0]):
            for j in range(self._matrix.shape[1]):
                self.assertLessEqual(abs(self._matrix[i, j] - matrix[i, j]), threshold,
                                     f"Elements {self._matrix[i, j]} and {matrix[i, j]} are not equal")

    def test_channel_from_matrix(self) -> None:
        """
        Tests a channel creation from a np.ndarray.
        """
        channel: Channel = Channel(self._matrix)
        self.assertIsNotNone(channel, "channel is None")
        self.assertIsInstance(channel, Channel, "channel is not a Channel")
        result: np.ndarray = channel.compose(1)
        self.assertEqual(result.shape, self._matrix.shape, "The matrices don't have the same dimensions")
        self.compare_matrices(result, 10 ** -15)

    def test_channel_out_of_bound_value(self) -> None:
        """
        Tests the exception throwing for a out of bound singular value.
        """
        channel: Channel = Channel(self._matrix)
        self.assertRaises(ValueError, functools.partial(channel.compose, 3))

    def test_compressor_from_svd(self) -> None:
        """
        Tests a channel creation from a {u, s, vt} dictionany.
        """
        matrices: np.ndarray = np.array({"_u": np.array([[-0.7071067811865477, -0.7071067811865475], [-0.7071067811865475, 0.7071067811865476]]),
                                         "_s": np.array([7.745966692414833e+00, 9.420554752102651e-16]),
                                         "_vt": np.array([[-0.1825741858350552, -0.3651483716701107, -0.5477225575051661, -0.7302967433402214],
                                                          [-0.9737289911202952, 0.0326709649048479, 0.2156731140239386, 0.0653419298096959]])})
        channel: Channel = Channel(matrices)
        self.assertIsNotNone(channel, "channel is None")
        self.assertIsInstance(channel, Channel, "channel is not a Channel")
        result: np.ndarray = channel.compose(1)
        self.assertEqual(result.shape, self._matrix.shape, "The matrices don't have the same dimensions")
        self.compare_matrices(result, 10 ** -14.5)

    def test_compressor_negative_value(self) -> None:
        """
        Tests the exception throwing for a negative singular value.
        """
        compressor: Compressor = Compressor()
        compressor.load("test.jpg")
        self.assertRaises(ValueError, functools.partial(compressor.compose, -1))

    def test_compressor_grayscale(self) -> None:
        """
        Tests the compression of a grayscale image.
        """
        values: List[int] = [500, 250, 100, 75, 50, 10]
        compressor: Compressor = Compressor()
        self.assertIsNotNone(compressor, "compressor is None")
        self.assertIsInstance(compressor, Compressor, "compressor is not a Compressor")
        compressor.load("test_bw.jpg")
        previous_ratio: float = 0
        for i in self._values:
            with self.subTest(compression_value=i):
                compressor.compose(i)
                compressor.save("result_bw.jpg")
                ratio: float = Compressor.get_compression_rate("test_bw.jpg", "result_bw.jpg")
                self.assertGreater(ratio, previous_ratio,
                                       f"The image compression ratio for {i} is not greater than for the previous value")
                previous_ratio = ratio
        if os.path.exists("result_bw.jpg"):
            os.remove("result_bw.jpg")

    def test_compressor_rgb(self) -> None:
        """
        Tests the compression of a RGB image.
        """
        compressor: Compressor = Compressor()
        self.assertIsNotNone(compressor, "compressor is None")
        self.assertIsInstance(compressor, Compressor, "compressor is not a Compressor")
        compressor.load("test.jpg")
        previous_ratio: float = 0
        for i in self._values:
            with self.subTest(compression_value=i):
                compressor.compose(i)
                compressor.save("result.jpg")
                ratio: float = Compressor.get_compression_rate("test.jpg", "result.jpg")
                self.assertGreater(ratio, previous_ratio,
                                   f"The image compression ratio for {i} is not greater than for the previous value")
                previous_ratio = ratio
        if os.path.exists("result.jpg"):
            os.remove("result.jpg")

    def test_npz_grayscale(self) -> None:
        """
        Tests the saving and loading of an .npz file of a grayscale image.
        """
        compressor: Compressor = Compressor()
        compressor.load("test_bw.jpg")
        compressor.compose(self._max_values)
        image: Image.Image = compressor.image
        compressor.save("result_bw.npz")
        compressor = Compressor()
        compressor.load("result_bw.npz")
        compressor.compose(self._max_values)
        self.assertTrue((image == compressor.image).all())
        if os.path.exists("result_bw.npz"):
            os.remove("result_bw.npz")

    def test_npz_rgb(self) -> None:
        """
        Tests the saving and loading of an .npz file of a RGB image.
        """
        compressor: Compressor = Compressor()
        compressor.load("test.jpg")
        compressor.compose(self._max_values)
        image: Image.Image = compressor.image
        compressor.save("result.npz")
        compressor = Compressor()
        compressor.load("result.npz")
        compressor.compose(self._max_values)
        self.assertTrue((image == compressor.image).all())
        if os.path.exists("result.npz"):
            os.remove("result.npz")

if __name__ == "__main__":
    unittest.main()
