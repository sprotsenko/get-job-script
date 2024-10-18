import logging
import os
from config import log_file

def setup_logging():
    # Ensure the directory for the log file exists
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Set up logging
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=log_file,
        filemode='a'
    )