from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSlider


class Panel(QWidget):
    """
    The panel page of the window's tab widget.

    Attributes:
        _image (QPixmap): The graphic representation of the image to compress.
        _slider (QSlider): The slider used to select the number of singular values.
        _panel_controller (PanelController): The controller of the panel.
    """

    def __init__(self, path: str) -> None:
        """
        Creates a Panel.

        Args:
            path (str): The path to the file of the panel,
        """
        super().__init__()
        from ..control.panel_controller import PanelController
        self._image: QPixmap = QPixmap("./assets/loading.png")
        self._slider: QSlider = QSlider(Qt.Horizontal)
        self._panel_controller: PanelController = PanelController(self)
        self._slider.setMinimum(0)
        self._slider.setMaximum(100)
        self.setEnabled(False)
        self._slider.valueChanged.connect(lambda: print(self._slider.value()))
        layout: QVBoxLayout = QVBoxLayout()
        layout.setAlignment(Qt.AlignHCenter)
        self._image = self._image.scaled(400, 400, Qt.KeepAspectRatioByExpanding)
        label: QLabel = QLabel()
        label.setPixmap(self._image)
        layout.addWidget(self._slider)
        layout.addWidget(label)
        self.setLayout(layout)
        self._panel_controller.load_image(path)
