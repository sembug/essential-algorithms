from . import chapter1

def test_zero():
    assert chapter1.gcd(5, 0) == 5

def test_normal_case():    
    assert chapter1.gcd(10, 15) == 5
