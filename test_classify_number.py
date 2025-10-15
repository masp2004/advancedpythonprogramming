"""
Test suite for the classify_number module.

This module contains tests for the classify_number function,
ensuring it correctly classifies positive/negative and even/odd numbers.
"""

from classify_number import classify_number


def test_classify_number_even():
    """
    Test classification of even numbers (both positive and negative).
    """
    assert classify_number(-4) == "Negative even"   # Test negative even number
    assert classify_number(8) == "Positive even"    # Test positive even number
    assert classify_number(2) == "Positive even"    # Test positive even number
    assert classify_number(-2) == "Negative even"


def test_classify_number_odd():
    """
    Test classification of odd numbers (both positive and negative).
    """
    assert classify_number(-3) == "Negative odd"    # Test negative odd number
    assert classify_number(3) == "Positive odd"     # Test positive odd number
    assert classify_number(-1) == "Negative odd"    # Test negative odd number
    assert classify_number(1) == "Positive odd"     # Test positive odd number


def test_classify_number_zero():
    """
    Test classification of zero.
    """
    assert classify_number(0) == "Zero"             # Test zero
