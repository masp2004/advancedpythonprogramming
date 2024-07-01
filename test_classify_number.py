from classify_number import classify_number

def test_classify_number_even():
    assert classify_number(-4) == "Negative even"   # Testet negative gerade Zahl
    assert classify_number(8) == "Positive even"    # Testet positive gerade Zahl
    assert classify_number(2) == "Positive even"    # Testet positive gerade Zahl
    assert classify_number(-2) == "Negative even"
    

def test_classify_number_odd():    
    assert classify_number(-3) == "Negative odd"    # Testet negative ungerade Zahl
    assert classify_number(3) == "Positive odd"     # Testet positive ungerade Zahl
    assert classify_number(-1) == "Negative odd"    # Testet negative ungerade Zahl
    assert classify_number(1) == "Positive odd"     # Testet positive ungerade Zahl

def test_classify_number_zero():    
    assert classify_number(0) == "Zero"             # Testet null