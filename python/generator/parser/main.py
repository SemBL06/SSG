# Bestand opsplitsen in yml en HTML
from pathlib import Path


def main(file: Path):
    content = file.read_text(encoding="utf-8")
    return tuple(content.split("---", 2)[1:])
