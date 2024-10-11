import logging
from rich.logging import RichHandler

def init_logging(args):
    if args.verbose:
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(message)s",
            handlers=[RichHandler(rich_tracebacks=True)],
            datefmt="%d/%m/%Y %I:%M:%S",
        )
    else:
        logging.basicConfig(
            level=logging.INFO,
            format="%(message)s",
            handlers=[RichHandler(rich_tracebacks=True)],
            datefmt="%d/%m/%Y %I:%M:%S",
        )
