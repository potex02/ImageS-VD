import functools
import threading
import numpy as np
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtGui import QPixmap, QImage, QAction
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSlider, QHBoxLayout, QLineEdit


class Panel(QWidget):
    """
    The panel page of the window's tab widget.

    Attributes:
        _image (QLAbel): The label that contains the graphic representation of the image to compress.
        _slider (QSlider): The slider used to select the number of singular values.
        _slider_line (QLineEdit): The entry to show and change the slider value.
        _loaded (bool): The flag that indicates if the image has been loaded.
        _panel_controller (PanelController): The controller of the panel.

    Methods:
        set_image(image: Image.Image, k: int) -> None:
            Sets the images to show.
        save(path: str) -> None:
            Saves the image.
        def _add_components() -> None:
            Adds and initializes the gui components of the panel.
    """

    def __init__(self, path: str, save_action: QAction) -> None:
        """
        Creates a Panel.

        Args:
            path (str): The path to the file of the panel.
            save_action (QAction): The action used to save the images.
        """
        super().__init__()
        from ..control.panel_controller import PanelController
        self._image: QLabel = QLabel()
        self._slider: QSlider = QSlider(Qt.Horizontal)
        self._slider_line: QLineEdit = QLineEdit()
        self._loaded: bool = False
        self._panel_controller: PanelController = PanelController(self, save_action)
        self._add_components()
        threading.Thread(
           target=functools.partial(self._panel_controller.load_image, path)
        ).start()

    @property
    def slider(self) -> QSlider:
        """
        Gets the panel slider.

        Returns:
            QSlider: The panel slider.
        """
        return self._slider

    @property
    def slider_line(self) -> QLineEdit:
        """
        Gets the panel slider_line.

        Returns:
            QLineEdit: The panel slider_line.
        """
        return self._slider_line

    @property
    def loaded(self) -> bool:
        """
        Gets the loaded flag.

        Returns:
            bool: The flag that indicates if the image has been loaded.
        """
        return self._loaded

    def set_image(self, image: np.ndarray, k: int = -1) -> None:
        """
        Sets the images to show.

        Args:
            image (np.ndarray): The data of the image to show.
            k (int): The number of singular values of the image.

        Raises:
            ValueError: is the number of channel of the image is not supported.
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
                raise ValueError(QCoreApplication.translate("Gui", "channels"))
        pixmap: QPixmap = QPixmap.fromImage(qimage)
        pixmap = pixmap.scaled(400, 400, Qt.KeepAspectRatioByExpanding)
        self._image.setPixmap(pixmap)
        if k != -1:
            self._slider.setMinimum(0)
            self._slider.setMaximum(k)
            self._slider.setEnabled(True)
            self._loaded = True

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
        self._slider.sliderReleased.connect(self._panel_controller.change_value)
        self._slider_line.setText("0")
        self._slider_line.editingFinished.connect(self._panel_controller.change_line)
        pixmap: QPixmap = QPixmap("./assets/loading.png")
        slider_layout: QHBoxLayout = QHBoxLayout()
        layout: QVBoxLayout = QVBoxLayout()
        layout.setAlignment(Qt.AlignHCenter)
        pixmap = pixmap.scaled(400, 400, Qt.KeepAspectRatioByExpanding)
        self._image.setPixmap(pixmap)
        slider_layout.addWidget(self._slider, stretch=10)
        slider_layout.addWidget(self._slider_line, stretch=1)
        layout.addLayout(slider_layout)
        layout.addWidget(self._image)
        self.setLayout(layout)