import os
import sys
from PySide6.QtWidgets import QApplication
from src.model.compressor import Compressor
from src.view.window import Window


def cli_usage(index: int) -> None:
    """
    Executes the program in the command line mode.

    Args:
        index: index of the cli flag in the argv.
    """
    try:
        if len(sys.argv) < index + 3:
            print("Bad arguments", file=sys.stderr)
            sys.exit(1)
        original_image_path: str = sys.argv[index + 1]
        result_image_path: str = sys.argv[index + 2]
        k: int = -1
        if len(sys.argv) > index + 3:
            k = int(sys.argv[index + 3])
        compressor: Compressor = Compressor()
        compressor.load(original_image_path)
        if os.path.splitext(result_image_path)[1] != ".npz":
            compressor.compose(k)
        compressor.save(result_image_path)
    except Exception as ex:
        print("Errore: ", ex)


if __name__ == "__main__":
    index: int = -1
    if "--cli" in sys.argv:
        index = sys.argv.index("--cli")
    if "-c" in sys.argv:
        index = sys.argv.index("-c")
    if index != -1:
        cli_usage(index)
        sys.exit(0)
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
