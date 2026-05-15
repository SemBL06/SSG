from pathlib import Path
import os


def meta(yaml_dict: dict, PUBLIC: Path, output_file: Path):
    css_file = PUBLIC / "css" / "documentation.css"
    syntax_file = PUBLIC / "css" / "syntax.css"
    relative_css = os.path.relpath(css_file, start=output_file.parent)
    relative_syntax = os.path.relpath(syntax_file, start=output_file.parent)
    return f"""
    <meta charset="{yaml_dict.get("charset", "UTF-8")}" />
    <meta name="description" content="{yaml_dict.get("description", "Change me in the .md!")}" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="icon" type="image/x-icon" href="favicon.ico">
    <link rel="stylesheet" href="{relative_css}" />
    <link rel="stylesheet" href="{relative_syntax}" />
    <title>{yaml_dict.get("title", "Default Title")}</title>
    """


def nav(configuration, output_files, output_file, PUBLIC):
    core = configuration["core"]
    sidebar_tree = renderable_tree(build_tree(output_files, PUBLIC), output_file)

    return core["site_title"], sidebar_tree


def build_tree(paths, PUBLIC):
    tree = {}

    for path in paths:
        relative = path.relative_to(PUBLIC)
        parts = relative.parts

        node = tree

        for part in parts[:-1]:
            node = node.setdefault(part, {})

        node.setdefault("__pages__", []).append(path)

    return tree


def renderable_tree(node, current_page):
    result = []

    for key, value in node.items():
        if key == "__pages__":
            for page in value:
                result.append(
                    {
                        "type": "page",
                        "title": page.stem.replace("_", " ").title(),
                        "path": os.path.relpath(
                            page, start=current_page.parent
                        ).replace("\\", "/"),
                    }
                )

        else:
            result.append(
                {
                    "type": "folder",
                    "title": key.replace("_", " ").title(),
                    "children": renderable_tree(value, current_page),
                }
            )

    return result
