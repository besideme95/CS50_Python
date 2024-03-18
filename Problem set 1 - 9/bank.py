def main():
    greeting = input("Greeting").lower().strip()
    #.strip() remove the white space in the front and space. It does not remove the middke.
    #if there is an argument inside then it will remove that particular argument within the str.
    if greeting [0:5] == "hello":
    # [] in this context is used for slicing str by creating an index thus h = 0, e = 1 and etc...
    #by stating [0:5], 0 == fist letter and have to +1 because the 5 is where it stop. So hellox, x is where it stop so it does not include.
        print("$0")
    elif greeting [0] == "h":
        print("$20")
    else:
        print("$100")
main()
