# main.py

import config 
from log_utils import clear_file
from url_utils import read_urls_from_file
from console_utils import clear_console
from job_search import find_jobs

# Clear old log files if they exist
clear_file(config.jobs_output_file)
#clear_file(config.error_log_file)

# Clear console
clear_console()

# Read URLs from file
urls = read_urls_from_file(config.file_path)

# Find jobs and log errors using configurations from config.py
find_jobs(urls, config.jobs_output_file, config.keywords)