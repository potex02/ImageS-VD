from PySide6.QtWidgets import QMainWindow, QToolBar, QVBoxLayout, QWidget, QScrollArea, QLabel, QTabWidget, QMenuBar, \
    QMenu
from PySide6.QtGui import QAction, QIcon
from .panel import Panel


class Window(QMainWindow):
    """
    The class representing the main window of the application.

    Methods:
        add_components() -> None:
            Load the gui components on the window.
        add_menubar() -> None:
            Creates the menubar and load it in the window.
        add_toolbar() -> None:
            Creates the toolbar and load it in the window.
        add_tab_widget() -> None:
            Creates the main part of the window.
    """

    def __init__(self) -> None:
        """
        Creates a Window.
        """
        super().__init__()
        self.setWindowTitle("ImageS-VD")
        self.setGeometry(100, 100, 800, 500)
        self.add_components()
        self.show()

    def add_components(self) -> None:
        """
        Load the gui components on the window.
        """
        self.add_menubar()
        self.add_toolbar()
        self.add_tab_widget()

    def add_menubar(self) -> None:
        """
        Creates the menubar and load it in the window.
        """
        menubar: QMenuBar = self.menuBar()
        file_menu: QMenu = menubar.addMenu("File")
        imagesvd_menu: QMenu = menubar.addMenu(self.windowTitle())
        open_action: QAction = QAction("Open", self)
        open_action.triggered.connect(lambda: print("Open"))
        file_menu.addAction(open_action)
        about_action: QAction = QAction("About", self)
        about_action.triggered.connect(lambda: print("Ciao"))
        imagesvd_menu.addAction(about_action)
        exit_action: QAction = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        imagesvd_menu.addAction(exit_action)

    def add_toolbar(self) -> None:
        """
        Creates the toolbar and load it in the window.
        """
        toolbar: QToolBar = QToolBar()
        self.addToolBar(toolbar)
        open_action: QAction = QAction(self)
        open_action.setIcon(QIcon("./assets/open.png"))
        open_action.triggered.connect(lambda: print("Open"))
        toolbar.addAction(open_action)

    def add_tab_widget(self) -> None:
        """
        Creates the main part of the window.
        """
        tab_widget: QTabWidget = QTabWidget()
        for i in range(5):
            tab_widget.addTab(Panel(), f"Panel {i}")
        scroll_area: QScrollArea = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(tab_widget)
        self.setCentralWidget(scroll_area)
