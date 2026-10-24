word = input("Enter a 3-digit word: ")
reverse = word[2] + word[1] + word[0]

if word == reverse:
  print("word is palindrome")
else:
  print("word is not palindrome")