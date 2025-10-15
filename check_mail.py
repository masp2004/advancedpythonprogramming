"""
Module for email address validation.

This module provides the CheckMail class for validating email addresses
according to basic RFC 5322 rules.
"""


class CheckMail:
    """
    A class for checking the validity of email addresses.
    
    This validator checks for basic email format compliance including:
    - Presence of exactly one "@" symbol
    - Text before the "@" symbol (local part)
    - At least one dot in the domain part
    - A top-level domain with at least 2 characters
    """
    
    def isValidMailAddress(self, address: str) -> bool:
        """
        Check if an email address is valid.
        
        A valid email address must:
        - Be a non-empty string
        - Contain exactly one "@" symbol
        - Have text before the "@" symbol (local part)
        - Have a domain part with at least one dot
        - Have a top-level domain with at least two characters
        
        Args:
            address (str): The email address to validate.
        
        Returns:
            bool: True if the address is valid, False otherwise.
        
        Examples:
            >>> checker = CheckMail()
            >>> checker.isValidMailAddress("user@example.com")
            True
            >>> checker.isValidMailAddress("invalid.email")
            False
            >>> checker.isValidMailAddress("@example.com")
            False
        """
        # Invalid if not a string or empty
        if not isinstance(address, str) or not address:
            return False
        
        # Exactly one "@" symbol must be present
        if address.count("@") != 1:
            return False
        
        local, domain = address.split("@")
        
        # Text must exist before the @ symbol
        if not local:
            return False
        
        # The domain part must contain a dot
        if "." not in domain:
            return False
        
        # The top-level domain (part after the last dot) must be
        # at least two characters long
        if len(domain.split(".")[-1]) < 2:
            return False
        
        return True
