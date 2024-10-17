"""
This module contains data transformation functions.
"""

def preprocess_data(data: dict) -> dict:
    """
    Preprocesses input data to make it suitable for model input.
    
    Args:
        data (dict): The raw input data.
    
    Returns:
        dict: The preprocessed data.
    """
    # Sample preprocessing (mock transformation)
    return {key: value.lower() if isinstance(value, str) else value for key, value in data.items()}
