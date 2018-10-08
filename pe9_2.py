def file():

    while True:
        letters= input('Give a string of four letters:')

        if len(letters) == 4:
            print(letters, 'is done')
            break
        else:
            print('This word has', len(letters),'letters')


file()
