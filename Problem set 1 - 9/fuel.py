while True:
    try:
        user_input = input('Fraction: ').split('/')
        x = int(user_input[0])
        y = int(user_input[1])
        if x > y:
            continue
        output = round((x/y)*100)
        max_range = (99/100)*100
        min_range = (1/100)*100
        if output >= max_range:
            print('F')
            break
        elif output <= min_range:
            print('E')
            break
        else:
            print(f'{output}%')
            break

    except(ValueError, ZeroDivisionError):
        continue
