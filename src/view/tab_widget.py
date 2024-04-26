from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTabWidget, QApplication


class TabWidget(QTabWidget):
    """
    The class representing the tabs of the application.
    """

    def __init__(self) -> None:
        """
        Creates a TabWidget.
        """
        super().__init__()
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.removeTab)