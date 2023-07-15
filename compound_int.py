def compound_interest(principal, rate, years):
  amount = principal * (1 + rate)**years
  return amount

print("The compound interest on Rs. 10000 at 10% interest for 5 years is Rs.", compound_interest(10000, 0.1, 5))
