def common_char(text1, text2):
    common_char_list = []
    for char in text2:
        if char in text1:
            if not char in common_char_list:
                common_char_list.append(char)
    print("Common letters: ", end="")
    print(*common_char_list, sep=", ")
