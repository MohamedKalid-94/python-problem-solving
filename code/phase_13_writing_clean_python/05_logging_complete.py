"""
Phase 13 - Writing Clean Python
05 Logging
Use logging instead of print() for messages about what the program is doing.
"""

import logging
import sys

from helpers import separator

logger = logging.getLogger(__name__)      # one logger per file


# ---------- BAD ----------
def bad_process(data):
    print("processing")              # no level, cannot be switched off
    try:
        return 10 / data
    except Exception as error:       # too broad, and the traceback is lost
        print(error)


# ---------- CLEAN ----------
def process_data(data):
    logger.info("Processing started")
    logger.debug("Input value is %s", data)    # %s: built only if DEBUG is on
    try:
        result = 10 / data
    except ZeroDivisionError:
        logger.exception("Division failed")    # message AND the traceback
        return None
    logger.info("Processing completed")
    return result


def main():
    # Configure logging once, in main(), not when the file is imported
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s | %(name)s | %(message)s",
        stream=sys.stdout,
    )

    separator("BAD: print and a broad except")
    print("Result:", bad_process(0))

    separator("CLEAN: logging with levels")
    print("Result:", process_data(5))

    separator("CLEAN: the error is logged with a traceback")
    print("Result:", process_data(0))

    separator("All five levels")
    logger.debug("DEBUG: details for developers")
    logger.info("INFO: normal progress")
    logger.warning("WARNING: something unexpected, but it still works")
    logger.error("ERROR: something failed")
    logger.critical("CRITICAL: the program may not continue")

    separator("Changing the level hides the small messages")
    logging.getLogger().setLevel(logging.WARNING)
    logger.debug("You will NOT see this")
    logger.info("You will NOT see this either")
    logger.warning("You WILL see this warning")


if __name__ == "__main__":
    main()