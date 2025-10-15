"""
Test suite for the cocktails module.

This module contains tests for the bestimme_cocktail_typ function,
verifying cocktail recommendations based on base alcohol.
"""

from cocktails import bestimme_cocktail_typ


def test_rum():
    """
    Test that rum returns the correct cocktail.
    """
    assert bestimme_cocktail_typ("Rum") == "Mai Tai"
