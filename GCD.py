def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

print("The GCD of 100 and 150 is", gcd(100, 150))
