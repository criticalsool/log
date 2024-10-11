import argparse
import logging
import utils.log
from time import sleep

def parse_arguments():
    parser = argparse.ArgumentParser(
                    prog='Log utility',
                    description="This program is a log parser utility using rich !")

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Increase log verbosity.",
    )

    return parser.parse_args()

def main():
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

if __name__ == "__main__":
    args = parse_arguments()
    utils.log.init_logging(args)
    log = logging.getLogger('log example')
    if args.verbose: log.debug('Verbose mod activated')
    main()
