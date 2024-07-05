from typing import Dict, Tuple
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QFileDialog, QMessageBox
from src.view.window import Window
from src.view.about_dialog import AboutDialog


class MenuController:
    """
    The class used as controller for the app menu.

    Attributes:
        _window (Window): The window controlled by the controller.
        _actions: (Dict[str, QAction]): The dictionary of the menu actions.

    Methods:
        _get_supported_formats() -> str:
            Gets all the supported image extensions by the app, plus the .npz extension.
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
            "open": QAction(QIcon("./assets/open.png"), QCoreApplication.translate("Gui", "open")),
            "save": QAction(QIcon("./assets/save.png"), QCoreApplication.translate("Gui", "save")),
            "about": QAction(QCoreApplication.translate("Gui", "about")),
            "exit": QAction(QCoreApplication.translate("Gui", "exit")),
        }
        self._actions["open"].triggered.connect(self._open)
        self._actions["open"].setShortcut("ctrl+o")
        self._actions["save"].triggered.connect(self._save)
        self._actions["save"].setShortcut("ctrl+s")
        self._actions["save"].setEnabled(False)
        self._actions["about"].triggered.connect(self._about)
        self._actions["about"].setShortcut("ctrl+i")
        self._actions["exit"].triggered.connect(window.close)
        self._actions["exit"].setShortcut("ctrl+x")


    @property
    def actions(self) -> Dict[str, QAction]:
        """
        Gets an actions

        Returns:
            Dict[str, QAction]: The dictionary of the actions of the controller.
        """
        return self._actions

    @staticmethod
    def _get_supported_formats() -> str:
        """
        Gets all the supported image extensions by the app, plus the .npz extension.

        Returns:
             String: The string used as dialog filter.
        """
        supported_formats = [
            "*.bmp", "*.jpeg", "*.jpg", "*.jp2", "*.png", "*.ppm", "*.tiff", "*.tif", "*.npz"
        ]
        return "Supported Files (" + " ".join(supported_formats) + ")"

    def _open(self) -> None:
        """
        Opens a file.
        """
        path: Tuple[str, str] = QFileDialog.getOpenFileName(self._window, 'Open File', filter=MenuController._get_supported_formats())
        if path[0]:
            self._window.add_tab(path[0])

    def _save(self) -> None:
        """
        Saves a file
        """
        path: Tuple[str, str] = QFileDialog.getSaveFileName(self._window, "Save file", filter=MenuController._get_supported_formats())
        if path[0]:
            self._window.get_current_panel().save(path[0])

    def _about(self) -> None:
        about_dialog: AboutDialog = AboutDialog(self._window)
        about_dialog.exec()