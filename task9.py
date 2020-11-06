def multiples():
    multiples = [3, 5]
    table = []
    result = 0
    i = 0

    for num in multiples:
        while (i * num) < 1000:
            if not(i * num) in table:
                table.append(i * num)
            i += 1
        i = 0
    for num in table:
        result += num
    print(result)
