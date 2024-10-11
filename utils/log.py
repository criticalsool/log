import logging
from rich.logging import RichHandler


def init_logging(args):
    level=logging.DEBUG
    logfileFormat = "%(asctime)s %(levelname)-8s %(name)-8s %(message)s"
    logfileDateFormat = "[%d/%m/%Y %I:%M:%S]"

    fileHandler = logging.FileHandler('log.log')
    logfileFormatter = logging.Formatter(logfileFormat, logfileDateFormat)
    fileHandler.setFormatter(logfileFormatter)
    
    if args.verbose:
        logging.basicConfig(
            level=level,
            format="%(message)s",
            handlers=[RichHandler(rich_tracebacks=True), fileHandler],
            datefmt=logfileDateFormat
        )
    else:
        logging.basicConfig(
            level=logging.INFO,
            format="%(message)s",
            handlers=[RichHandler(rich_tracebacks=True), fileHandler],
            datefmt=logfileDateFormat
        )
