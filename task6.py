def max_num(*numbers):
    r = 0;
    for num in numbers:
        if num > r:
            r = num
    return r
