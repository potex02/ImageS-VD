import json
import csv
import os
import sys
import xml.etree.ElementTree as ET
import numpy as np
import yaml
from PIL import Image


def get_compression_rate(original_file, compressed_file):
    original_size = os.path.getsize(original_file)
    compressed_size = os.path.getsize(compressed_file)
    compression_rate = 1 - (compressed_size / original_size)
    return compression_rate


def save_channels(channels: list[np.ndarray], path: str) -> bool:
    extensions: list[str] = ["json", "xml", "yaml", "csv"]
    index: int = path.rfind('.')
    if index == -1:
        return False
    extension: str = result_image_path[index + 1:]
    if not extension in extensions:
        return False
    result: list[list[int]] = [channel.tolist() for channel in channels]
    match extension:
        case "json":
            with open(path, 'w') as file:
                json.dump(result, file, indent=4)
        case "xml":
            root: ET.Element = ET.Element("root")
            for i in result:
                row: ET.Element = ET.SubElement(root, "channel")
                for j in i:
                    value: ET.Element = ET.SubElement(row, "value")
                    value.text = str(j)
            tree: ET.ElementTree = ET.ElementTree(root)
            tree.write(path, encoding="utf-8", xml_declaration=True, method="xml")
        case "yaml":
            with open(path, 'w') as file:
                yaml.dump(result, file, indent=4)
        case "csv":
            with open(path, 'w', newline='') as file:
                writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                writer.writerows(result)
    return True


def compress_image(image_path: str, result_image_path: str, k: int) -> None:
    image = Image.open(image_path)
    image_array: np.ndarray = np.array(image)
    index: int = image_path.rfind('.')
    if index != -1 and image_path[index + 1:].lower() == "pbm":
        image_array = np.where(image_array, 0, 255)
    channels: int = 1
    compressed_channels: list[np.ndarray] = list[np.ndarray]()
    if len(image_array.shape) == 3:
        _, _, channels = image_array.shape
    for i in range(channels):
        channel: np.ndarray
        if channels == 1:
            channel = image_array
        else:
            channel = image_array[:, :, i]
        u: np.ndarray
        s: np.ndarray
        vt: np.ndarray
        u, s, vt = np.linalg.svd(channel, full_matrices=False)
        print(s[k])
        s[k:] = 0
        compressed_channels.append(np.dot(u, np.dot(np.diag(s), vt)))
    if save_channels(compressed_channels, result_image_path):
        return
    compressed_image_array: np.ndarray = np.stack(compressed_channels, axis=-1)
    compressed_image_array = np.clip(compressed_image_array, 0, 255).astype(np.uint8)
    result: Image.Image = Image.fromarray(compressed_image_array.squeeze())
    result.save(result_image_path)
    print(get_compression_rate(image_path, result_image_path))


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Bad arguments", file=sys.stderr)
        sys.exit(1)
    original_image_path: str = sys.argv[1]
    result_image_path: str = sys.argv[2]
    k: int = int(sys.argv[3])
    compress_image(original_image_path, result_image_path, k)
