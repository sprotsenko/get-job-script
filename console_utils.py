import os

def clear_console():
    """Clears the console"""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/MacOS
        os.system('clear')