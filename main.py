import logging
import os
import sys
import locale
import configparser
from typing import Tuple, Optional
import platformdirs
from PySide6.QtCore import QCoreApplication, QTranslator, QLocale
from PySide6.QtWidgets import QApplication
from src.model.compressor import Compressor
from src.view.window import Window


def load_translations(app: QCoreApplication) -> Optional[Tuple[QTranslator, str]]:
    """
    Loads the translations file from a qm file.

    Args:
        app (QCoreApplication): The PySide app application.

    Returns:
        Optional[Tuple[QTranslator, code]]: An optional tuple containing the translator and the locale code if the loading is successfully.
    """
    path: str = platformdirs.user_config_dir("ImageS-VD", False) + "/imageS-VD.conf"
    locale: str = QLocale.system().name()[0: 2]
    if os.path.exists(path):
        config: configparser.ConfigParser = configparser.ConfigParser()
        config.read(path)
        if "config" in config and "locale" in config["config"]:
            locale = config["config"]["locale"]
    translator: QTranslator = QTranslator()
    file_path: str = f"translations/app_{locale}.qm"
    if not os.path.exists(file_path):
        locale = "en"
        logging.warning(f"Translation file not found: {file_path}")
        file_path: str = f"translations/app_en.qm"
    if not translator.load(file_path):
        logging.error(f"Failed to load translation file: {file_path}")
        return None
    app.installTranslator(translator)
    return (translator, locale)


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
    translator, code = load_translations(app)
    window = Window(code)
    window.show()
    sys.exit(app.exec())