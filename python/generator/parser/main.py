# Bestand opsplitsen in yml en HTML
from pathlib import Path


def main(file: Path):
    content = file.read_text()
    return tuple(content.split("---", 2)[1:])
