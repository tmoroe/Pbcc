def common_char(text1, text2):
    common = []
    for char in text1:
        if char in text2:
            if not char in common:
                common.append(char)
    for char in common:
        print(char)
