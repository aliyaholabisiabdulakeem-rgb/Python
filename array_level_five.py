def sorted_prime_numbers(numbers):
    new_list = []
    for number in numbers:
        count = 0
        for index in range(1,number):
            if number % index == 0:
                count = count + 1
        if count == 1:
            new_list.append(number)
    return new_list
print (sorted_prime_numbers([4, 5, 2, 1, 9, 54, 3,3]))           



def replace_negative(array):

    new_arr = []
    for count in arr:
        if count < 0:
            new_arr.append(0)
        else:
            new_arr.append(count)
    return new_arr
print(replace_negative([5,-9,3,-6,2,-11, 0, 10]))



def move_zeros(array):
    zeros = 0
    for non_zeros in range(len(array)):
        if array[non_zeros] != 0:
            array[zeros], array[non_zeros] = array[non_zeros], array[zeros]
            zeros += 1
    return array
print(move_zeros([5,0,3,0,2,0,6, 0]))  



def duplicate_numbers(numbers):
    new_list = list() 
    duplicate = list()
    for index in numbers:
        if index 
