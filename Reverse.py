def reverse_string(str1):
  str2 = ""
  for i in range(len(str1) - 1, -1, -1):
    str2 += str1[i]
  return str2

str1 = "Hello, world!"
print("The reversed string is", reverse_string(str1))
