import logging
class Baseclass():
    def test_log(self):
        logger = logging.getLogger(__name__)
        handler = logging.FileHandler("file.log")
        format = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        handler.setFormatter(format)
        logger.addHandler(handler)
        logger.setLevel(logging.ERROR)
        return logger