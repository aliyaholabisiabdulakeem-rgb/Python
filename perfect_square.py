def perfect_square(numbers):
    list_of_numbers = []
    for count in numbers:
        square_root = count ** 0.5
        if square_root ** 2 == count:
            list_of_numbers.append(count)
    return list_of_numbers
print(perfect_square([16, 9, 3, 24]))




#def find_factorial(numbers):
 #   list_of_numbers = []
  #  factorial = 1
   # for count in range (0, lennumbers):
    #    factorial *= count
     #   list_of_numbers.append(factorial)
    #return list_of_numbers
#print(find_factorial(5))



def factorial_of_numbers(numbers):
    result_list = []
    result = 1
    for index in range (1, numbers[0],1):
        result *= index
    result_list.append(result_list)
    return result_list
print(factorial_of_numbers([5, 3, 4]))
