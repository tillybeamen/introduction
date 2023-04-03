#1

def countdown(num):
    result = []
    for i in range(num, -1, -1):
        result.append(i)
    return result

print(countdown(5))


#2

def print_and_return(list):
    
    for i in range(list[0]):
        print(list[0])

    return list[1]

print(print_and_return([1,2]))


#3

def first_plus_length(list):
    first = list[0]
    length = len(list)
    sum = first + length
   
    return sum

    # for i in range(list[0]):
    #     print(list)

print(first_plus_length([1,2,3,4,5]))

#4

def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    second_val = lst[1]
    result = []
    for val in lst:
        if val > second_val:
            result.append(val)
    
    return result

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

#5

def length_and_value(size, value):
    return [value] * size



print(length_and_value(4,7))
print(length_and_value(6,2))