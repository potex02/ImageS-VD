import os.path
from PySide6.QtWidgets import QMainWindow, QToolBar, QScrollArea, QTabWidget, QMenuBar, QMenu, QWidget
from PySide6.QtGui import QAction
from .panel import Panel
from .tab_widget import TabWidget


class Window(QMainWindow):
    """
    The class representing the main window of the application.

    Attributes:
        _menu_controller (MenuController): The controller used for the window menu.
        _tab_widget (TabWidget): The widget used as main part of the window.

    Methods:
        add_tab(path: str) -> None:
            Adds a tab to the main port of the window.
        get_current_panel() -> Panel:
            Gets the current active panel.
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
        self._menu_controller: MenuController = MenuController(self)
        self._tab_widget: TabWidget = TabWidget(self._menu_controller.actions["save"])
        self.setWindowTitle("ImageS-VD")
        self.setGeometry(100, 100, 800, 600)
        self._add_components()
        self.show()

    def add_tab(self, path: str) -> None:
        """
        Adds a tab to the main port of the window.

        Args:
            path (str): The path to file to open.
        """
        self._tab_widget.addTab(Panel(path, self._menu_controller.actions["save"]), os.path.split(path)[1])

    def get_current_panel(self) -> Panel:
        """
        Gets the current active panel
        """
        widget: QWidget = self._tab_widget.currentWidget()
        return widget if isinstance(widget, Panel) else None

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
        file_menu.addAction(self._menu_controller.actions["open"])
        file_menu.addAction(self._menu_controller.actions["save"])
        about_menu.addAction(self._menu_controller.actions["about"])
        exit_action: QAction = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        about_menu.addAction(exit_action)

    def _add_toolbar(self) -> None:
        """
        Creates the toolbar and load it in the window.
        """
        toolbar: QToolBar = QToolBar()
        self.addToolBar(toolbar)
        toolbar.addAction(self._menu_controller.actions["open"])
        toolbar.addAction(self._menu_controller.actions["save"])

    def _add_tab_widget(self) -> None:
        """
        Creates the main part of the window.
        """
        scroll_area: QScrollArea = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self._tab_widget)
        self.setCentralWidget(scroll_area)
