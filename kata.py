def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def is_prime(number):
    if number < 1:
        return False
    for count in range(2, number):
        if number % count == 0:
            return False
    return True

def subtract_two_numbers(number1, number2):
    if number1 > number2:
        return number1 - number2
    else:
        return number2 - number1

def divide_two_integer(number1, number2):
    if number2 == 0:
        return 0
    else:
        return number1 / number2

def factor_of(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    return count

def is_square(number):
    for index in range(1, number + 1):
        if index * index == number:
            return True
    else:
        return False

def is_palindrome(number):
    original = number
    reversed = 0
    while number > 0:
        digit = number % 10
        reversed = reversed * 10 + digit
        number = number // 10
    if original == reversed:
        return True
    else:
     return False

def factorial_of(number):
    factorial = 1
    for index in range(1, number + 1):
        factorial *= index;
    return factorial;

def square_of(number):
    return number * number


print(is_even(4))
print(is_prime(9))
print(subtract_two_numbers(14, 19))
print(divide_two_integer(15,5))
print(divide_two_integer(3, 0))
print(factor_of(10))
print(is_square(25))
print(is_palindrome(54345))
print(factorial_of(5))
print(square_of(2))

