from PySide6.QtCore import QThread
from ..model.compressor import Compressor


class ComposeThread(QThread):
    """
        The class used to compose the panel image.

        Attributes:
            _compressor (Compressor): The compressor used to compress the panel image.
            _values (int): number of image singular values.

        Methods:
            run() -> None:
                Composes the image.
        """

    def __init__(self, compressor: Compressor, values: int) -> None:
        """
            Creates a ComposeThread

            Args:
                compressor (Compressor): The compressor used to compress the panel image.
                values (int): number of image singular values.:
            """
        super().__init__()
        self._compressor: Compressor = compressor
        self._values: int = values

    def run(self) -> None:
        """
        Composes the image.
        """
        self._compressor.compose(self._values)
        self.finished.emit()
