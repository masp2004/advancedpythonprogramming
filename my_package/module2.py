"""
Module 2 - Mathematical utilities.

This module provides basic mathematical operations.
"""


def add(a: int, b: int) -> int:
    """
    Add two numbers together.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The sum of a and b.
    
    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """
    Subtract the second number from the first.
    
    Args:
        a (int): The number to subtract from.
        b (int): The number to subtract.
    
    Returns:
        int: The difference (a - b).
    
    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(1, 1)
        0
    """
    return a - b
