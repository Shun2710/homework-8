# Task 8.1

def add_one(digits):
    number = int(''.join(map(str, digits)))
    number += 1
    result = list(map(int, str(number)))

    return result

print(add_one([1, 2, 3, 4]))
print(add_one([9, 9, 9]))
print(add_one([0]))