# Task 8.3

def find_unique_value(numbers):
    for num in numbers:
        if numbers.count(num) == 1:
            return num
    return None

