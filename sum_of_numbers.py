numbers = print("Enter a number: ")

while (numbers >= 10):   
    sum = 0
while numbers > 0 :
    num = numbers % 10
    sum += num
    numbers = (numbers - num) / 10

numbers = sum;

print(numbers);

