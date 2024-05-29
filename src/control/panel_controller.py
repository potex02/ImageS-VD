import logging

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QLineEdit, QSlider
from ..model.compressor import Compressor
from ..view.panel import Panel


class PanelController:
    """
    The class used as controller for an app panel.

    Attributes:
        _panel (Panel): The panel controlled by the controller.
        _compressor (Compressor): The compressor used to compress the panel image.
        _values (int): number of image singular values.
        _save_action (QAction): The action used to save the images.

    Methods:
        load_image(self, path: str) -> None:
            Loads and decomposes the image.
        change_value(k: int) -> None:
            Changes the number of the singular values through a QSlider.
        Changes the value of singular values through a QLineEdit.
            change_line(line: QLineEdit, slider: QSlider) -> None:
        save(path: str) -> None:
            Saves the image.
    """

    def __init__(self, panel: Panel, save_action: QAction) -> None:
        """
        Creates a new PanelController.

        Args:
            panel (Panel): The panel controlled by the controller.
            save_action (Action): The action used to save the images.
        """
        self._panel: Panel = panel
        self._compressor: Compressor = Compressor()
        self._values: int = 0
        self._save_action: QAction = save_action

    def load_image(self, path: str) -> None:
        """
        Loads and decomposes the image.

        Args:
            path (str): he path to the file of the panel.
        """
        self._values = self._compressor.load(path)
        self._compressor.compose(self._values - 1)
        self._panel.set_image(self._compressor.image.squeeze(), self._values)
        self._save_action.setEnabled(True)

    def change_value(self, k: int) -> None:
        """
        Changes the number of the singular values through a QSlider.

        Args:
            k (int): The value of the slider. The number of singular values is calculated as values - k.
        """
        self._compressor.compose(self._values - k - 1)
        self._panel.set_image(self._compressor.image.squeeze())
        self._panel.set_slider_value(k)

    def change_line(self, line: QLineEdit, slider: QSlider) -> None:
        """
        Changes the value of singular values through a QLineEdit.

        Params:
            line (QLineEdit): The source of the event.
            slider (QSlider): The slider of the Panel.
        """
        try:
            slider.setValue(int(line.text()))
        except:
            logging.error(f"Cannot parse {line.text()} to int")

    def save(self, path: str) -> None:
        """
        Saves the image

        Args:
            path (str): The path where to save the image.
        """
        self._compressor.save(path)