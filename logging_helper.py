import logging

def setup_logger():
    # logging.basicConfig(format="%(asctime)s  %(levelname)s \t %(name)s \t %(message)s", level=logging.DEBUG)
    # logging_format = "%(levelname)-8s %(name)-40s %(funcName)-30s %(message)-150s %(asctime)s"
    logging_format = "%(levelname)-8s %(name)-20s %(funcName)-20s %(message)-150s"

    # Log to console:
    logging.basicConfig(format=logging_format, level=logging.INFO)

    # Log to file:
    # logging.basicConfig(format=logging_format, level=logging.WARNING, filename="app.log", filemode="w")


