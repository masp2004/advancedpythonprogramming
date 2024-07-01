def bestimme_cocktail_typ(basis_alkohol):
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