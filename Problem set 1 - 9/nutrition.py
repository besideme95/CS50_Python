fruit = {'apple': 130,
        'avocado':50,
        'banana':110,
        'cantaloupe':50,
        'grapefruit':60,
        'grape':90,
        'honeydew':50,
        'kiwifruit':90,
        'lemon':15,
        'lime':20,
        'nectarine':60,
        'orange':80,
        'peach':60,
        'pear':100,
        'pineapple':50,
        'plum':70,
        'strawberry':50,
        'sweet cherries':100,
        'tangerine':50,
        'watermelon':80}



while True:
    user_input = input('Item: ').lower()
    if user_input in fruit:
        value = fruit[user_input]
        print(f'Calorie: {value}')
        break
    else:
        print('')
        break

