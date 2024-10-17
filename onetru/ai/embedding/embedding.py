"""
This module contains functions related to text embeddings.
"""

def generate_embedding(text: str) -> list:
    """
    Generates a text embedding from the input text.
    
    Args:
        text (str): The text to generate an embedding for.
    
    Returns:
        list: A list of numerical values representing the embedding.
    """
    # Sample embedding code (just a mock function)
    return [ord(char) for char in text]
