# Get Job Script

This script automates the process of scraping job listings from various websites and aggregates them into a single file. It includes logging capabilities and allows users to search for specific job-related keywords.
  
## Requirements

Make sure you have the libraries listed in `requirements.txt`.

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install required dependencies.
4. Configure the input/output file and logging in `config.py`. The input file must have a `.txt` format, with each link on a new line. Also add the key words for search.
5. Run the script with the `main.py` file:

   ```bash
   python main.py

6. Check the results in the output file you set in step 4.

## Logging
The script logs important actions and events, such as:

- Requests sent to job websites
- Responses and status codes
- Parsed job listings
- Errors and exceptions
- Logs are saved in the `logs/` directory and provide insights into the script’s execution, making it easier to troubleshoot issues.

## Project Structure

```plaintext
get-job-script/
│
├── README.md            # Project documentation
├── main.py              # Main script to run the job search
├── requirements.txt     # Python dependencies
├── logging_config.py    # Logging configuration module
├── utils.py             # Utility functions for job scraping and parsing
└── logs/                # Directory where log files are saved