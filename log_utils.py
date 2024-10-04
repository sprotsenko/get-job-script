# my_project/log_utils.py

def log_to_file(file_path, message):
    """Append messages to a log file."""
    with open(file_path, 'a', encoding='utf-8') as log_file:
        log_file.write(message + '\n')

def clear_file(file_path):
    """Clear the content of the file if it exists."""
    with open(file_path, 'w', encoding='utf-8') as log_file:
        log_file.write('')  # Overwrite with nothing