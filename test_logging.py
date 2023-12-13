import logging
def test_log():
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler("file.log")
    format = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    handler.setFormatter(format)
    logger.addHandler(handler)
    logger.setLevel(logging.ERROR)
    logger.debug("hi")
    logger.info("bye")
    logger.warning("hey")
    logger.error("noow")
    logger.critical("tyen")