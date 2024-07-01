from cocktails import bestimme_cocktail_typ

def test_rum():
    assert bestimme_cocktail_typ("Rum") == "Mai Tai"

def test_wodka():
    assert bestimme_cocktail_typ("Wodka") == "Moscow Mule"

def test_gin():
    assert bestimme_cocktail_typ("Gin") == "Gin Tonic"

def test_wasser():
    assert bestimme_cocktail_typ("Wasser") == "Virgin Margarita"

def test_tequila():
    assert bestimme_cocktail_typ("Tequila") == "Nicht verfügbar"

def test_whiskey():
    assert bestimme_cocktail_typ("Whiskey") == "Nicht verfügbar"

def test_empty_string():
    assert bestimme_cocktail_typ("") == "Nicht verfügbar"

def test_lowercase_wodka():
    assert bestimme_cocktail_typ("wodka") == "Moscow Mule"

def test_mixed_case_gin():
    assert bestimme_cocktail_typ("GiN") == "Gin Tonic"

def test_uppercase_rum():
    assert bestimme_cocktail_typ("RUM") == "Mai Tai"

def test_invalid_input_numbers():
    assert bestimme_cocktail_typ("123") == "Nicht verfügbar"

def test_partial_match():
    assert bestimme_cocktail_typ("gin and tonic") == "Nicht verfügbar"
