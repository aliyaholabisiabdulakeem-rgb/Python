name = input("Enter name: ")
length = len(name)

if length >= 3 and length <= 5:
  print("Hi", name + "!")
elif length >5:
  print("Hello", name + "!")