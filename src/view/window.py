import os.path
from PySide6.QtWidgets import QMainWindow, QToolBar, QScrollArea, QTabWidget, QMenuBar, QMenu
from PySide6.QtGui import QAction
from .panel import Panel


class Window(QMainWindow):
    """
    The class representing the main window of the application.

    Attributes:
        _tab_widget (QTabWidget): The widget used as main part of the window.
        _menu_controller (MenuController): The controller used for the window menu.

    Methods:
        add_tab(path: str) -> None:
            Adds a tab to the main port of the window.
        _add_components() -> None:
            Adds the gui components to the window.
        _add_menubar() -> None:
            Creates the menubar and load it in the window.
        _add_toolbar() -> None:
            Creates the toolbar and load it in the window.
        _add_tab_widget() -> None:
            Creates the main part of the window.
    """

    def __init__(self) -> None:
        """
        Creates a Window.
        """
        super().__init__()
        from ..control.menu_controller import MenuController
        self._tab_widget: QTabWidget = QTabWidget()
        self._menu_controller: MenuController = MenuController(self)
        self.setWindowTitle("ImageS-VD")
        self.setGeometry(100, 100, 800, 600)
        self._add_components()
        self.show()

    def add_tab(self, path: str) -> None:
        """
        Adds a tab to the main port of the window.

        Args:
            path (str): the path to file to open.
        """
        self._tab_widget.addTab(Panel(path), os.path.split(path)[1])

    def _add_components(self) -> None:
        """
        Adds the gui components to the window.
        """
        self._add_menubar()
        self._add_toolbar()
        self._add_tab_widget()

    def _add_menubar(self) -> None:
        """
        Creates the menubar and load it in the window.
        """
        menubar: QMenuBar = self.menuBar()
        file_menu: QMenu = menubar.addMenu("File")
        about_menu: QMenu = menubar.addMenu(self.windowTitle())
        open_action: QAction = QAction(self)
        save_action: QAction = QAction(self)
        self._menu_controller.register_widget("open", open_action)
        self._menu_controller.register_widget("save", save_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        about_action: QAction = QAction("About", self)
        about_action.triggered.connect(lambda: print("Ciao"))
        about_menu.addAction(about_action)
        exit_action: QAction = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        about_menu.addAction(exit_action)

    def _add_toolbar(self) -> None:
        """
        Creates the toolbar and load it in the window.
        """
        toolbar: QToolBar = QToolBar()
        self.addToolBar(toolbar)
        open_action: QAction = QAction(self)
        save_action: QAction = QAction(self)
        self._menu_controller.register_widget("open", open_action, True)
        self._menu_controller.register_widget("save", save_action, True)
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)

    def _add_tab_widget(self) -> None:
        """
        Creates the main part of the window.
        """
        scroll_area: QScrollArea = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self._tab_widget)
        self.setCentralWidget(scroll_area)
