def main():
    question = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    # I did most of the part correctly but earlier I did not assign a variable for user_input(question) therefore I had an error
    result = user_input(question)
    if result == True:
        print("Yes")
    else:
        print("No")

def user_input(str):
    str = str.replace(" ","")
    str = str.lower()
    match str:
        case "fortytwo" | "forty-two"| "42":
            return True
        case _:
            return False


main()

