"""
Test suite for the CheckMail class.

This module contains comprehensive tests for email address validation,
checking various valid and invalid email formats.
"""

from check_mail import CheckMail


# Create a test instance
myMailChecker = CheckMail()
myMailChecker.isValidMailAddress("a@test.e")


def test_class_CheckMail():
    """
    Test that CheckMail can be instantiated correctly.
    """
    myMailChecker = CheckMail()
    assert isinstance(myMailChecker, CheckMail)


def test_class_CheckMail_no_input():
    """
    Test that empty or None inputs are rejected.
    """
    myMailChecker = CheckMail()
    assert not myMailChecker.isValidMailAddress(None)
    address = ""
    assert not myMailChecker.isValidMailAddress(address)


def test_class_CheckMail_correct_input():
    """
    Test that a valid email address is accepted.
    """
    myMailChecker = CheckMail()
    assert myMailChecker.isValidMailAddress("jonas@test.abc.de")


def test_class_CheckMail_check_for_ats():
    """
    Test that emails must have exactly one @ symbol.
    """
    myMailChecker = CheckMail()
    assert not myMailChecker.isValidMailAddress("jonastest.de")
    assert not myMailChecker.isValidMailAddress("jon@s@test.de")


def test_class_CheckMail_check_text_before_at():
    """
    Test that there must be text before the @ symbol.
    """
    myMailChecker = CheckMail()
    assert not myMailChecker.isValidMailAddress("@jonastest.de")
    assert myMailChecker.isValidMailAddress("a@test.de")


def test_class_CheckMail_check_for_dot():
    """
    Test that the domain must contain a dot and valid TLD.
    """
    myMailChecker = CheckMail()
    assert not myMailChecker.isValidMailAddress("jonas@testde")
    assert not myMailChecker.isValidMailAddress("a@test.e")
