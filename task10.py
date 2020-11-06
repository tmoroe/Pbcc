def vowels(text):
    vowels = "aeiou"
    for char in text:
        if char in vowels or char in vowels.upper():
            print(char)
