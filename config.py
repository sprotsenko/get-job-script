import logging

# File paths
file_path = 'job_pages_urls.txt'
jobs_output_file = 'matched_jobs.txt'

# Keywords for the job search
keywords = ['technical writer', 'content writer', 'writer']

# Logging configuration
def setup_logging(log_file='app.log'):
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=log_file,
        filemode='a'
    )

# Initialize logging
setup_logging()