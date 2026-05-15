from rich.progress import track

import python.generator.sitemap as sitemap
import python.generator.parser.main as parser
import python.generator.parser.yaml_dict as yamlParser
import python.generator.html.markdown as mdHTML
import python.generator.html.yaml as yamlHTML
import python.generator.html.main as combine
import python.generator.robots as robots
from pathlib import Path
import shutil
from json import loads


def main(ROOT_DIR: Path):
    CONTENT_DIR = ROOT_DIR / "content"
    PUBLIC = ROOT_DIR / "public"

    configuration: dict = loads(
        (ROOT_DIR / "python" / "configuration" / "configuration.json").read_text()
    )

    clear_public(PUBLIC)

    output_files, input_files = create_files(CONTENT_DIR, PUBLIC, configuration)
    # CSS
    layout: str = configuration.get("layout")
    layout_dir: Path = ROOT_DIR / "layouts" / layout / "CSS"
    layout_dir.copy(PUBLIC / "css")
    from pygments.formatters import HtmlFormatter

    css = HtmlFormatter().get_style_defs(".codehilite")
    (PUBLIC / "css" / "syntax.css").write_text(css)

    xml = ""
    for output_file, input_file in track(
        zip(output_files, input_files), description="Making pages..."
    ):
        # Parsing
        yaml, markdown = parser.main(input_file)
        dict_meta, dict_sitemap = yamlParser.main(yaml)
        dict_sitemap["url"] = output_file.relative_to(PUBLIC).as_posix()

        # HTML
        body = mdHTML.main(markdown)
        meta = yamlHTML.meta(dict_meta, PUBLIC, output_file)
        title, sidebar_tree = yamlHTML.nav(
            configuration, output_files, output_file, PUBLIC
        )
        html = combine.main(meta, body, title, sidebar_tree, configuration, ROOT_DIR)
        output_file.write_text(html, encoding="utf-8")

        # Sitemap
        xml += sitemap.generate_xml(dict_sitemap, configuration)

    sitemap.create_xml(xml, ROOT_DIR)


def clear_public(public: Path):
    if public.exists():
        shutil.rmtree(public)


def create_files(CONTENT_DIR: Path, PUBLIC: Path, configuration):
    """
    Creates all the files

    Returns:
    The created files.
    """
    output_files = []
    input_files = []
    robot_exists = False
    for file in CONTENT_DIR.rglob("*"):
        # Skip directories
        if file.is_dir():
            continue
        relative_path = file.relative_to(CONTENT_DIR)

        if file.suffix == ".md":
            output_path = PUBLIC / relative_path.with_suffix(".html")

            output_files.append(output_path)
            input_files.append(file)
            output_path.parent.mkdir(parents=True, exist_ok=True)

        else:
            # Avoid error for dir not found
            output_path = PUBLIC / relative_path
            output_path.parent.mkdir(parents=True, exist_ok=True)

            output_path.write_bytes(file.read_bytes())
            if file.name == "robots.txt":
                robot_exists = True

    # Robots.txt generation
    if not robot_exists:
        robots_txt = robots.main(configuration)
        (PUBLIC / "robots.txt").write_text(robots_txt)

    return output_files, input_files
