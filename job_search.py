# job_search.py

from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
from fetch_jobs import fetch_jobs
from log_utils import log_to_file

def find_jobs(urls, jobs_output_file, error_log_file, keywords):
    """Read URLs from file, find matching jobs, and log errors."""
    
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
                        log_to_file(error_log_file, matched_jobs)
                    elif matched_jobs:
                        tqdm.write(f"\nMatching jobs found on {url}:")
                        for job in matched_jobs:
                            tqdm.write(job)
                            log_to_file(jobs_output_file, job)
                except Exception as e:
                    log_to_file(error_log_file, f"Error processing {url}: {e}")
                finally:
                    pbar.update(1)

    tqdm.write(f"\nJob search completed. Results saved in '{jobs_output_file}'.")