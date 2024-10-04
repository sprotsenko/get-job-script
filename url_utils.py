# my_project/url_utils.py

def read_urls_from_file(file_path):
    """Read job page URLs from a .txt file, one URL per line."""
    with open(file_path, 'r') as file:
        urls = file.read().splitlines()
    return urls
