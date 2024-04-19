import functools
import threading
import numpy as np
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSlider


class Panel(QWidget):
    """
    The panel page of the window's tab widget.

    Attributes:
        _image (QLAbel): The label that contains the graphic representation of the image to compress.
        _slider (QSlider): The slider used to select the number of singular values.
        _panel_controller (PanelController): The controller of the panel.

    Methods:
        set_image(image: Image.Image, k: int) -> None:
            Sets the images to show.
        save(path: str) -> None:
            Saves the image.
        def _add_components() -> None:
            Adds and initializes the gui components of the panel.
    """

    def __init__(self, path: str) -> None:
        """
        Creates a Panel.

        Args:
            path (str): The path to the file of the panel.
        """
        super().__init__()
        from ..control.panel_controller import PanelController
        self._image: QLabel = QLabel()
        self._slider: QSlider = QSlider(Qt.Horizontal)
        self._panel_controller: PanelController = PanelController(self)
        self._add_components()
        threading.Thread(
           target=functools.partial(self._panel_controller.load_image, path)
        ).start()

    def set_image(self, image: np.ndarray, k: int = -1) -> None:
        """
        Sets the images to show.

        Args:
            image (np.ndarray): The data of the image to show.
            k (int): The number of singular values of the image.
        """
        height, width = image.shape[:2]
        qimage: QImage
        if len(image.shape) == 2:
            qimage = QImage(image.data, width, height, width, QImage.Format_Grayscale8)
        elif len(image.shape) == 3:
            if image.shape[2] == 3:
                qimage = QImage(image.data, width, height, 3 * width, QImage.Format_RGB888)
            elif image.shape[2] == 4:
                qimage = QImage(image.data, width, height, 4 * width, QImage.Format_RGBA8888)
            else:
                raise ValueError("Unsupported number of channels for image")
        pixmap: QPixmap = QPixmap.fromImage(qimage)
        pixmap = pixmap.scaled(400, 400, Qt.KeepAspectRatioByExpanding)
        self._image.setPixmap(pixmap)
        if k != -1:
            self._slider.setMinimum(1)
            self._slider.setMaximum(k - 1)
            self._slider.setEnabled(True)

    def save(self, path: str) -> None:
        """
        Saves the image

        Args:
            path (str): The path where to save the image.
        """
        self._panel_controller.save(path)

    def _add_components(self) -> None:
        """
        Adds and initializes the gui components of the panel.
        """
        self._slider.setMinimum(0)
        self._slider.setMaximum(100)
        self._slider.setEnabled(False)
        self._slider.valueChanged.connect(self._panel_controller.change_value)
        pixmap: QPixmap = QPixmap("./assets/loading.png")
        layout: QVBoxLayout = QVBoxLayout()
        layout.setAlignment(Qt.AlignHCenter)
        pixmap = pixmap.scaled(400, 400, Qt.KeepAspectRatioByExpanding)
        self._image.setPixmap(pixmap)
        layout.addWidget(self._slider)
        layout.addWidget(self._image)
        self.setLayout(layout)