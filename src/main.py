import sys
import tkinter as tk
from model.compressor import Compressor
from view.application import Application


if __name__ == "__main__":
    root: tk.Tk = tk.Tk()
    app: Application = Application(root)
    if len(sys.argv) < 3:
        print("Bad arguments", file=sys.stderr)
        sys.exit(1)
    original_image_path: str = sys.argv[1]
    result_image_path: str = sys.argv[2]
    k = -1
    if len(sys.argv) > 3:
        k: int = int(sys.argv[3])
    compressor: Compressor = Compressor()
    compressor.load(original_image_path)
    compressor.save(result_image_path, k)
