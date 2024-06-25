import logging
import os
import sys
import locale
from typing import Optional
from PySide6.QtCore import QCoreApplication, QTranslator, QLocale
from PySide6.QtWidgets import QApplication
from src.model.compressor import Compressor
from src.view.window import Window


def load_translations(app: QCoreApplication) -> Optional[QTranslator]:
    """
    Loads the translations file from a qm file.

    Args:
        app (QCoreApplication): The PySide app application.

    Returns:
        Optional[QTranslator]: An optional containing the translator if the loading is successfully.
    """
    translator: QTranslator = QTranslator()
    locale: str = QLocale.system().name()[0: 2]
    file_path: str = f"translations/app_{locale}.qm"
    if not os.path.exists(file_path):
        logging.warning(f"Translation file not found: {file_path}")
        file_path: str = f"translations/app_en.qm"
    if not translator.load(file_path):
        logging.error(f"Failed to load translation file: {file_path}")
        return None
    app.installTranslator(translator)
    return translator


def cli_usage(index: int) -> None:
    """
    Executes the program in the command line mode.

    Args:
        index: index of the cli flag in the argv.
    """
    try:
        app: QCoreApplication = QCoreApplication(sys.argv)
        translator: Optional[QTranslator] = load_translations(app)
        if len(sys.argv) < index + 3:
            logging.error(QCoreApplication.translate("Cli", "bad"))
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
        logging.error(f"Error:\t{ex}")


if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, "")
    logging.getLogger().setLevel(logging.INFO)
    index: int = -1
    if "--cli" in sys.argv:
        index = sys.argv.index("--cli")
    if "-c" in sys.argv:
        index = sys.argv.index("-c")
    if index != -1:
        cli_usage(index)
        sys.exit(0)
    app = QApplication(sys.argv)
    translator: Optional[QTranslator] = load_translations(app)
    window = Window()
    window.show()
    sys.exit(app.exec())
