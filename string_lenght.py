statement = input("Enter a string: ")
length = len(statement)

if length < 5:
  print("short string")

elif length >= 5 and length <= 10:
  print("medium string")

else:
  print("long string")