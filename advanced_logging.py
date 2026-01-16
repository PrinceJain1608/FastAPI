import logging
class CustomLogging:
  def myLogger(self):
    logger=logging.getLogger("Custom Logger")
    logger.setLevel(logging.DEBUG)
    ch=logging.StreamHandler()
    consoleFormatter=logging.Formatter("%(asctime)s-%(filename)s-%(name)s:%(message)s")
    ch.setFormatter(consoleFormatter)
    logger.addHandler(ch)
    logger.error("Custom error logging handler")
obj=CustomLogging()
obj.myLogger()

import logging
class CustomLogging:
  def myLogger(self):
    logger=logging.getLogger("Custom Logger")
    logger.setLevel(logging.DEBUG)
    fh=logging.FileHandler("classLogging.log")
    fileFormatter=logging.Formatter("%(asctime)s-%(filename)s-%(name)s:%(message)s")
    fh.setFormatter(fileFormatter)
    logger.addHandler(fh)
    logger.error("Custom error logging handler")
obj=CustomLogging()
obj.myLogger()