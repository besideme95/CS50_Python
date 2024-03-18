#create an input
coke = 50
valid_payment = [5,10,25,50]


while coke != 0:
    coke_payment = int(input("Insert Coin: "))
    if coke_payment in valid_payment:
        coke = coke - coke_payment
        if coke > 0:
            print(f'Amount Due: {coke}')
        elif coke == 0:
            print(f'Change Owed: {coke}')
        else:
            x = abs(coke)
            print(f'Change Owed: {x}')
            exit()
    else:
        print(f'Amount Due: {coke}')


