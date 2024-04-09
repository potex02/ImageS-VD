from typing import Dict
import numpy as np


class Channel:
    """
    Representation of an SVD decomposition of a matrix.

    Attributes:
        _u (np.ndarray): The matrix of the left singular vectors.
        _s (np.ndarray: The matrix of the singular values.
        _vt (np.ndarray): The matrix of right singular vectors.

    Methods:
        compose(K: int) -> np.ndarray:
            Compose the matrix from u, s and vt.
    """

    def __init__(self, matrix: np.ndarray) -> None:
        """
        Create a Channel instance.

        Args:
            matrix (np.ndarray): The matrix to decomposed or a np.ndarray containing the u, s and vt values.
        """
        if len(matrix.shape) == 0:
            channel: Dict = matrix.item()
            self._u: np.ndarray = channel["_u"]
            self._s: np.ndarray = channel["_s"]
            self._vt: np.ndarray = channel["_vt"]
            return
        self._u, self._s, self._vt = np.linalg.svd(matrix, full_matrices=False)

    def compose(self, k: int) -> np.ndarray:
        """
        Compose the matrix from u, s and vt.

        Args;
            k (int): The number of singular values to use in the composition.

        Returns:
            np.ndarray The composed matrix.
        """
        if k >= len(self._s):
            error: str = f"Cannot use {k} values for {len(self._s)} vector"
            raise ValueError(error)
        sigma: np.ndarray = self._s.copy()
        if k != 0:
            sigma[k:] = 0
        return np.dot(np.dot(self._u, np.diag(sigma)), self._vt)
