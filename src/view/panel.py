from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class Panel(QWidget):
    """
    The panel page of the window's tab widget.
    """

    def __init__(self) -> None:
        """
        Creates a Panel.
        """
        super().__init__()
        layout: QVBoxLayout = QVBoxLayout()
        layout.addWidget(QLabel("Image"))
        self.setLayout(layout)