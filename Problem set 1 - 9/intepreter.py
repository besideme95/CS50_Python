def main():
    expression_input = input("Expression:")
    expression_input = expression_input.split()
    x = float(expression_input[0])
    y = expression_input[1]
    z = float(expression_input[2])
    if y == "+":
        y = x + z
        y = round(y,1)
        print(y)
    elif y == "-":
        y = x - z
        y = round(y,1)
        print(y)
    elif y == "*":
        y = x * z
        y = round(y,1)
        print(y)
    elif y == "/":
        y = x / z
        y = round(y,1)
        print(y)
    else:
        print("Error")

main()

