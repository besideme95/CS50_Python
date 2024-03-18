name = input("What's your name?")


def main():
    if name == "Harry" or name == "Hermione" or name == "Ron":
        print("Gryffindor")
    elif name == "Draco":
        print("Slytherin")
    else:
        print("who?")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("gryffindor")

    case "Draco":
        print("Slytherin")
    case _:
        print("who")
