"""
Module 1 - Greeting utilities.

This module provides simple greeting functions.
"""


def greet(name: str) -> str:
    """
    Generate a greeting message for a given name.
    
    Args:
        name (str): The name of the person to greet.
    
    Returns:
        str: A greeting message in the format "Hello, {name}!"
    
    Examples:
        >>> greet("Alice")
        'Hello, Alice!'
        >>> greet("World")
        'Hello, World!'
    """
    return f"Hello, {name}!"
