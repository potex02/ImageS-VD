import threading
from ..model.compressor import Compressor
from ..view.panel import Panel


class PanelController():
    """
    The class used as controller for an app panel.

    Attributes:
        _panel (Panel): The panel controlled by the controller.
        _compressor (Compressor): The compressor used to compress the panel image.

    Methods:
        register_widget(self, action_name: str, widget: QAction, icon: bool) -> None
        Registers a widget to an action.
    """

    def __init__(self, panel: Panel) -> None:
        self._panel: Panel = panel
        self._compressor: Compressor = Compressor()

    def load_image(self, path: str) -> None:
        threading.Thread(target=lambda: print("Thread")).start()
