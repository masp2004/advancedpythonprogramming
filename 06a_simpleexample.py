# Beispielcode: Eine Funktion, die zwei Zahlen addiert
def add_numbers(a, b):
    return a + b

# Test für die Funktion add_numbers
def test_add_numbers():
    assert add_numbers(1, 2) == 3
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, -1) == -2