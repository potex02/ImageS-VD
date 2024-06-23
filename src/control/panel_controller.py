import functools
import logging
from typing import List
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QAction
from src.model.compressor import Compressor
from src.view.panel import Panel
from src.control.compose_thread import ComposeThread


class PanelController:
    """
    The class used as controller for an app panel.

    Attributes:
        _panel (Panel): The panel controlled by the controller.
        _compressor (Compressor): The compressor used to compress the panel image.
        _values (int): number of image singular values.
        _save_action (QAction): The action used to save the images.
        _last_value (int): The last valid value for the singular values.
        _threads (List[ComposeThread]): The list of ComposeThraed associated at the controller.

    Methods:
        load_image(self, path: str) -> None:
            Loads and decomposes the image.
        change_value() -> None:
            Changes the number of the singular values through a QSlider.
        Changes the value of singular values through a QLineEdit.
            change_line(line: QLineEdit, slider: QSlider) -> None:
        save(path: str) -> None:
            Saves the image.
        _set_image(thread: ComposeThread) -> None:
            Sets the panel image ath the end of the _current_thread.
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
        self._threads: List[ComposeThread] = []

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

    def change_value(self) -> None:
        """
        Changes the number of the singular values through a QSlider.
        """
        k: int = self._panel.slider.value()
        thread: ComposeThread = ComposeThread(self._compressor, self._values - k - 1)
        self._threads.append(thread)
        thread.finished.connect(functools.partial(self._set_image, thread))
        thread.start()
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
            if value >= self._values:
                value = self._values - 1
                self._panel.slider_line.setText(str(value))
            elif value < 0:
                value = 0
                self._panel.slider_line.setText(str(value))
            self._panel.slider.setValue(value)
            self._panel.slider.sliderReleased.emit()
            self._last_value = value
        except ValueError:
            logging.error(QCoreApplication.translate("Gui", "parse").format(value=self._panel.slider_line.text()))
            self._panel.slider_line.setText(str(self._last_value))

    def save(self, path: str) -> None:
        """
        Saves the image

        Args:
            path (str): The path where to save the image.
        """
        self._compressor.save(path)

    def _set_image(self, thread: ComposeThread) -> None:
        """
        Sets the panel image ath the end of the _current_thread

        Args:
            thread (ComposeThread): the thread that emitted the signal.
        """
        if self._threads and thread == self._threads[-1]:
            self._panel.set_image(self._compressor.image.squeeze())
        if thread in self._threads:
            self._threads.remove(thread)