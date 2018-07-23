from . import chapter1

def test_true():
  assert chapter1.contains_duplicate([0,9,4,2,7,9]) == True

def test_false():
  assert chapter1.contains_duplicate([0,6,4,2,7,9]) == True
