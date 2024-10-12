import argparse
import logging
import utils.log

from rich import print

# Import for testing
from time import sleep

def main():
    # Logging examples for testing
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
    # Arguments parser calling
    parser = argparse.ArgumentParser(
                    prog='Log utility',
                    description="This program is a log parser utility using rich !")

    # Adding verbos option
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Increase log verbosity.",
    )

    return parser.parse_args()


if __name__ == "__main__":
    # Retrieve arguments
    args = parse_arguments()
    # Logger initialisation
    utils.log.init_logging(args)
    # Logger calling
    log = logging.getLogger('log')
    # Startup print with emoji :)
    print("[bold blue]Log utility[/bold blue]", ":memo:")
    # Print if verbose mod is activated
    if args.verbose: log.debug('Verbose mod activated')
    # Start main function
    main()
