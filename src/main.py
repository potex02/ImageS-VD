import sys
from model.compressor import Compressor


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Bad arguments", file=sys.stderr)
        sys.exit(1)
    original_image_path: str = sys.argv[1]
    result_image_path: str = sys.argv[2]
    k: int = int(sys.argv[3])
    compressor: Compressor = Compressor()
    compressor.load(original_image_path)
    compressor.save(result_image_path, k)
