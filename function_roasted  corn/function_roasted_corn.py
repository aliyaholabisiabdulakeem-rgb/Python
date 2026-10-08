# length_of_string

def length_of_string(string):
    length_of_string = len(string)
    return length_of_string


#first two and last two
def first_two_last_two(string):
    if len(string) < 2:
        return ""
    return string[:2] + string[-2:]

# Adding 'ing' and 'ly'
def add_ing_or_ly(string):
    if len(string) <= 3:
        return string
    if string[-3:] == 'ing':
        return string + 'ly'
    else:
        return(string + 'ing')

# Longest and lenght of a string
def longest_and_lenght(strings):
    longest = strings[0]
    for index in strings:
        if len(index) > len(longest):
            longest = index
    return  longest, len(longest)


# Odd index of string
def odd_index_of_string(string):
    result = ""
    for count in range(len(string)):
        if count % 2 == 1:
            result += string[count]
    return result


# minimum numbers from a given list of numbers
def minimum_of_a_list(numbers):
    minimum = numbers[0]
    for index in numbers:
        if index < minimum:
            minimum = index
    return minimum


# maximum numbers from a a given list of numbers
def maximum_of_a_list(numbers):
    maximum = numbers[0]
    for index in numbers:
        if index > maximum:
            maximum = index
    return maximum


# repeat strings in the repeated numbers of times
def repeat_string(string, number):
    if int(number) != number:
        return string
    result = ""
    for index in range(number):
        result += string
    return result


# ruturning squared parameters
def return_square_Of(numbers):
    for index in numbers:
            print("\t", index * index, end = "")


     
# sum of squared parameters
def return_square_sum_Of(numbers):
    total = 0
    for index in numbers:
        total = total + index * index
    return total




print(length_of_string("semicolon"))
print(first_two_last_two("As"))
print(first_two_last_two("semicolon"))
print(add_ing_or_ly("abc"))
print(add_ing_or_ly("string"))
print(longest_and_lenght(["apple", "corn", "pin", "breakfast"]))
print(odd_index_of_string("semicolon"))
print(minimum_of_a_list([2,1,4,5,6,7]))
print(maximum_of_a_list([2,1,4,5,6,7]))
print(repeat_string("hello", 3))
print(repeat_string("hi", 4.5))
print(return_square_Of([2, 3, 4, 5, 6, 1]))
print(return_square_sum_Of([2,3,4,5,7]))
