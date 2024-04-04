import threading
from ..model.compressor import Compressor
from ..view.panel import Panel


class PanelController:
    """
    The class used as controller for an app panel.

    Attributes:
        _panel (Panel): The panel controlled by the controller.
        _compressor (Compressor): The compressor used to compress the panel image.

    Methods:
        oad_image(self, path: str) -> None:
            Loads and decomposes the image.
    """

    def __init__(self, panel: Panel) -> None:
        """
        Creates a new PanelController.

        Args:
            panel (Panel): The panel controlled by the controller.
        """
        self._panel: Panel = panel
        self._compressor: Compressor = Compressor()

    def load_image(self, path: str) -> None:
        """
        Loads and decomposes the image.

        Args:
            path: he path to the file of the panel.
        """
        threading.Thread(target=lambda: print("Thread")).start()
