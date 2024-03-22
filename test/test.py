import unittest
import numpy as np
from src.model.compressor import Compressor
from src.model.channel import Channel


class Test(unittest.TestCase):

    def setUp(self):
        self._matrix: np.ndarray = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
        self._threshold: float = 10 ** -7

    def compare_matrices(self, matrix: np.ndarray):
        for i in range(self._matrix.shape[0]):
            for j in range(self._matrix.shape[1]):
                self.assertLessEqual(abs(self._matrix[i, j] - matrix[i, j]), self._threshold,
                                     f"Elements {self._matrix[i, j]} and {matrix[i, j]} are not equal")

    def test_channel_from_matrix(self):
        channel: Channel = Channel(self._matrix)
        self.assertIsNotNone(channel, "channel is None")
        self.assertIsInstance(channel, Channel, "channel is not a Channel")
        result: np.ndarray = channel.compose(1)
        self.assertEqual(result.shape, self._matrix.shape, "The matrices don't have the same dimensions")
        self.compare_matrices(result)

    def test_channel_from_svd(self):
        matrices: np.ndarray = np.array({"_u": np.array([[-0.70710678, -0.70710678], [-0.70710678, 0.70710678]]),
                                         "_s": np.array([7.74596669e+00, 9.42055475e-16]),
                                         "_vt": np.array([[-0.18257419, -0.36514837, -0.54772256, -0.73029674],
                                                          [-0.97372899, 0.03267096, 0.21567311, 0.06534193]])})
        channel: Channel = Channel(matrices)
        self.assertIsNotNone(channel, "channel is None")
        self.assertIsInstance(channel, Channel, "channel is not a Channel")
        result: np.ndarray = channel.compose(1)
        self.assertEqual(result.shape, self._matrix.shape, "The matrices don't have the same dimensions")
        self.compare_matrices(result)

    def test_compressor_bw(self):
        compressor: Compressor = Compressor()
        self.assertIsNotNone(compressor, "compressor is None")
        self.assertIsInstance(compressor, Compressor, "compressor is not a Compressor")
        compressor.load("test_bw.jpg")
        compressor.save("result_bw.jpg", 100)
        self.assertGreater(Compressor.get_compression_rate("test_bw.jpg", "result_bw.jpg"), 0, "The image is not compressed")

    def test_compressor(self):
        compressor: Compressor = Compressor()
        self.assertIsNotNone(compressor, "compressor is None")
        self.assertIsInstance(compressor, Compressor, "compressor is not a Compressor")
        compressor.load("test.jpg")
        compressor.save("result.jpg", 100)
        self.assertGreater(Compressor.get_compression_rate("test.jpg", "result.jpg"), 0, "The image is not compressed")


if __name__ == "__main__":
    unittest.main()
