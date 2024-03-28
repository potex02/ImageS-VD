from typing import Callable
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QPushButton


class Action:
    """
    Represent an action of the app used to manage the widget's behaviour.

    Attributes:
        _function (Callable[[], None]): The code to execute when the action is called.
        _text (str): The text of the action.
        _icon (QIcon): The icon of the action.
    """

    def __init__(self, function: Callable[[], None], text: str, icon_path: str) -> None:
        """
        Creates an action.

        Args:
            function (Callable[[], None]): The code to execute when the action is called.
            text (str): The text of the action.
            icon_path (str): The path to the icon.
        """
        self._function: Callable[[], None] = function
        self._text: str = text
        self._icon: QIcon = QIcon(icon_path)

    def register_widget(self, widget: QAction, icon: bool = False) -> None:
        """
        Registers a widget to the action.

        Args:
            widget (QAction): The widget to register.
            icon (bool): Flag indicating if the widget must show the icon instead of the text.
        """
        widget.triggered.connect(self._function)
        if icon:
            widget.setIcon(self._icon)
            return
        widget.setText(self._text)