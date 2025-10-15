"""
Simple example module demonstrating basic function testing.

This module contains a basic addition function and corresponding tests,
serving as an introduction to test-driven development.
"""


def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers together.
    
    Args:
        a (int): The first number to add.
        b (int): The second number to add.
    
    Returns:
        int: The sum of a and b.
    
    Examples:
        >>> add_numbers(1, 2)
        3
        >>> add_numbers(-1, 1)
        0
    """
    return a + b


def test_add_numbers():
    """
    Test the add_numbers function with various inputs.
    
    Tests include:
    - Positive numbers
    - Negative and positive number combination
    - Zero values
    - Two negative numbers
    """
    assert add_numbers(1, 2) == 3
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, -1) == -2