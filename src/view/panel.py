import numpy as np
from PIL import Image
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
        set_image(self, image: Image.Image) -> None:
            Sets the images to show.
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
        self._slider.setMinimum(0)
        self._slider.setMaximum(100)
        self._slider.setEnabled(False)
        self._slider.valueChanged.connect(lambda: print(self._slider.value()))
        pixmap: QPixmap = QPixmap("./assets/loading.png")
        layout: QVBoxLayout = QVBoxLayout()
        layout.setAlignment(Qt.AlignHCenter)
        pixmap = pixmap.scaled(400, 400, Qt.KeepAspectRatioByExpanding)
        self._image.setPixmap(pixmap)
        layout.addWidget(self._slider)
        layout.addWidget(self._image)
        self.setLayout(layout)
        self._panel_controller.load_image(path)

    def set_image(self, image: Image.Image) -> None:
        """
        Sets the images to show.

        Args:
            image (np.ndarray): The data of the image to show.
        """
        width, height = image.size
        qimage: QImage = QImage(image.tobytes(), width, height,
                        QImage.Format_RGBA8888 if image.mode == "RGBA" else QImage.Format_RGB888)
        pixmap: QPixmap = QPixmap.fromImage(qimage)
        pixmap = pixmap.scaled(400, 400, Qt.KeepAspectRatioByExpanding)
        self._image.setPixmap(pixmap)