from PySide6.QtCore import QThread, Signal
from src.model.compressor import Compressor


class DecomposeThread(QThread):
    """
    The class used to decompose the panel image.

    Attributes:
        _compressor (Compressor): The compressor used to decompose the panel image.
        _path (str): The path to the file.
        decomposed (Signal): The signal used to return the number of singular values.

    Methods:
        run() -> None:
            Decomposes the image.
    """

    decomposed: Signal = Signal(int)

    def __init__(self, compressor: Compressor, path: str) -> None:
        """
        Creates a DecomposeThread.

        Args:
            compressor (Compressor): The compressor used to decompose the panel image.
            path (str): The path to the file.
        """
        super().__init__()
        self._compressor: Compressor = compressor
        self._path: str = path


    def run(self) -> None:
        """
        Composes the image.
        """
        values: int = self._compressor.load(self._path)
        self._compressor.compose(values - 1)
        self.decomposed.emit(values)
