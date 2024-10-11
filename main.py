import argparse
import logging
import utils.log

from rich import print

# Import pour les tests
from time import sleep

def main():
    # Tests pour le logging
    log.info("Info message")
    sleep(1)
    log.debug("Debug message")
    sleep(1)
    log.warning("Warning message")
    sleep(1)
    log.error("Error message")
    sleep(1)
    log.error("[bold red blink]Server is shutting down![/]", extra={"markup": True})
    sleep(1)
    log.error("123 will be highlighted")
    sleep(1)
    log.error("123 will not be highlighted", extra={"highlighter": None})
    sleep(1)
    try:
        print(1 / 0)
    except Exception:
        log.exception("Exception : unable print!")


def parse_arguments():
    # Instanciation du parser d'arguments
    parser = argparse.ArgumentParser(
                    prog='Log utility',
                    description="This program is a log parser utility using rich !")

    # Ajout de l'option verbose
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Increase log verbosity.",
    )

    return parser.parse_args()


if __name__ == "__main__":
    # Récupération des arguments
    args = parse_arguments()
    # Initialisation du log
    utils.log.init_logging(args)
    # Instanciation du log
    log = logging.getLogger('log')
    # Startup print with emoji :)
    print("[bold blue]Log utility[/bold blue]", ":memo:")
    # If verbose
    if args.verbose: log.debug('Verbose mod activated')
    # Start main function
    main()
