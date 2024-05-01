from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QTabWidget, QTabBar
from ..control.action import Action


class TabWidget(QTabWidget):
    """
    The class representing the tabs of the application.

    Attributes:
        _save_action (Action): The action used to save the images.

    Methods:
        mouse_event(self, event: QMouseEvent) -> None:
            Handles the mouse press on the tab title.
        close_tab(index: int) -> None:
            Closes a tab of the widget and closes the app if there isn't any open tab.
    """
    def __init__(self, save_action: Action) -> None:
        """
        Creates a TabWidget.
        """
        super().__init__()
        self._save_action = save_action
        self.setTabBar(QTabBar(self))
        self.tabBar().mousePressEvent = self.mouse_event
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_tab)

    def close_tab(self, index: int) -> None:
        """
        Closes a tab of the widget and closes the app if there isn't any open tab.

        Args:
            index (int): The index of the tab to close.
        """
        self.removeTab(index)
        if self.count() == 0:
            QCoreApplication.quit()

    def mouse_event(self, event: QMouseEvent) -> None:
        """
        Handles the mouse press on the tab title.

        Args:
            event (QMouseEvent): The event to handle.
        """
        if event.button() == Qt.MiddleButton:
            index = self.tabBar().tabAt(event.pos())
            if index != -1:
                self.tabCloseRequested.emit(index)
            return
        QTabBar.mousePressEvent(self.tabBar(), event)
        if event.button() == Qt.LeftButton:
            self._save_action.set_enabled(self.currentWidget().loaded)
