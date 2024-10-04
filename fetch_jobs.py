# my_project/fetch_jobs.py

import requests
from bs4 import BeautifulSoup

def fetch_jobs(careers_url, keywords):
    """Fetch jobs from the identified careers page and search for jobs matching the keywords."""
    try:
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
        
        return matched_jobs

    except requests.exceptions.RequestException as e:
        return f"Error fetching jobs from {careers_url}: {e}"