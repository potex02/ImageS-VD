
from typing import NoReturn
import tkinter as tk
from tkinter import ttk


class Application:
    """
    The class representing the gui application.

    Attributes:
        _root (tk.Tk): The tkinter Tk root window.

    Methods:
        add_components():
            Load the gui components on the window.
        add_menubar():
            Creates the menubar and load it in the window.
    """

    def __init__(self, root: tk.Tk) -> None:
        """
        Creates an Application.

        Args:
             root (tk.Tk): The tkinter Tk root window.
        """
        self._root = root
        self._root.title("ImageS-VD")
        self._root.geometry("800x500")
        self.add_components()
        self._root.mainloop()

    def add_components(self) -> None:
        """
        Load the gui components on the window.
        """
        ttk.Label(self._root, text="ImageS-VD").pack()
        self.add_menubar()

    def add_menubar(self) -> None:
        """
        Creates the menubar and load it in the window.
        """
        menubar: tk.Menu = tk.Menu(self._root)
        file: tk.Menu = tk.Menu(menubar, tearoff=0)
        imagesvd: tk.Menu = tk.Menu(menubar, tearoff=0)
        file.add_command(label="Open", command=lambda: print("Open"))
        imagesvd.add_command(label="About", command=lambda: print("Ciao"))
        imagesvd.add_command(label="Exit", command=lambda: self._root.destroy())
        menubar.add_cascade(label="File", menu=file)
        menubar.add_cascade(label=self._root.title(), menu=imagesvd)
        self._root.config(menu=menubar)
