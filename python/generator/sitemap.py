from jinja2 import Environment, FileSystemLoader
from pathlib import Path


def generate_xml(sitemap_setting: dict, configuration):
    url_page = configuration["core"].get(
        "domain_name", "http://localhost/"
    ) + sitemap_setting.get("url")
    lastmod = sitemap_setting.get("lastmod", "")
    changefreq = sitemap_setting.get("changefreq", "")
    priority = sitemap_setting.get("priority", "")
    return f"""
       <url>

      <loc>{url_page}</loc>

      {f"<lastmod>{lastmod}</lastmod>" if lastmod else ""}

      {f"<changefreq>{changefreq}</changefreq>" if changefreq else ""}

      {f"<priority>{priority}</priority>" if priority else ""}

      </url>
    """


def create_xml(xml: str, root):
    layout_dir: Path = root / "layouts"

    env = Environment(loader=FileSystemLoader(layout_dir))
    sitemap = env.get_template("sitemap.xml")

    sitemap_xml = sitemap.render(content=xml)
    Path(root / "public" / "sitemap.xml").write_text(sitemap_xml)
