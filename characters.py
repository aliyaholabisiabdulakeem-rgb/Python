character = input("Enter a single character: ")

if character >= 'A' and character <= 'z':
  print("letters")
elif character >= 'a' and character <= 'z':
  print("letters")
elif character >= '0'and character <= '9':
  print("numbers")
else:
  print("special symbol")