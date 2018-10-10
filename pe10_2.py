while True:

    import random

    a = random.randrange(1,7)
    b = random.randrange(1,7)

    prison= []

    def monopolythrow():
        while True:
            print('Welcome!\nType something to start rolling the dices!')
            antwoord = input('Choice: ')
            if antwoord != '1':
                print('You need to insert 1 to start rolling!')
                break
            if antwoord == '1':
                print('Now rolling ...\n')
            if a != b:
                print('You rolled', a , 'and', b, 'which gives you a total of', a + b, '!')
                break
            print("You rolled the same number, Let's try that again!\n")
            prison.append('a')
            if len(prison) == 3:
                print('You doubled three times, time to go to prison mate!')
                break

    monopolythrow()
    roll = input('You want to roll again?')
    if roll == 'Yes' or roll == 'yes':
        continue
    else:
        break
