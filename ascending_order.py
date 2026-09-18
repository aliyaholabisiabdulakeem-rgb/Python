number1 = int(input("Enter first integer: "))
number2 = int(input("Enter second integer: "))
number3 = int(input("Enter third integer: "))

if number1 < number2 < number3:
  print(number1, number2, number3)

elif number1 < number3 < number2:
  print(number1, number3, number2)

elif number2 < number1 < number3:
  print(number2, number1, number3)

elif number2 < number3 < number1:
  print(number2, number3, number1)

elif number3 < number1 < number2:
  print(number3, number1, number2)

else:
  print(number3, number2, number1)