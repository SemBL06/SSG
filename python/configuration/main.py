import python.text_formatter as formatter
import questionary
from questionary import Choice
import python.configuration.robots as robots
import python.configuration.core as conn
import python.configuration.layout as layout
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
CONFIG_PATH = BASE_DIR / "configuration.json"


def main():
    """
    Configuration file for SSG

    Returns:
    True: Everything configured
    False: Not
    """
    configuration = get_configuration()

    formatter.clear_screen()
    formatter.title("SSG: Configuration")

    while True:
        choice = questionary.select(
            "What do you want to configure?",
            choices=[
                Choice(
                    title="Robots.txt ✅" if configuration["robots"] else "Robots.txt",
                    value="robots",
                ),
                Choice(
                    title="Layout ✅" if configuration["layout"] else "Layout",
                    value="layout",
                ),
                Choice(
                    title="Core ✅" if configuration["core"] else "Core",
                    value="core",
                ),
                Choice(title="Exit", value="exit"),
            ],
        ).ask()

        match choice:
            case "robots":
                configuration["robots"] = robots.main()
            case "layout":
                configuration["layout"] = layout.main()
            case "core":
                configuration["core"] = conn.main()
            case "exit":
                for value in configuration.values():
                    if not value:
                        if questionary.confirm(
                            "You did not configure everyhting. Continue?"
                        ).ask():
                            return False
                        else:
                            break
                else:
                    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
                        json.dump(configuration, f)
                    return True


def get_configuration():
    configuration = ""
    is_empty = False
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        try:
            configuration = json.load(f)
        except json.decoder.JSONDecodeError:
            is_empty = True

    return {"robots": "", "layout": "", "core": ""} if is_empty else configuration
