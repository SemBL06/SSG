import python.text_formatter as formatter
import questionary as q


def main():
    formatter.clear_screen()
    formatter.title("[red]SSG: Configuration of Robots.txt")
    enable_robots = q.confirm("Enable robot.txt?").ask()
    if enable_robots:
        all_robots = q.confirm("All robots are allowed?").ask()  # Disallow: / (refuse)
        crawl_delay = q.text("What is the crawl delay?").ask()  # Crawl-delay: 10
        site_map = q.confirm(
            "Include sitemap (auto generated)"
        ).ask()  # Sitemap: reqhge
        restricted_pages = []

        while True:
            answer = q.text("Restricted pages for robots? (Enter to stop)").ask()
            if answer:
                restricted_pages.append(answer)
            else:
                break
    robots = {
        "enabled": enable_robots,
        "all_robots_allowed": all_robots,
        "crawl_delay": crawl_delay,
        "site_map_enabled": site_map,
        "restricted_pages": restricted_pages,
    }
    formatter.title("[green]SSG: Completed Configuration Wizard")
    return robots
