from typing import Callable, List
from PySide6.QtGui import QIcon, QAction


class Action:
    """
    Represent an action of the app used to manage the widget's behaviour.

    Attributes:
        _function (Callable[[], None]): The code to execute when the action is called.
        _text (str): The text of the action.
        _icon (QIcon): The icon of the action.
        _widgets (List[QAction]): The list of registered widgets.
        _enabled (bool): The flag that indicates if the action isa enabled.

    Methods:
        register_widget(widget: QAction, icon: bool) -> None:
            Registers a widget to the action.
        set_enabled(enabled: bool) -> None:
            Enables or disables the action.
    """

    def __init__(self, function: Callable[[], None], text: str, icon_path: str, enabled: bool = True) -> None:
        """
        Creates an action.

        Args:
            function (Callable[[], None]): The code to execute when the action is called.
            text (str): The text of the action.
            icon_path (str): The path to the icon.
            enabled (bool): The flag that indicates if the action isa enabled.
        """
        self._function: Callable[[], None] = function
        self._text: str = text
        self._icon: QIcon = QIcon(icon_path)
        self._widgets: List[QAction] = []
        self._enabled = enabled

    def register_widget(self, widget: QAction, icon: bool) -> None:
        """
        Registers a widget to the action.

        Args:
            widget (QAction): The widget to register.
            icon (bool): Flag indicating if the widget must show the icon instead of the text.
        """
        widget.triggered.connect(self._function)
        if icon:
            widget.setIcon(self._icon)
        else:
            widget.setText(self._text)
        widget.setEnabled(self._enabled)
        self._widgets.append(widget)

    def set_enabled(self, enabled: bool) -> None:
        """
        Enables or disables the action.

        Args:
            enabled: The new flag that indicates if the action is enabled.
        """
        self._enabled = enabled
        for i in self._widgets:
            i.setEnabled(enabled)