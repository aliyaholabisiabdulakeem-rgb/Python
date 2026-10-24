list1 = [10, 20, 30]
list2 = [40, 50]

concatenated_list = list1 + list2
print(concatenated_list)

for i in range(len(concatenated_list)):
    print(concatenated_list[i])


def cube_list(values):
    for i in range(len(values)):
        values[i] **= 2
    return values
print(cube_list([1, 2, 3, 4, 5, 6]))


characters = []
characters += 'Birthday'

