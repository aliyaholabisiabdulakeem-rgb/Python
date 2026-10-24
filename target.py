numbers = [2, 7, 11, 15]
target = 18

for index in range(len(numbers)):
    for count in range(index + 1, len(numbers)):
        if numbers[index] + numbers[count] == target:
            print(numbers[index], numbers[count])
            print(index, count)
