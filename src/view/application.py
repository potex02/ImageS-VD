import tkinter as tk
from tkinter import ttk


class Application:
    """
    The class representing the gui application.

    Attributes:
        _root (np.ndarray): The tkinter Tk root window.

    Methods:
        add_components() -> None:
            Load the gui components on the window.
    """
    def __init__(self, root: tk.Tk):
        self._root = root
        self._root.title = "ImageS-VD"
        self._root.geometry("800x500")
        self.add_components()
        self._root.mainloop()

    def add_components(self) -> None:
        """
        Load the gui components on the window.
        """
        ttk.Label(self._root, text="ImageS-VD")