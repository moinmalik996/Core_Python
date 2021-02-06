import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt="%d/%m/%Y %H:%M:%S")

# logging.debug("This is a debug log")
# logging.info("This is a info log")
# logging.warning("This is a warning log")
# logging.critical("This is a critical log")
# logging.error("This is a error log")

logger = logging.getLogger(__name__)

# Create Handlers
stream_h = logging.StreamHandler()
file_h   = logging.FileHandler('file.log')

# Create Level and Format

stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logging.warning("This is warning")
logging.error("This is error")


