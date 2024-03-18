
name_input = input("Key in your input")

words = name_input.split()


for word in words:
    new_word = ''
    for letter in word:
        if letter.isupper():
            new_word += '_'
            new_word += letter
        else:
            new_word += letter
    print(new_word.lower())

