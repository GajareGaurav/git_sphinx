"""
This module contains utility functions for analytics tasks.
"""

def calculate_accuracy(predictions, labels) -> float:
    """
    Calculates the accuracy of model predictions.
    
    Args:
        predictions: The model's predicted values.
        labels: The true labels.
    
    Returns:
        float: The accuracy of the predictions.
    """
    correct = sum(p == l for p, l in zip(predictions, labels))
    return correct / len(labels)
