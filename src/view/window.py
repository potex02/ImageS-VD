import sys
from PySide6.QtWidgets import QMainWindow, QToolBar, QLabel, QVBoxLayout, QScrollArea, QWidget, QTabWidget
from PySide6.QtGui import QAction, QIcon


class Window(QMainWindow):
    """
    The class representing the main window of the application.
    """

    def __init__(self):
        """
        Creates an Application.
        """
        super().__init__()
        self._icons = self.create_icons()
        self.setWindowTitle("ImageS-VD")
        self.setGeometry(100, 100, 800, 500)
        self.add_components()
        self.show()

    def create_icons(self):
        """
        Creates the dictionary of gui icons.
        """
        # Nota: PyQt5 non supporta direttamente PhotoImage. È necessario utilizzare QPixmap per le immagini.
        # Tuttavia, per mantenere le cose semplici, userò solo i nomi delle icone a scopo dimostrativo.
        return {"open": "./assets/open.png"}  # Store paths to image files.

    def add_components(self):
        """
        Load the gui components on the window.
        """
        self.add_menubar()
        self.add_toolbar()

    def add_menubar(self):
        """
        Creates the menubar and load it in the window.
        """
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        imagesvd_menu = menubar.addMenu(self.windowTitle())

        open_action = QAction("Open", self)
        open_action.triggered.connect(lambda: print("Open"))
        file_menu.addAction(open_action)

        about_action = QAction("About", self)
        about_action.triggered.connect(lambda: print("Ciao"))
        imagesvd_menu.addAction(about_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        imagesvd_menu.addAction(exit_action)

    def add_toolbar(self):
        """
        Creates the toolbar and load it in the window.
        """
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        open_action = QAction(self)
        open_action.setIcon(QIcon("./assets/open.png"))
        open_action.triggered.connect(lambda: print("Open"))
        toolbar.addAction(open_action)
