"""
Module for classifying numbers as positive/negative and even/odd.
"""


def classify_number(num: int) -> str:
    """
    Classify a number based on its sign and parity.
    
    Args:
        num (int): The number to classify.
    
    Returns:
        str: A classification string that describes the number:
            - "Negative even" for negative even numbers
            - "Negative odd" for negative odd numbers
            - "Positive even" for positive even numbers
            - "Positive odd" for positive odd numbers
            - "Zero" for zero
    
    Examples:
        >>> classify_number(-4)
        'Negative even'
        >>> classify_number(3)
        'Positive odd'
        >>> classify_number(0)
        'Zero'
    """
    if num < 0:
        if num % 2 == 0:
            return "Negative even"
        else:
            return "Negative odd"
    elif num > 0:
        if num % 2 == 0:
            return "Positive even"
        else:
            return "Positive odd"
    else:
        return "Zero"