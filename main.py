import questionary
import python.text_formatter as formatter
from python.configuration.main import main as configure
from python.generator.main import main as generator
from pathlib import Path


def main():
    ROOT_DIR = Path(__file__).parent
    while True:
        formatter.clear_screen()
        formatter.title("[red]SSG: Startup", "By Sem!")

        choice = questionary.select(
            "What do you want to do?",
            choices=["Configure", "Generate Site", "Exit"],
        ).ask()

        match choice:
            case "Configure":
                configure()

            case "Generate Site":
                generator(ROOT_DIR)

            case "Exit":
                formatter.clear_screen()
                formatter.title("[red]Thank you for using SSG")
                break


if __name__ == "__main__":
    main()
