def gcd(a, b):
  while (b != 0):
    remainder = a % b
    a = b
    b = remainder
  return a

def find_largest(l):
  largest = l[0]
  for item in l:
    if item > largest:
      largest = item
  return largest
  
def contains_duplicate(l):
  for i in l:
    for j in l:
      if i == j:
        return True
  return False
