def sum_of_unique(numbers):
    sum = 0
    for count in (len(numbers)):
        occurrences = 0
        for index in (len(numbers)):
            if numbers[count] == numbers[index]:
                occurrences = occurrences + 1
                
        if (occurrences == 1):
             sum += numbers[count]
            
    return sum

numbers1 = [1, 2, 3, 2]
print(sumOfUnique(numbers1))

numbers2 = [1, 1, 1, 1, 1]
print(sumOfUnique(numbers2))






















































#def sum_of_unique(numbers):
#    sum = 0
#    count = 0
#    while count < len(numbers):
#        occurrences = 0
#        index = 0
#  
#        while index < len(numbers):
#            if numbers[count] == numbers[index]:
#                occurrences = occurrences + 1
#            index = index + 1
#        
#        if occurrences == 1:
#            sum = sum + numbers[count]
#        
#        count = count + 1
#    
#    return sum
#
#numbers1 = [1, 2, 3, 2]
#print(sum_of_unique(numbers1)) 
#
#numbers2 = [1, 1, 1, 1, 1]
#print(sum_of_unique(numbers2)) 











