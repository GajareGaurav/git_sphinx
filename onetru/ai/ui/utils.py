"""
Utilities for handling UI-related tasks for OneTru AI Workbench.
"""

import os

def init_config(log=False):
    """
    Initialize configuration settings for the server, particularly logging.

    Args:
        log (bool): Whether to enable logging mode. Defaults to False.
    """
    if log:
        print("Logging is enabled.")
    else:
        print("Logging is disabled.")
    
    config_path = os.getenv('CONFIG_PATH', './config.json')
    print(f"Configuration loaded from {config_path}")


def handle_ui_message(message: str) -> str:
    """
    Processes a UI message before displaying it.

    Args:
        message (str): The raw message from the UI.

    Returns:
        str: The processed message, ready for UI display.
    """
    return message.capitalize()


def validate_message_format(message: str) -> bool:
    """
    Validates if the given message follows the correct format.

    Args:
        message (str): The message content to be validated.

    Returns:
        bool: True if the message format is valid, False otherwise.
    """
    return isinstance(message, str) and len(message) > 0
