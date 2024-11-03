import os
import logging

# Constants
DEFAULT_SAVE_PATH = './downloads'
FFMPEG_PATH = '/opt/homebrew/bin/ffmpeg'  # Adjust as needed

# Logging configuration
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
