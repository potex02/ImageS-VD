from typing import Dict, Tuple
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QFileDialog
from ..view.window import Window


class MenuController:
    """
    The class used as controller for the app menu.

    Attributes:
        _window (Window): The window controlled by the controller.
        _actions: (Dict[str, QAction]): The dictionary of the menu actions.

    Methods:
        _open() -> None:
            Opens a file.
        _save() -> None:
            Saves a file
    """

    def __init__(self, window: Window) -> None:
        """
        Creates a new MenuController.

        Args:
            window (Window): The window controlled by the controller.
        """
        self._window: Window = window
        self._actions: Dict[str, QAction] = {
            "open": QAction(QIcon("./assets/open.png"), "Open"),
            "save": QAction(QIcon("./assets/save.png"), "Save")
        }
        self._actions["open"].triggered.connect(self._open)
        self._actions["open"].setShortcut("ctrl+o")
        self._actions["save"].triggered.connect(self._save)
        self._actions["save"].setShortcut("ctrl+s")
        self._actions["save"].setEnabled(False)

    @property
    def actions(self) -> Dict[str, QAction]:
        """
        Gets an actions

        Returns:
            Dict[str, QAction]: The dictionary of the actions of the controller.
        """
        return self._actions

    def _open(self) -> None:
        """
        Opens a file.
        """
        path: Tuple[str, str] = QFileDialog.getOpenFileName(self._window, 'Open File')
        if path[0]:
            self._window.add_tab(path[0])

    def _save(self) -> None:
        """
        Saves a file
        """
        path: Tuple[str, str] = QFileDialog.getSaveFileName(self._window, "Save file")
        if path[0]:
            self._window.get_current_panel().save(path[0])