def max_num(*numbers):
    result = 0
    for num in numbers:
        if num > result:
            result = num
    return result
