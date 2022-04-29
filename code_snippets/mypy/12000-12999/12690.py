import logging

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('output.txt')
logger = logging.getLogger()
for handler in (stream_handler, file_handler):
    logger.addHandler(handler)
