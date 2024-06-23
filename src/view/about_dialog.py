from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from src.view.window import Window


class AboutDialog(QDialog):
    """
    The dialog used as the app about dialog.
    """
    def __init__(self, parent: Window) -> None:
        """
        Creates an AboutDialog.

        Args:
            parent (Window): The application main window.
        """
        super().__init__(parent)
        self.setWindowTitle("About")
        self.setFixedSize(300, 200)
        layout: QVBoxLayout = QVBoxLayout()
        title_label: QLabel = QLabel("ImageS-VD")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title_label)
        version_label: QLabel = QLabel("Version: alpha.")
        layout.addWidget(version_label)
        author_label: QLabel = QLabel("Author: Potex02.")
        layout.addWidget(author_label)
        description_label: QLabel = QLabel("An application to compress images using the SVD.")
        layout.addWidget(description_label)
        license_label: QLabel = QLabel("License: BSD-3.")
        layout.addWidget(license_label)
        button_layout: QLabel = QHBoxLayout()
        close_button: QPushButton = QPushButton("Close")
        close_button.clicked.connect(self.accept)
        button_layout.addStretch()
        button_layout.addWidget(close_button)
        layout.addStretch()
        layout.addLayout(button_layout)
        self.setLayout(layout)