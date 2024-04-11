from typing import Dict, Tuple
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QFileDialog
from .action import Action
from ..view.window import Window


class MenuController:
    """
    The class used as controller for the app menu.

    Attributes:
        _window (Window): The window controlled by the controller.
        _actions: (Dict[str, Action]): The dictionary of the menu actions.

    Methods:
        register_widget(action_name: str, widget: QAction, icon: bool) -> None:
            Registers a widget to an action.
        _open() -> None:
            Opens a file.
    """

    def __init__(self, window: Window) -> None:
        """
        Creates a new MenuController.

        Args:
            window (Window): The window controlled by the controller.
        """
        self._window: Window = window
        self._actions: Dict[str, Action] = {
            "open": Action(self._open, "Open", "./assets/open.png")
        }

    def register_widget(self, action_name: str, widget: QAction, icon: bool = False) -> None:
        """
        Registers a widget to an action.

        Args:
            action_name (str): The key of the action in the dictionary.
            widget (QAction): The widget to register.
            icon (bool): Flag indicating if the widget must show the icon instead of the text.
        """
        self._actions[action_name].register_widget(widget, icon)

    def _open(self) -> None:
        """
        Opens a file.
        """
        path: Tuple[str, str] = QFileDialog.getOpenFileName(self._window, 'Open File')
        self._window.add_tab(path[0])
