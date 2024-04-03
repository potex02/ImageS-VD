from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class Panel(QWidget):
    """
    The panel page of the window's tab widget.

    Attributes:
        _image (QPixmap): The graphic representation of the image to compress.
    """

    def __init__(self, path: str) -> None:
        """
        Creates a Panel.

        Args:
            path (str): The path to the file of the panel,
        """
        super().__init__()
        self._image: QPixmap = QPixmap(path)
        layout: QVBoxLayout = QVBoxLayout()
        layout.setAlignment(Qt.AlignHCenter)
        self._image = self._image.scaled(400, 400, Qt.KeepAspectRatioByExpanding)
        label: QLabel = QLabel()
        label.setPixmap(self._image)
        layout.addWidget(label)
        self.setLayout(layout)