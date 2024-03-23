import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):
    """
    The class representing the main window of the application.

    Methods:
        add_components():
            Load the gui components on the window.
        add_menubar():
            Creates the menubar and load it in the window.
        add_toolbar():
            Creates the toolbar and load it in the window.
    """

    def __init__(self) -> None:
        """
        Creates an Application.
        """
        super().__init__()
        self.title("ImageS-VD")
        self.geometry("800x500")
        self.add_components()
        self.mainloop()

    def add_components(self) -> None:
        """
        Load the gui components on the window.
        """
        self.add_menubar()
        self.add_toolbar()

    def add_menubar(self) -> None:
        """
        Creates the menubar and load it in the window.
        """
        menubar: tk.Menu = tk.Menu(self)
        file: tk.Menu = tk.Menu(menubar, tearoff=0)
        imagesvd: tk.Menu = tk.Menu(menubar, tearoff=0)
        file.add_command(label="Open", command=lambda: print("Open"))
        imagesvd.add_command(label="About", command=lambda: print("Ciao"))
        imagesvd.add_command(label="Exit", command=lambda: self.destroy())
        menubar.add_cascade(label="File", menu=file)
        menubar.add_cascade(label=self.title(), menu=imagesvd)
        self.config(menu=menubar)

    def add_toolbar(self) -> None:
        """
        Creates the toolbar and load it in the window.
        """
        toolbar: ttk.Frame = ttk.Frame(self)
        toolbar.pack(side="top", fill="x")
        ttk.Button(toolbar, text="Open", command=lambda: print("Open")).pack(side="left")
