from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class Panel(QWidget):
    """
    The panel page of the window's tab widget.
    """

    def __init__(self, path: str) -> None:
        """
        Creates a Panel.

        Args:
            path (str): The path to the file of the panel,
        """
        super().__init__()
        layout: QVBoxLayout = QVBoxLayout()
        layout.addWidget(QLabel("Image"))
        self.setLayout(layout)