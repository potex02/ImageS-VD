import logging
from PySide6.QtGui import QAction
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
        _last_value (int): The last valid value for the singular values.

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
        self._last_value: int = 0

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
        self._panel.slider_line.setText(str(k))
        self._last_value = k

    def change_line(self) -> None:
        """
        Changes the value of singular values through a QLineEdit.

        Params:
            line (QLineEdit): The source of the event.
            slider (QSlider): The slider of the Panel.
        """
        try:
            value: int = int(self._panel.slider_line.text())
            print(self._values)
            if value >= self._values:
                value = self._values - 1
                self._panel.slider_line.setText(str(value))
            self._panel.slider.setValue(value)
            self._last_value = value
        except ValueError:
            logging.error(f"Cannot parse {self._panel.slider_line.text()} to int")
            self._panel.slider_line.setText(str(self._last_value))

    def save(self, path: str) -> None:
        """
        Saves the image

        Args:
            path (str): The path where to save the image.
        """
        self._compressor.save(path)