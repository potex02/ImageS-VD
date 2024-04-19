from ..model.compressor import Compressor
from ..view.panel import Panel


class PanelController:
    """
    The class used as controller for an app panel.

    Attributes:
        _panel (Panel): The panel controlled by the controller.
        _compressor (Compressor): The compressor used to compress the panel image.
        _values (int): number of image singular values.

    Methods:
        load_image(self, path: str) -> None:
            Loads and decomposes the image.
        change_value(k: int) -> None:
            Changes the number of the singular values.
        save(path: str) -> None:
            Saves the image.
    """

    def __init__(self, panel: Panel) -> None:
        """
        Creates a new PanelController.

        Args:
            panel (Panel): The panel controlled by the controller.
        """
        self._panel: Panel = panel
        self._compressor: Compressor = Compressor()
        self._values: int = 0

    def load_image(self, path: str) -> None:
        """
        Loads and decomposes the image.

        Args:
            path (str): he path to the file of the panel.
        """
        self._values = self._compressor.load(path)
        self._compressor.compose(0)
        self._panel.set_image(self._compressor.image.squeeze(), self._values)

    def change_value(self, k: int) -> None:
        """
        Changes the number of the singular values.

        Args:
            k (int): The value of the slider. The number of singular values is calculated as values - k.
        """
        self._compressor.compose(self._values - k)
        self._panel.set_image(self._compressor.image.squeeze(), self._values)

    def save(self, path: str) -> None:
        """
        Saves the image

        Args:
            path (str): The path where to save the image.
        """
        self._compressor.save(path)
