from jinja2 import Environment, FileSystemLoader
from pathlib import Path


def main(
    meta: str,
    body: str,
    title,
    tree,
    configuration: dict,
    root: Path,
):
    layout: str = configuration.get("layout")
    layout_dir: Path = root / "layouts" / layout
    # Setup Jinja2
    env = Environment(loader=FileSystemLoader((layout_dir / "html")))
    document_page = env.get_template("doc.html")

    # Render template with markdown HTML
    return document_page.render(body=body, meta=meta, title=title, sidebar_tree=tree)


if __name__ == "__main__":
    main()
