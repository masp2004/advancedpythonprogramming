"""
Module for determining cocktail types based on base alcohol.
"""


def bestimme_cocktail_typ(basis_alkohol: str) -> str:
    """
    Determine the cocktail type based on the base alcohol.
    
    Args:
        basis_alkohol (str): The base alcohol type (case-insensitive).
            Supported values: "rum", "wodka", "gin", "wasser"
    
    Returns:
        str: The name of the recommended cocktail:
            - "Mai Tai" for rum
            - "Moscow Mule" for wodka (vodka)
            - "Gin Tonic" for gin
            - "Virgin Margarita" for wasser (water)
            - "Nicht verfügbar" (not available) for unknown alcohols
    
    Examples:
        >>> bestimme_cocktail_typ("Rum")
        'Mai Tai'
        >>> bestimme_cocktail_typ("gin")
        'Gin Tonic'
        >>> bestimme_cocktail_typ("whiskey")
        'Nicht verfügbar'
    """
    basis_alkohol = basis_alkohol.lower()
    if basis_alkohol == "rum":
        return "Mai Tai"
    elif basis_alkohol == "wodka":
        return "Moscow Mule"
    elif basis_alkohol == "gin":
        return "Gin Tonic"
    elif basis_alkohol == "wasser":
        return "Virgin Margarita"
    else:
        return "Nicht verfügbar"