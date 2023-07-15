def is_palindrome(str1):
  str2 = ""
  for i in range(len(str1) - 1, -1, -1):
    str2 += str1[i]
  return str1 == str2

str1 = "racecar"
print("Is 'racecar' a palindrome? ", is_palindrome(str1))
