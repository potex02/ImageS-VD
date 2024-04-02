from typing import Dict
from PySide6.QtGui import QAction
from . import action


class MenuController:
    """
    The class used as controller for the app menu.

    Attributes:
        _actions: Dict[str, action.Action]: The dictionary of the menu actions.

    Methods:
        register_widget(self, action_name: str, widget: QAction, icon: bool) -> None
        Registers a widget to an action.
    """

    def __init__(self) -> None:
        """
        Creates a new MenuController.
        """
        self._actions: Dict[str, action.Action] = {
            "open": action.Action(lambda: print("Open"), "Open", "./assets/open.png")
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
