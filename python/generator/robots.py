def main(configuration):
    robots_configuration: dict = configuration.get("robots", None)
    robots_text = ""
    if robots_configuration:
        if robots_configuration["enabled"]:
            if robots_configuration.get("all_robots_allowed", True):
                robots_text += "User-agent: *\n"
                robots_text += "Disallow:\n"
            else:
                robots_text += "User-agent:\n"
                robots_text += "Disallow: /\n"
            if robots_configuration.get("crawl_delay", "0") != "0":
                robots_text += "Crawl-delay: 10\n"
            if robots_configuration.get("site_map_enabled", True):
                robots_text += f"Sitemap: {configuration.get("core").get("domain_name", "http://localhost/")+"sitemap.xml"}\n"
            for disallowed_file in robots_configuration.get("restricted_pages", []):
                robots_text += f"Disallow: /{disallowed_file}\n"
    return robots_text
