from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
from fetch_jobs import fetch_jobs
from log_utils import log_to_file
import logging
from collections import Counter

def find_jobs(urls, jobs_output_file, keywords):
    """Read URLs from file, find matching jobs, and log errors."""
    
    # Init counters for jobs and errors
    job_counter = Counter()
    error_counter = Counter()

    logging.info("Starting job search.")
    
    # Use ThreadPoolExecutor for multithreading
    with ThreadPoolExecutor(max_workers=50) as executor:
        # Initialize tqdm for progress bar
        with tqdm(total=len(urls), desc="Processing URLs", unit="url") as pbar:
            futures = {executor.submit(fetch_jobs, url, keywords): url for url in urls}

            for future in as_completed(futures):
                url = futures[future]
                try:
                    matched_jobs = future.result()

                    if isinstance(matched_jobs, str):  # If an error occurred, it's returned as a string
                        logging.error(f"Error fetching jobs from {url}: {matched_jobs}")
                        error_counter[url] += 1 #Count errors
                    elif matched_jobs:
                        logging.info(f"Matching jobs found on {url}: {len(matched_jobs)} jobs")
                        for job in matched_jobs:
                            logging.debug(f"Job found: {job}")
                            log_to_file(jobs_output_file, job)
                        job_counter[url] += 1 #Count jobs found with script
                except Exception as e:
                    logging.exception(f"Error processing {url}: {e}")
                finally:
                    pbar.update(1)

    # Log total jobs and errors
    tqdm.write(f"\nTotal jobs found: {sum(job_counter.values())}")
    tqdm.write(f"Total errors: {sum(error_counter.values())}")
    logging.info(f"Job search completed. Results saved in '{jobs_output_file}'.")
    tqdm.write(f"\nJob search completed. Results saved in '{jobs_output_file}'.")