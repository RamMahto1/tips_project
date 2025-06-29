import logging
import sys
from datetime import datetime
import os

# Create log file with current date
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(os.path.dirname(log_path), exist_ok=True)

# Final log file path
LOG_FILE_PATH = log_path

# Set up logging config
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)
logging.info(f"Logging started. Log file created at {LOG_FILE_PATH}")