"""
This module defines the base classes for analytics models.
"""

class AnalyticsModel:
    """
    A base class for analytics models.
    """
    
    def __init__(self, name: str):
        """
        Initializes the model with a name.
        
        Args:
            name (str): The name of the model.
        """
        self.name = name
    
    def train(self, data):
        """
        Trains the model on the given data.
        
        Args:
            data: The training data.
        """
        print(f"Training model {self.name}...")
