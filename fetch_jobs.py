import requests
from bs4 import BeautifulSoup
import logging

def fetch_jobs(careers_url, keywords):
    """Fetch jobs from the identified careers page and search for jobs matching the keywords.

    Args:
        careers_url (str): The URL of the careers page to fetch jobs from.
        keywords (list): A list of keywords to match against job titles.

    Returns:
        list: A list of matched job strings or an error message if the fetch fails.
    """
    try:
        logging.info(f"Fetching jobs from: {careers_url}")
        response = requests.get(careers_url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all job links
        job_listings = soup.find_all('a', href=True, string=True)
        
        matched_jobs = []
        for job in job_listings:
            job_title = job.text.strip().lower()
            if any(keyword.lower() in job_title for keyword in keywords):
                # Build full job URL
                job_url = job['href']
                if not job_url.startswith('http'):
                    job_url = careers_url.rstrip('/') + '/' + job_url.lstrip('/')
                
                matched_jobs.append(f"- {job.text.strip()} | {job_url}")
                logging.info(f"Matched job: {job.text.strip()} | {job_url}")
        
        if not matched_jobs:
            logging.warning(f"No matching jobs found on: {careers_url}")

        return matched_jobs

    except requests.exceptions.RequestException as e:
        error_message = f"Error fetching jobs from {careers_url}: {e}"
        logging.error(error_message)
        return f"Error fetching jobs from {careers_url}: {e}"