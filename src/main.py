import sys
from model.compressor import Compressor


"""def save_channels(channels: list[np.ndarray], path: str) -> bool:
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
"""


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